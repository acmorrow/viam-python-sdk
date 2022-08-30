"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*proto/api/service/sensors/v1/sensors.proto\x12\x1cproto.api.service.sensors.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"\'\n\x11GetSensorsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"Z\n\x12GetSensorsResponse\x12D\n\x0csensor_names\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\x0bsensorNames"n\n\x12GetReadingsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12D\n\x0csensor_names\x18\x02 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\x0bsensorNames"\xe8\x01\n\x08Readings\x125\n\x04name\x18\x01 \x01(\x0b2!.proto.api.common.v1.ResourceNameR\x04name\x12P\n\x08readings\x18\x02 \x03(\x0b24.proto.api.service.sensors.v1.Readings.ReadingsEntryR\x08readings\x1aS\n\rReadingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueR\x05value:\x028\x01"Y\n\x13GetReadingsResponse\x12B\n\x08readings\x18\x01 \x03(\x0b2&.proto.api.service.sensors.v1.ReadingsR\x08readings2\xda\x02\n\x0eSensorsService\x12\x9c\x01\n\nGetSensors\x12/.proto.api.service.sensors.v1.GetSensorsRequest\x1a0.proto.api.service.sensors.v1.GetSensorsResponse"+\x82\xd3\xe4\x93\x02%\x12#/viam/api/v1/service/{name}/sensors\x12\xa8\x01\n\x0bGetReadings\x120.proto.api.service.sensors.v1.GetReadingsRequest\x1a1.proto.api.service.sensors.v1.GetReadingsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/sensors/{name}/readingsBY\n)com.viam.rdk.proto.api.service.sensors.v1Z,go.viam.com/rdk/proto/api/service/sensors/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.sensors.v1.sensors_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n)com.viam.rdk.proto.api.service.sensors.v1Z,go.viam.com/rdk/proto/api/service/sensors/v1'
    _READINGS_READINGSENTRY._options = None
    _READINGS_READINGSENTRY._serialized_options = b'8\x01'
    _SENSORSSERVICE.methods_by_name['GetSensors']._options = None
    _SENSORSSERVICE.methods_by_name['GetSensors']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/viam/api/v1/service/{name}/sensors'
    _SENSORSSERVICE.methods_by_name['GetReadings']._options = None
    _SENSORSSERVICE.methods_by_name['GetReadings']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/sensors/{name}/readings'
    _GETSENSORSREQUEST._serialized_start = 170
    _GETSENSORSREQUEST._serialized_end = 209
    _GETSENSORSRESPONSE._serialized_start = 211
    _GETSENSORSRESPONSE._serialized_end = 301
    _GETREADINGSREQUEST._serialized_start = 303
    _GETREADINGSREQUEST._serialized_end = 413
    _READINGS._serialized_start = 416
    _READINGS._serialized_end = 648
    _READINGS_READINGSENTRY._serialized_start = 565
    _READINGS_READINGSENTRY._serialized_end = 648
    _GETREADINGSRESPONSE._serialized_start = 650
    _GETREADINGSRESPONSE._serialized_end = 739
    _SENSORSSERVICE._serialized_start = 742
    _SENSORSSERVICE._serialized_end = 1088