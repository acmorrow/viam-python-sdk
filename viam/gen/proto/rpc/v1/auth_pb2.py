"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17proto/rpc/v1/auth.proto\x12\x0cproto.rpc.v1\x1a\x1cgoogle/api/annotations.proto";\n\x0bCredentials\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x18\n\x07payload\x18\x02 \x01(\tR\x07payload"j\n\x13AuthenticateRequest\x12\x16\n\x06entity\x18\x01 \x01(\tR\x06entity\x12;\n\x0bcredentials\x18\x02 \x01(\x0b2\x19.proto.rpc.v1.CredentialsR\x0bcredentials"9\n\x14AuthenticateResponse\x12!\n\x0caccess_token\x18\x01 \x01(\tR\x0baccessToken"/\n\x15AuthenticateToRequest\x12\x16\n\x06entity\x18\x01 \x01(\tR\x06entity";\n\x16AuthenticateToResponse\x12!\n\x0caccess_token\x18\x01 \x01(\tR\x0baccessToken2\x82\x01\n\x0bAuthService\x12s\n\x0cAuthenticate\x12!.proto.rpc.v1.AuthenticateRequest\x1a".proto.rpc.v1.AuthenticateResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x14/rpc/v1/authenticate2\x93\x01\n\x13ExternalAuthService\x12|\n\x0eAuthenticateTo\x12#.proto.rpc.v1.AuthenticateToRequest\x1a$.proto.rpc.v1.AuthenticateToResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x17/rpc/v1/authenticate_toB Z\x1ego.viam.com/utils/proto/rpc/v1b\x06proto3')
_CREDENTIALS = DESCRIPTOR.message_types_by_name['Credentials']
_AUTHENTICATEREQUEST = DESCRIPTOR.message_types_by_name['AuthenticateRequest']
_AUTHENTICATERESPONSE = DESCRIPTOR.message_types_by_name['AuthenticateResponse']
_AUTHENTICATETOREQUEST = DESCRIPTOR.message_types_by_name['AuthenticateToRequest']
_AUTHENTICATETORESPONSE = DESCRIPTOR.message_types_by_name['AuthenticateToResponse']
Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {'DESCRIPTOR': _CREDENTIALS, '__module__': 'proto.rpc.v1.auth_pb2', '__doc__': 'Attributes:\n      type:\n          type is the type of credentials being used.\n      payload:\n          payload is an opaque string used that are of the given type\n          above.\n  '})
_sym_db.RegisterMessage(Credentials)
AuthenticateRequest = _reflection.GeneratedProtocolMessageType('AuthenticateRequest', (_message.Message,), {'DESCRIPTOR': _AUTHENTICATEREQUEST, '__module__': 'proto.rpc.v1.auth_pb2', '__doc__': 'An AuthenticateRequest contains the credentials used to authenticate.'})
_sym_db.RegisterMessage(AuthenticateRequest)
AuthenticateResponse = _reflection.GeneratedProtocolMessageType('AuthenticateResponse', (_message.Message,), {'DESCRIPTOR': _AUTHENTICATERESPONSE, '__module__': 'proto.rpc.v1.auth_pb2', '__doc__': 'An AuthenticateResponse is returned after successful authentication.\n  \n  Attributes:\n      access_token:\n          access_token is a JWT where only the expiration should be\n          deemed important.  Future(erd): maybe a refresh_token\n  '})
_sym_db.RegisterMessage(AuthenticateResponse)
AuthenticateToRequest = _reflection.GeneratedProtocolMessageType('AuthenticateToRequest', (_message.Message,), {'DESCRIPTOR': _AUTHENTICATETOREQUEST, '__module__': 'proto.rpc.v1.auth_pb2', '__doc__': 'An AuthenticateToRequest contains the entity to authenticate to.'})
_sym_db.RegisterMessage(AuthenticateToRequest)
AuthenticateToResponse = _reflection.GeneratedProtocolMessageType('AuthenticateToResponse', (_message.Message,), {'DESCRIPTOR': _AUTHENTICATETORESPONSE, '__module__': 'proto.rpc.v1.auth_pb2', '__doc__': 'An AuthenticateResponse is returned after successful authentication.\n  \n  Attributes:\n      access_token:\n          access_token is a JWT where only the expiration should be\n          deemed important.  Future(erd): maybe a refresh_token\n  '})
_sym_db.RegisterMessage(AuthenticateToResponse)
_AUTHSERVICE = DESCRIPTOR.services_by_name['AuthService']
_EXTERNALAUTHSERVICE = DESCRIPTOR.services_by_name['ExternalAuthService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1ego.viam.com/utils/proto/rpc/v1'
    _AUTHSERVICE.methods_by_name['Authenticate']._options = None
    _AUTHSERVICE.methods_by_name['Authenticate']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x14/rpc/v1/authenticate'
    _EXTERNALAUTHSERVICE.methods_by_name['AuthenticateTo']._options = None
    _EXTERNALAUTHSERVICE.methods_by_name['AuthenticateTo']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x17/rpc/v1/authenticate_to'
    _CREDENTIALS._serialized_start = 71
    _CREDENTIALS._serialized_end = 130
    _AUTHENTICATEREQUEST._serialized_start = 132
    _AUTHENTICATEREQUEST._serialized_end = 238
    _AUTHENTICATERESPONSE._serialized_start = 240
    _AUTHENTICATERESPONSE._serialized_end = 297
    _AUTHENTICATETOREQUEST._serialized_start = 299
    _AUTHENTICATETOREQUEST._serialized_end = 346
    _AUTHENTICATETORESPONSE._serialized_start = 348
    _AUTHENTICATETORESPONSE._serialized_end = 407
    _AUTHSERVICE._serialized_start = 410
    _AUTHSERVICE._serialized_end = 540
    _EXTERNALAUTHSERVICE._serialized_start = 543
    _EXTERNALAUTHSERVICE._serialized_end = 690