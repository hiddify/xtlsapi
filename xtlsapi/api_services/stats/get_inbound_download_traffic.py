import grpc
from vump_grpc_client.v2ray_api.app.stats.command import command_pb2
from .._base import BaseService


class GetInboundDownloadTraffic(BaseService):
    def get_inbound_download_traffic(self, tag, reset=False):
        try:
            return self.stats_stub.GetStats(
                command_pb2.GetStatsRequest(
                    name=f"inbound>>>{tag}>>>traffic>>>downlink", reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            return 0
