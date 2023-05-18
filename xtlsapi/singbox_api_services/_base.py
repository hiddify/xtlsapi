from xtlsapi.singbox_api import stats_pb2_grpc



class BaseService:
    def __init__(self):
        self.stats_stub = stats_pb2_grpc.StatsServiceStub(self._channel)
