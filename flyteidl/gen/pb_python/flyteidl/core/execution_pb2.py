# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/core/execution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/core/execution.proto',
  package='flyteidl.core',
  syntax='proto3',
  serialized_options=_b('Z4github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/core'),
  serialized_pb=_b('\n\x1d\x66lyteidl/core/execution.proto\x12\rflyteidl.core\x1a\x1egoogle/protobuf/duration.proto\"\x99\x01\n\x11WorkflowExecution\"\x83\x01\n\x05Phase\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0e\n\nSUCCEEDING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\x0b\n\x07\x46\x41ILING\x10\x05\x12\n\n\x06\x46\x41ILED\x10\x06\x12\x0b\n\x07\x41\x42ORTED\x10\x07\x12\r\n\tTIMED_OUT\x10\x08\"\xa7\x01\n\rNodeExecution\"\x95\x01\n\x05Phase\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\x0b\n\x07\x46\x41ILING\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\x12\x0b\n\x07\x41\x42ORTED\x10\x06\x12\x0b\n\x07SKIPPED\x10\x07\x12\r\n\tTIMED_OUT\x10\x08\x12\x13\n\x0f\x44YNAMIC_RUNNING\x10\t\"\x96\x01\n\rTaskExecution\"\x84\x01\n\x05Phase\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\x0b\n\x07\x41\x42ORTED\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\x12\x10\n\x0cINITIALIZING\x10\x06\x12\x19\n\x15WAITING_FOR_RESOURCES\x10\x07\"\xa9\x01\n\x0e\x45xecutionError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\terror_uri\x18\x03 \x01(\t\x12\x35\n\x04kind\x18\x04 \x01(\x0e\x32\'.flyteidl.core.ExecutionError.ErrorKind\".\n\tErrorKind\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04USER\x10\x01\x12\n\n\x06SYSTEM\x10\x02\"\xbb\x01\n\x07TaskLog\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12<\n\x0emessage_format\x18\x03 \x01(\x0e\x32$.flyteidl.core.TaskLog.MessageFormat\x12&\n\x03ttl\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\"/\n\rMessageFormat\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x43SV\x10\x01\x12\x08\n\x04JSON\x10\x02\"J\n\x14QualityOfServiceSpec\x12\x32\n\x0fqueueing_budget\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xc2\x01\n\x10QualityOfService\x12\x34\n\x04tier\x18\x01 \x01(\x0e\x32$.flyteidl.core.QualityOfService.TierH\x00\x12\x33\n\x04spec\x18\x02 \x01(\x0b\x32#.flyteidl.core.QualityOfServiceSpecH\x00\"4\n\x04Tier\x12\r\n\tUNDEFINED\x10\x00\x12\x08\n\x04HIGH\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x07\n\x03LOW\x10\x03\x42\r\n\x0b\x64\x65signationB6Z4github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/coreb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])



_WORKFLOWEXECUTION_PHASE = _descriptor.EnumDescriptor(
  name='Phase',
  full_name='flyteidl.core.WorkflowExecution.Phase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABORTED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=103,
  serialized_end=234,
)
_sym_db.RegisterEnumDescriptor(_WORKFLOWEXECUTION_PHASE)

_NODEEXECUTION_PHASE = _descriptor.EnumDescriptor(
  name='Phase',
  full_name='flyteidl.core.NodeExecution.Phase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABORTED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKIPPED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_OUT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIC_RUNNING', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=255,
  serialized_end=404,
)
_sym_db.RegisterEnumDescriptor(_NODEEXECUTION_PHASE)

_TASKEXECUTION_PHASE = _descriptor.EnumDescriptor(
  name='Phase',
  full_name='flyteidl.core.TaskExecution.Phase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABORTED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAITING_FOR_RESOURCES', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=425,
  serialized_end=557,
)
_sym_db.RegisterEnumDescriptor(_TASKEXECUTION_PHASE)

_EXECUTIONERROR_ERRORKIND = _descriptor.EnumDescriptor(
  name='ErrorKind',
  full_name='flyteidl.core.ExecutionError.ErrorKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=683,
  serialized_end=729,
)
_sym_db.RegisterEnumDescriptor(_EXECUTIONERROR_ERRORKIND)

_TASKLOG_MESSAGEFORMAT = _descriptor.EnumDescriptor(
  name='MessageFormat',
  full_name='flyteidl.core.TaskLog.MessageFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CSV', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=872,
  serialized_end=919,
)
_sym_db.RegisterEnumDescriptor(_TASKLOG_MESSAGEFORMAT)

_QUALITYOFSERVICE_TIER = _descriptor.EnumDescriptor(
  name='Tier',
  full_name='flyteidl.core.QualityOfService.Tier',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1125,
  serialized_end=1177,
)
_sym_db.RegisterEnumDescriptor(_QUALITYOFSERVICE_TIER)


_WORKFLOWEXECUTION = _descriptor.Descriptor(
  name='WorkflowExecution',
  full_name='flyteidl.core.WorkflowExecution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WORKFLOWEXECUTION_PHASE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=234,
)


_NODEEXECUTION = _descriptor.Descriptor(
  name='NodeExecution',
  full_name='flyteidl.core.NodeExecution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NODEEXECUTION_PHASE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=404,
)


_TASKEXECUTION = _descriptor.Descriptor(
  name='TaskExecution',
  full_name='flyteidl.core.TaskExecution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TASKEXECUTION_PHASE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=557,
)


_EXECUTIONERROR = _descriptor.Descriptor(
  name='ExecutionError',
  full_name='flyteidl.core.ExecutionError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='flyteidl.core.ExecutionError.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='flyteidl.core.ExecutionError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_uri', full_name='flyteidl.core.ExecutionError.error_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='flyteidl.core.ExecutionError.kind', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXECUTIONERROR_ERRORKIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=729,
)


_TASKLOG = _descriptor.Descriptor(
  name='TaskLog',
  full_name='flyteidl.core.TaskLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='flyteidl.core.TaskLog.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flyteidl.core.TaskLog.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_format', full_name='flyteidl.core.TaskLog.message_format', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='flyteidl.core.TaskLog.ttl', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TASKLOG_MESSAGEFORMAT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=732,
  serialized_end=919,
)


_QUALITYOFSERVICESPEC = _descriptor.Descriptor(
  name='QualityOfServiceSpec',
  full_name='flyteidl.core.QualityOfServiceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queueing_budget', full_name='flyteidl.core.QualityOfServiceSpec.queueing_budget', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=921,
  serialized_end=995,
)


_QUALITYOFSERVICE = _descriptor.Descriptor(
  name='QualityOfService',
  full_name='flyteidl.core.QualityOfService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tier', full_name='flyteidl.core.QualityOfService.tier', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='flyteidl.core.QualityOfService.spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _QUALITYOFSERVICE_TIER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='designation', full_name='flyteidl.core.QualityOfService.designation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=998,
  serialized_end=1192,
)

_WORKFLOWEXECUTION_PHASE.containing_type = _WORKFLOWEXECUTION
_NODEEXECUTION_PHASE.containing_type = _NODEEXECUTION
_TASKEXECUTION_PHASE.containing_type = _TASKEXECUTION
_EXECUTIONERROR.fields_by_name['kind'].enum_type = _EXECUTIONERROR_ERRORKIND
_EXECUTIONERROR_ERRORKIND.containing_type = _EXECUTIONERROR
_TASKLOG.fields_by_name['message_format'].enum_type = _TASKLOG_MESSAGEFORMAT
_TASKLOG.fields_by_name['ttl'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TASKLOG_MESSAGEFORMAT.containing_type = _TASKLOG
_QUALITYOFSERVICESPEC.fields_by_name['queueing_budget'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_QUALITYOFSERVICE.fields_by_name['tier'].enum_type = _QUALITYOFSERVICE_TIER
_QUALITYOFSERVICE.fields_by_name['spec'].message_type = _QUALITYOFSERVICESPEC
_QUALITYOFSERVICE_TIER.containing_type = _QUALITYOFSERVICE
_QUALITYOFSERVICE.oneofs_by_name['designation'].fields.append(
  _QUALITYOFSERVICE.fields_by_name['tier'])
_QUALITYOFSERVICE.fields_by_name['tier'].containing_oneof = _QUALITYOFSERVICE.oneofs_by_name['designation']
_QUALITYOFSERVICE.oneofs_by_name['designation'].fields.append(
  _QUALITYOFSERVICE.fields_by_name['spec'])
_QUALITYOFSERVICE.fields_by_name['spec'].containing_oneof = _QUALITYOFSERVICE.oneofs_by_name['designation']
DESCRIPTOR.message_types_by_name['WorkflowExecution'] = _WORKFLOWEXECUTION
DESCRIPTOR.message_types_by_name['NodeExecution'] = _NODEEXECUTION
DESCRIPTOR.message_types_by_name['TaskExecution'] = _TASKEXECUTION
DESCRIPTOR.message_types_by_name['ExecutionError'] = _EXECUTIONERROR
DESCRIPTOR.message_types_by_name['TaskLog'] = _TASKLOG
DESCRIPTOR.message_types_by_name['QualityOfServiceSpec'] = _QUALITYOFSERVICESPEC
DESCRIPTOR.message_types_by_name['QualityOfService'] = _QUALITYOFSERVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkflowExecution = _reflection.GeneratedProtocolMessageType('WorkflowExecution', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWEXECUTION,
  __module__ = 'flyteidl.core.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.WorkflowExecution)
  ))
_sym_db.RegisterMessage(WorkflowExecution)

NodeExecution = _reflection.GeneratedProtocolMessageType('NodeExecution', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTION,
  __module__ = 'flyteidl.core.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.NodeExecution)
  ))
_sym_db.RegisterMessage(NodeExecution)

TaskExecution = _reflection.GeneratedProtocolMessageType('TaskExecution', (_message.Message,), dict(
  DESCRIPTOR = _TASKEXECUTION,
  __module__ = 'flyteidl.core.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.TaskExecution)
  ))
_sym_db.RegisterMessage(TaskExecution)

ExecutionError = _reflection.GeneratedProtocolMessageType('ExecutionError', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONERROR,
  __module__ = 'flyteidl.core.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.ExecutionError)
  ))
_sym_db.RegisterMessage(ExecutionError)

TaskLog = _reflection.GeneratedProtocolMessageType('TaskLog', (_message.Message,), dict(
  DESCRIPTOR = _TASKLOG,
  __module__ = 'flyteidl.core.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.TaskLog)
  ))
_sym_db.RegisterMessage(TaskLog)

QualityOfServiceSpec = _reflection.GeneratedProtocolMessageType('QualityOfServiceSpec', (_message.Message,), dict(
  DESCRIPTOR = _QUALITYOFSERVICESPEC,
  __module__ = 'flyteidl.core.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.QualityOfServiceSpec)
  ))
_sym_db.RegisterMessage(QualityOfServiceSpec)

QualityOfService = _reflection.GeneratedProtocolMessageType('QualityOfService', (_message.Message,), dict(
  DESCRIPTOR = _QUALITYOFSERVICE,
  __module__ = 'flyteidl.core.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.QualityOfService)
  ))
_sym_db.RegisterMessage(QualityOfService)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
