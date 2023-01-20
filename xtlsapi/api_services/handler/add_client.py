from grpc._channel import _InactiveRpcError
from xtlsapi.xray_api.proxy.vmess import account_pb2
from xtlsapi.xray_api.common.protocol import user_pb2
from xtlsapi.xray_api.app.proxyman.command import command_pb2
from xtlsapi.ext import utils
from .._base import BaseService
from xtlsapi import exceptions


class AddClient(BaseService):
    def add_client(self, inbound_tag, user_id, email, level=None, alter_id=None):
        try:
            self.handler_stub.AlterInbound(
                command_pb2.AlterInboundRequest(
                    tag=inbound_tag,
                    operation=utils.to_typed_message(
                        command_pb2.AddUserOperation(
                            user=user_pb2.User(
                                email=email,
                                level=level,
                                account=utils.to_typed_message(
                                    account_pb2.Account(id=user_id, alter_id=alter_id)
                                ),
                            )
                        )
                    ),
                )
            )
            return user_id
        except _InactiveRpcError as e:
            details = e.details()
            if details.endswith(f"User {email} already exists."):
                raise exceptions.EmailAlreadyExists(details, email)
            elif details.endswith(f"handler not found: {inbound_tag}"):
                raise exceptions.InboundNotFound(details, inbound_tag)
            else:
                raise exceptions.XRayException(details)
