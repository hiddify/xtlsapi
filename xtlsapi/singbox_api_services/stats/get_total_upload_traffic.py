import grpc
from xtlsapi.singbox_api import stats_pb2
from .._base import BaseService


class GetTotalUploadTraffic(BaseService):
    def get_total_upload_traffic(self, reset=False):
        raise Exception('Not Implemented')
        try:
            return self.stats_stub.GetStats(
                stats_pb2.GetStatsRequest(
                    name=f"outbound>>>direct>>>traffic>>>uplink", reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            return None
