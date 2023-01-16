from grpc._channel import _InactiveRpcError

from vump_grpc_client import utils, exceptions
from vump_grpc_client.v2ray_api.app.proxyman.command import command_pb2

from .._base import BaseService


class RemoveClient(BaseService):
    def remove_client(self, inbound_tag, email):
        try:
            self.handler_stub.AlterInbound(
                command_pb2.AlterInboundRequest(
                    tag=inbound_tag,
                    operation=utils.to_typed_message(
                        command_pb2.RemoveUserOperation(email=email)
                    ),
                )
            )
        except _InactiveRpcError as e:
            details = e.details()
            if details.endswith(f"User {email} not found."):
                raise exceptions.EmailNotFound(details, email)
            elif details.endswith(f"handler not found: {inbound_tag}"):
                raise exceptions.InboundNotFound(details, inbound_tag)
            else:
                raise exceptions.V2RayException(details)
