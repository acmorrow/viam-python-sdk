"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Operation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    ARGUMENTS_FIELD_NUMBER: builtins.int
    STARTED_FIELD_NUMBER: builtins.int
    id: typing.Text
    method: typing.Text

    @property
    def arguments(self) -> google.protobuf.struct_pb2.Struct:
        ...

    @property
    def started(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    def __init__(self, *, id: typing.Text=..., method: typing.Text=..., arguments: typing.Optional[google.protobuf.struct_pb2.Struct]=..., started: typing.Optional[google.protobuf.timestamp_pb2.Timestamp]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['arguments', b'arguments', 'started', b'started']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['arguments', b'arguments', 'id', b'id', 'method', b'method', 'started', b'started']) -> None:
        ...
global___Operation = Operation

class GetOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___GetOperationsRequest = GetOperationsRequest

class GetOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OPERATIONS_FIELD_NUMBER: builtins.int

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Operation]:
        ...

    def __init__(self, *, operations: typing.Optional[typing.Iterable[global___Operation]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['operations', b'operations']) -> None:
        ...
global___GetOperationsResponse = GetOperationsResponse

class CancelOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text

    def __init__(self, *, id: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___CancelOperationRequest = CancelOperationRequest

class CancelOperationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___CancelOperationResponse = CancelOperationResponse

class BlockForOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text

    def __init__(self, *, id: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___BlockForOperationRequest = BlockForOperationRequest

class BlockForOperationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___BlockForOperationResponse = BlockForOperationResponse