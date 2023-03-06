from grpc._channel import _InactiveRpcError

from xtlsapi.xray_api.common.protocol import user_pb2
from xtlsapi.xray_api.app.proxyman.command import command_pb2
from xtlsapi.ext import utils
from .._base import BaseService
from xtlsapi import exceptions


class AddClient(BaseService):
    def add_client(self, inbound_tag, user_id_or_password, email,protocol='vless', level=None, alter_id=None,flow=None,cipher=None):
        try:
            if protocol=='vmess':
                from xtlsapi.xray_api.proxy.vmess import account_pb2
                account=account_pb2.Account(id=user_id_or_password, alter_id=alter_id)
            elif protocol=='vless':
                from xtlsapi.xray_api.proxy.vless import account_pb2
                account=account_pb2.Account(id=user_id_or_password,flow=flow,encryption="none")
            elif protocol=='trojan':
                from xtlsapi.xray_api.proxy.trojan import config_pb2
                account=config_pb2.Account(password=user_id_or_password,flow=flow)
            elif protocol=='shadowsocks':
                from xtlsapi.xray_api.proxy.shadowsocks import config_pb2
                cipher_map={'aes_128_gcm':config_pb2.CipherType.AES_128_GCM,
                            'aes_256_gcm':config_pb2.CipherType.AES_256_GCM,
                            'chacha20_poly1305':config_pb2.CipherType.CHACHA20_POLY1305,
                            'xchacha20_poly1305':config_pb2.CipherType.XCHACHA20_POLY1305,
                            None:config_pb2.CipherType.NONE                            
                            }
                account=config_pb2.Account(password=user_id_or_password,cipher_type=cipher_map.get(cipher,cipher_map[None]))
            # elif protocol=='shadowsocks_2022':
                # from xtlsapi.xray_api.proxy.shadowsocks import config_pb2
                # cipher_map={'aes_128_gcm':config_pb2.CipherType.AES_128_GCM,
                #             'aes_256_gcm':config_pb2.CipherType.AES_256_GCM,
                #             'chacha20_poly1305':config_pb2.CipherType.CHACHA20_POLY1305,
                #             'xchacha20_poly1305':config_pb2.CipherType.XCHACHA20_POLY1305,
                #             None:config_pb2.CipherType.NONE                            
                #             }
                # account=config_pb2.Account(password=user_id_or_password,cipher_type=cipher_map.get(cipher,cipher_map[None])
                # raise Exception("not implemented ")
            else:
                raise Exception("not implemented "+protocol )
            
            self.handler_stub.AlterInbound(
                command_pb2.AlterInboundRequest(
                    tag=inbound_tag,
                    operation=utils.to_typed_message(
                        command_pb2.AddUserOperation(
                            user=user_pb2.User(
                                email=email,
                                level=level,
                                account=utils.to_typed_message(account),
                            )
                        )
                    ),
                )
            )
            return user_id_or_password
        except _InactiveRpcError as e:
            details = e.details()
            if details.endswith(f"User {email} already exists."):
                raise exceptions.EmailAlreadyExists(details, email)
            elif details.endswith(f"handler not found: {inbound_tag}"):
                raise exceptions.InboundNotFound(details, inbound_tag)
            else:
                raise exceptions.XRayException(details)
