from xtlsapi.xray_api.app.log.command import config_pb2_grpc as logger_pb2_grpc
from xtlsapi.xray_api.app.stats.command import command_pb2_grpc as stats_pb2_grpc
from xtlsapi.xray_api.app.proxyman.command import command_pb2_grpc as handler_pb2_grpc


class BaseService:
    def __init__(self):
        self.stats_stub = stats_pb2_grpc.StatsServiceStub(self._channel)
        self.logger_stub = logger_pb2_grpc.LoggerServiceStub(self._channel)
        self.handler_stub = handler_pb2_grpc.HandlerServiceStub(self._channel)
