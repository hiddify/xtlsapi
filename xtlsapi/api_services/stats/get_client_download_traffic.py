import grpc
from xtlsapi.xray_api.app.stats.command import command_pb2

from .._base import BaseService


class GetClientDownloadTraffic(BaseService):
    def get_client_download_traffic(self, email, reset=False):
        try:
            return self.stats_stub.GetStats(
                command_pb2.GetStatsRequest(
                    name=f"user>>>{email}>>>traffic>>>downlink", reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            # raise
            return None
