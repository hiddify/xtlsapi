import grpc
from xtlsapi.singbox_api import stats_pb2
from .._base import BaseService


class GetInboundDownloadTraffic(BaseService):
    def get_inbound_download_traffic(self, tag, reset=False):
        try:
            return self.stats_stub.GetStats(
                stats_pb2.GetStatsRequest(
                    name=f"inbound>>>{tag}>>>traffic>>>downlink", reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            # raise
            return None
