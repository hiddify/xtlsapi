import grpc
from xtlsapi.singbox_api import stats_pb2
from .._base import BaseService


class GetClientUploadTraffic(BaseService):
    def get_client_upload_traffic(self, email, reset=False):
        try:
            return self.stats_stub.GetStats(
                stats_pb2.GetStatsRequest(
                    name=f"user>>>{email}>>>traffic>>>uplink", reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            return None
