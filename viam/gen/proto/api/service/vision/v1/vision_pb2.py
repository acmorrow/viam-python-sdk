"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/service/vision/v1/vision.proto\x12\x1bproto.api.service.vision.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"\x19\n\x17GetDetectorNamesRequest"A\n\x18GetDetectorNamesResponse\x12%\n\x0edetector_names\x18\x01 \x03(\tR\rdetectorNames"\xb3\x01\n\x12AddDetectorRequest\x12#\n\rdetector_name\x18\x01 \x01(\tR\x0cdetectorName\x12.\n\x13detector_model_type\x18\x02 \x01(\tR\x11detectorModelType\x12H\n\x13detector_parameters\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x12detectorParameters"\x15\n\x13AddDetectorResponse"\\\n\x14GetDetectionsRequest\x12\x1f\n\x0bcamera_name\x18\x01 \x01(\tR\ncameraName\x12#\n\rdetector_name\x18\x02 \x01(\tR\x0cdetectorName"_\n\x15GetDetectionsResponse\x12F\n\ndetections\x18\x01 \x03(\x0b2&.proto.api.service.vision.v1.DetectionR\ndetections"\x9e\x01\n\tDetection\x12\x13\n\x05x_min\x18\x01 \x01(\x03R\x04xMin\x12\x13\n\x05y_min\x18\x02 \x01(\x03R\x04yMin\x12\x13\n\x05x_max\x18\x03 \x01(\x03R\x04xMax\x12\x13\n\x05y_max\x18\x04 \x01(\x03R\x04yMax\x12\x1e\n\nconfidence\x18\x05 \x01(\x01R\nconfidence\x12\x1d\n\nclass_name\x18\x06 \x01(\tR\tclassName"\x1a\n\x18GetSegmenterNamesRequest"D\n\x19GetSegmenterNamesResponse\x12\'\n\x0fsegmenter_names\x18\x01 \x03(\tR\x0esegmenterNames"F\n\x1dGetSegmenterParametersRequest\x12%\n\x0esegmenter_name\x18\x01 \x01(\tR\rsegmenterName"8\n\x0eTypedParameter\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type"\x80\x01\n\x1eGetSegmenterParametersResponse\x12^\n\x14segmenter_parameters\x18\x01 \x03(\x0b2+.proto.api.service.vision.v1.TypedParameterR\x13segmenterParameters"\xbb\x01\n\x1bGetObjectPointCloudsRequest\x12\x1f\n\x0bcamera_name\x18\x01 \x01(\tR\ncameraName\x12%\n\x0esegmenter_name\x18\x02 \x01(\tR\rsegmenterName\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeType\x127\n\nparameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\nparameters"|\n\x1cGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12?\n\x07objects\x18\x02 \x03(\x0b2%.proto.api.common.v1.PointCloudObjectR\x07objects2\xe2\x08\n\rVisionService\x12\xb3\x01\n\x10GetDetectorNames\x124.proto.api.service.vision.v1.GetDetectorNamesRequest\x1a5.proto.api.service.vision.v1.GetDetectorNamesResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/service/vision/detector_names\x12\xa2\x01\n\x0bAddDetector\x12/.proto.api.service.vision.v1.AddDetectorRequest\x1a0.proto.api.service.vision.v1.AddDetectorResponse"0\x82\xd3\xe4\x93\x02*"(/viam/api/v1/service/vision/add_detector\x12\xa6\x01\n\rGetDetections\x121.proto.api.service.vision.v1.GetDetectionsRequest\x1a2.proto.api.service.vision.v1.GetDetectionsResponse".\x82\xd3\xe4\x93\x02("&/viam/api/v1/service/vision/detections\x12\xb7\x01\n\x11GetSegmenterNames\x125.proto.api.service.vision.v1.GetSegmenterNamesRequest\x1a6.proto.api.service.vision.v1.GetSegmenterNamesResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/vision/segmenter_names\x12\xcb\x01\n\x16GetSegmenterParameters\x12:.proto.api.service.vision.v1.GetSegmenterParametersRequest\x1a;.proto.api.service.vision.v1.GetSegmenterParametersResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/vision/segmenter_parameters\x12\xc4\x01\n\x14GetObjectPointClouds\x128.proto.api.service.vision.v1.GetObjectPointCloudsRequest\x1a9.proto.api.service.vision.v1.GetObjectPointCloudsResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/service/vision/object_point_cloudsBW\n(com.viam.rdk.proto.api.service.vision.v1Z+go.viam.com/rdk/proto/api/service/vision/v1b\x06proto3')
_GETDETECTORNAMESREQUEST = DESCRIPTOR.message_types_by_name['GetDetectorNamesRequest']
_GETDETECTORNAMESRESPONSE = DESCRIPTOR.message_types_by_name['GetDetectorNamesResponse']
_ADDDETECTORREQUEST = DESCRIPTOR.message_types_by_name['AddDetectorRequest']
_ADDDETECTORRESPONSE = DESCRIPTOR.message_types_by_name['AddDetectorResponse']
_GETDETECTIONSREQUEST = DESCRIPTOR.message_types_by_name['GetDetectionsRequest']
_GETDETECTIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetDetectionsResponse']
_DETECTION = DESCRIPTOR.message_types_by_name['Detection']
_GETSEGMENTERNAMESREQUEST = DESCRIPTOR.message_types_by_name['GetSegmenterNamesRequest']
_GETSEGMENTERNAMESRESPONSE = DESCRIPTOR.message_types_by_name['GetSegmenterNamesResponse']
_GETSEGMENTERPARAMETERSREQUEST = DESCRIPTOR.message_types_by_name['GetSegmenterParametersRequest']
_TYPEDPARAMETER = DESCRIPTOR.message_types_by_name['TypedParameter']
_GETSEGMENTERPARAMETERSRESPONSE = DESCRIPTOR.message_types_by_name['GetSegmenterParametersResponse']
_GETOBJECTPOINTCLOUDSREQUEST = DESCRIPTOR.message_types_by_name['GetObjectPointCloudsRequest']
_GETOBJECTPOINTCLOUDSRESPONSE = DESCRIPTOR.message_types_by_name['GetObjectPointCloudsResponse']
GetDetectorNamesRequest = _reflection.GeneratedProtocolMessageType('GetDetectorNamesRequest', (_message.Message,), {'DESCRIPTOR': _GETDETECTORNAMESREQUEST, '__module__': 'proto.api.service.vision.v1.vision_pb2'})
_sym_db.RegisterMessage(GetDetectorNamesRequest)
GetDetectorNamesResponse = _reflection.GeneratedProtocolMessageType('GetDetectorNamesResponse', (_message.Message,), {'DESCRIPTOR': _GETDETECTORNAMESRESPONSE, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      detector_names:\n          detectors in the registry\n  '})
_sym_db.RegisterMessage(GetDetectorNamesResponse)
AddDetectorRequest = _reflection.GeneratedProtocolMessageType('AddDetectorRequest', (_message.Message,), {'DESCRIPTOR': _ADDDETECTORREQUEST, '__module__': 'proto.api.service.vision.v1.vision_pb2'})
_sym_db.RegisterMessage(AddDetectorRequest)
AddDetectorResponse = _reflection.GeneratedProtocolMessageType('AddDetectorResponse', (_message.Message,), {'DESCRIPTOR': _ADDDETECTORRESPONSE, '__module__': 'proto.api.service.vision.v1.vision_pb2'})
_sym_db.RegisterMessage(AddDetectorResponse)
GetDetectionsRequest = _reflection.GeneratedProtocolMessageType('GetDetectionsRequest', (_message.Message,), {'DESCRIPTOR': _GETDETECTIONSREQUEST, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      camera_name:\n          name of camera source to use as input\n      detector_name:\n          name of the registered detector to use\n  '})
_sym_db.RegisterMessage(GetDetectionsRequest)
GetDetectionsResponse = _reflection.GeneratedProtocolMessageType('GetDetectionsResponse', (_message.Message,), {'DESCRIPTOR': _GETDETECTIONSRESPONSE, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      detections:\n          the bounding boxes and labels\n  '})
_sym_db.RegisterMessage(GetDetectionsResponse)
Detection = _reflection.GeneratedProtocolMessageType('Detection', (_message.Message,), {'DESCRIPTOR': _DETECTION, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      x_min:\n          the four corners of the box\n      confidence:\n          the confidence of the detection\n      class_name:\n          label associated with the detected object\n  '})
_sym_db.RegisterMessage(Detection)
GetSegmenterNamesRequest = _reflection.GeneratedProtocolMessageType('GetSegmenterNamesRequest', (_message.Message,), {'DESCRIPTOR': _GETSEGMENTERNAMESREQUEST, '__module__': 'proto.api.service.vision.v1.vision_pb2'})
_sym_db.RegisterMessage(GetSegmenterNamesRequest)
GetSegmenterNamesResponse = _reflection.GeneratedProtocolMessageType('GetSegmenterNamesResponse', (_message.Message,), {'DESCRIPTOR': _GETSEGMENTERNAMESRESPONSE, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      segmenter_names:\n          segmenters in the registry\n  '})
_sym_db.RegisterMessage(GetSegmenterNamesResponse)
GetSegmenterParametersRequest = _reflection.GeneratedProtocolMessageType('GetSegmenterParametersRequest', (_message.Message,), {'DESCRIPTOR': _GETSEGMENTERPARAMETERSREQUEST, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      segmenter_name:\n          Name of the segmentation algo\n  '})
_sym_db.RegisterMessage(GetSegmenterParametersRequest)
TypedParameter = _reflection.GeneratedProtocolMessageType('TypedParameter', (_message.Message,), {'DESCRIPTOR': _TYPEDPARAMETER, '__module__': 'proto.api.service.vision.v1.vision_pb2'})
_sym_db.RegisterMessage(TypedParameter)
GetSegmenterParametersResponse = _reflection.GeneratedProtocolMessageType('GetSegmenterParametersResponse', (_message.Message,), {'DESCRIPTOR': _GETSEGMENTERPARAMETERSRESPONSE, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      segmenter_parameters:\n          parameter names of the segmenter in the request\n  '})
_sym_db.RegisterMessage(GetSegmenterParametersResponse)
GetObjectPointCloudsRequest = _reflection.GeneratedProtocolMessageType('GetObjectPointCloudsRequest', (_message.Message,), {'DESCRIPTOR': _GETOBJECTPOINTCLOUDSREQUEST, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      camera_name:\n          Name of a camera\n      segmenter_name:\n          Name of the segmentation algorithm\n      mime_type:\n          Requested MIME type of response\n      parameters:\n          parameters for the chosen segmenter\n  '})
_sym_db.RegisterMessage(GetObjectPointCloudsRequest)
GetObjectPointCloudsResponse = _reflection.GeneratedProtocolMessageType('GetObjectPointCloudsResponse', (_message.Message,), {'DESCRIPTOR': _GETOBJECTPOINTCLOUDSRESPONSE, '__module__': 'proto.api.service.vision.v1.vision_pb2', '__doc__': 'Attributes:\n      mime_type:\n          Actual MIME type of response\n      objects:\n          List of objects in the scene\n  '})
_sym_db.RegisterMessage(GetObjectPointCloudsResponse)
_VISIONSERVICE = DESCRIPTOR.services_by_name['VisionService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n(com.viam.rdk.proto.api.service.vision.v1Z+go.viam.com/rdk/proto/api/service/vision/v1'
    _VISIONSERVICE.methods_by_name['GetDetectorNames']._options = None
    _VISIONSERVICE.methods_by_name['GetDetectorNames']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/service/vision/detector_names'
    _VISIONSERVICE.methods_by_name['AddDetector']._options = None
    _VISIONSERVICE.methods_by_name['AddDetector']._serialized_options = b'\x82\xd3\xe4\x93\x02*"(/viam/api/v1/service/vision/add_detector'
    _VISIONSERVICE.methods_by_name['GetDetections']._options = None
    _VISIONSERVICE.methods_by_name['GetDetections']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/viam/api/v1/service/vision/detections'
    _VISIONSERVICE.methods_by_name['GetSegmenterNames']._options = None
    _VISIONSERVICE.methods_by_name['GetSegmenterNames']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/vision/segmenter_names'
    _VISIONSERVICE.methods_by_name['GetSegmenterParameters']._options = None
    _VISIONSERVICE.methods_by_name['GetSegmenterParameters']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/vision/segmenter_parameters'
    _VISIONSERVICE.methods_by_name['GetObjectPointClouds']._options = None
    _VISIONSERVICE.methods_by_name['GetObjectPointClouds']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/service/vision/object_point_clouds'
    _GETDETECTORNAMESREQUEST._serialized_start = 167
    _GETDETECTORNAMESREQUEST._serialized_end = 192
    _GETDETECTORNAMESRESPONSE._serialized_start = 194
    _GETDETECTORNAMESRESPONSE._serialized_end = 259
    _ADDDETECTORREQUEST._serialized_start = 262
    _ADDDETECTORREQUEST._serialized_end = 441
    _ADDDETECTORRESPONSE._serialized_start = 443
    _ADDDETECTORRESPONSE._serialized_end = 464
    _GETDETECTIONSREQUEST._serialized_start = 466
    _GETDETECTIONSREQUEST._serialized_end = 558
    _GETDETECTIONSRESPONSE._serialized_start = 560
    _GETDETECTIONSRESPONSE._serialized_end = 655
    _DETECTION._serialized_start = 658
    _DETECTION._serialized_end = 816
    _GETSEGMENTERNAMESREQUEST._serialized_start = 818
    _GETSEGMENTERNAMESREQUEST._serialized_end = 844
    _GETSEGMENTERNAMESRESPONSE._serialized_start = 846
    _GETSEGMENTERNAMESRESPONSE._serialized_end = 914
    _GETSEGMENTERPARAMETERSREQUEST._serialized_start = 916
    _GETSEGMENTERPARAMETERSREQUEST._serialized_end = 986
    _TYPEDPARAMETER._serialized_start = 988
    _TYPEDPARAMETER._serialized_end = 1044
    _GETSEGMENTERPARAMETERSRESPONSE._serialized_start = 1047
    _GETSEGMENTERPARAMETERSRESPONSE._serialized_end = 1175
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_start = 1178
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_end = 1365
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_start = 1367
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_end = 1491
    _VISIONSERVICE._serialized_start = 1494
    _VISIONSERVICE._serialized_end = 2616