import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class MetadataServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Resources(self, stream: 'grpclib.server.Stream[proto.api.service.metadata.v1.metadata_pb2.ResourcesRequest, proto.api.service.metadata.v1.metadata_pb2.ResourcesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.metadata.v1.MetadataService/Resources': grpclib.const.Handler(self.Resources, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.metadata.v1.metadata_pb2.ResourcesRequest, proto.api.service.metadata.v1.metadata_pb2.ResourcesResponse)}

class MetadataServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Resources = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.metadata.v1.MetadataService/Resources', proto.api.service.metadata.v1.metadata_pb2.ResourcesRequest, proto.api.service.metadata.v1.metadata_pb2.ResourcesResponse)