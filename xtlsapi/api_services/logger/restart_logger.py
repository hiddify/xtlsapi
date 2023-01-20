from grpc._channel import _InactiveRpcError

from xtlsapi import exceptions
from xtlsapi.xray_api.app.log.command import config_pb2

from .._base import BaseService


class RestartLogger(BaseService):
    def restart_logger(self):
        try:
            self.logger_stub.RestartLogger(
                config_pb2.RestartLoggerRequest()
            )
        except _InactiveRpcError as e:
            details = e.details()
            raise exceptions.XRayException(details)
