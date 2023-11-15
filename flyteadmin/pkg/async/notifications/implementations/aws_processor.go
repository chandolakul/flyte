package implementations

import (
	"context"
	"time"

	"github.com/NYTimes/gizmo/pubsub"
	"github.com/golang/protobuf/proto"

	"github.com/flyteorg/flyte/flyteadmin/pkg/async"
	"github.com/flyteorg/flyte/flyteadmin/pkg/async/notifications/interfaces"
	"github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/admin"
	"github.com/flyteorg/flyte/flytestdlib/logger"
	"github.com/flyteorg/flyte/flytestdlib/promutils"
)

// TODO: Add a counter that encompasses the publisher stats grouped by project and domain.
type Processor struct {
	email interfaces.Emailer
	interfaces.BaseProcessor
}

// StartProcessing Currently only email is the supported notification because slack and pagerduty both use
// email client to trigger those notifications.
// When Pagerduty and other notifications are supported, a publisher per type should be created.
func (p *Processor) StartProcessing() {
	for {
		logger.Warningf(context.Background(), "Starting notifications processor")
		err := p.run()
		logger.Errorf(context.Background(), "error with running processor err: [%v] ", err)
		time.Sleep(async.RetryDelay)
	}
}

func (p *Processor) run() error {
	var emailMessage admin.EmailMessage
	var err error
	for msg := range p.Sub.Start() {
		p.SystemMetrics.MessageTotal.Inc()
		stringMsg := string(msg.Message())

		_, messageByte, ok := p.FromSQSMessage(msg)
		if !ok {
			continue
		}

		if err = proto.Unmarshal(messageByte, &emailMessage); err != nil {
			logger.Debugf(context.Background(), "failed to unmarshal to notification object from decoded string from message [%s] with err: %v", stringMsg, err)
			p.SystemMetrics.MessageDecodingError.Inc()
			p.MarkMessageDone(msg)
			continue
		}

		if err = p.email.SendEmail(context.Background(), emailMessage); err != nil {
			p.SystemMetrics.MessageProcessorError.Inc()
			logger.Errorf(context.Background(), "Error sending an email message for message [%s] with emailM with err: %v", emailMessage.String(), err)
		} else {
			p.SystemMetrics.MessageSuccess.Inc()
		}

		p.MarkMessageDone(msg)
	}

	// According to https://github.com/NYTimes/gizmo/blob/f2b3deec03175b11cdfb6642245a49722751357f/pubsub/pubsub.go#L36-L39,
	// the channel backing the subscriber will just close if there is an error. The call to Err() is needed to identify
	// there was an error in the channel or there are no more messages left (resulting in no errors when calling Err()).
	if err = p.Sub.Err(); err != nil {
		p.SystemMetrics.ChannelClosedError.Inc()
		logger.Warningf(context.Background(), "The stream for the subscriber channel closed with err: %v", err)
	}

	// If there are no errors, nil will be returned.
	return err
}

func NewProcessor(sub pubsub.Subscriber, emailer interfaces.Emailer, scope promutils.Scope) interfaces.Processor {
	return &Processor{
		email: emailer,
		BaseProcessor: interfaces.BaseProcessor{
			Sub:           sub,
			SystemMetrics: interfaces.NewProcessorSystemMetrics(scope.NewSubScope("processor")),
		},
	}
}
