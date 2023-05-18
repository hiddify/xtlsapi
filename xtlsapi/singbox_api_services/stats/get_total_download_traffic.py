import grpc
from xtlsapi.singbox_api import stats_pb2
from .._base import BaseService


class GetTotalDownloadTraffic(BaseService):
    def get_total_download_traffic(self, reset=False):
        raise Exception('Not Implemented')
        try:
            return self.stats_stub.GetStats(
                stats_pb2.GetStatsRequest(
                    name=f"outbound>>>statout>>>traffic>>>downlink", reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            # raise
            return None
