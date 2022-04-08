// Code generated by mockery v1.0.1. DO NOT EDIT.

package mocks

import (
	context "context"

	mock "github.com/stretchr/testify/mock"

	protoiface "google.golang.org/protobuf/runtime/protoiface"
)

// Publisher is an autogenerated mock type for the Publisher type
type Publisher struct {
	mock.Mock
}

type Publisher_Publish struct {
	*mock.Call
}

func (_m Publisher_Publish) Return(_a0 error) *Publisher_Publish {
	return &Publisher_Publish{Call: _m.Call.Return(_a0)}
}

func (_m *Publisher) OnPublish(ctx context.Context, notificationType string, msg protoiface.MessageV1) *Publisher_Publish {
	c := _m.On("Publish", ctx, notificationType, msg)
	return &Publisher_Publish{Call: c}
}

func (_m *Publisher) OnPublishMatch(matchers ...interface{}) *Publisher_Publish {
	c := _m.On("Publish", matchers...)
	return &Publisher_Publish{Call: c}
}

// Publish provides a mock function with given fields: ctx, notificationType, msg
func (_m *Publisher) Publish(ctx context.Context, notificationType string, msg protoiface.MessageV1) error {
	ret := _m.Called(ctx, notificationType, msg)

	var r0 error
	if rf, ok := ret.Get(0).(func(context.Context, string, protoiface.MessageV1) error); ok {
		r0 = rf(ctx, notificationType, msg)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}
