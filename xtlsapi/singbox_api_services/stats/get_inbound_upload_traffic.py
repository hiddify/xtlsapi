import grpc
from xtlsapi.singbox_api import stats_pb2
from .._base import BaseService


class GetInboundUploadTraffic(BaseService):
    def get_inbound_upload_traffic(self, tag, reset=False):
        try:
            return self.stats_stub.GetStats(
                stats_pb2.GetStatsRequest(
                    name=f"inbound>>>{tag}>>>traffic>>>uplink", reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            # raise
            return None
