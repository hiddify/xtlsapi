import grpc
from xtlsapi.xray_api.app.stats.command import command_pb2

from .._base import BaseService


class StatsOnline(BaseService):
    def stats_online(self, user,reset=False):
        try:
            return self.stats_stub.GetStatsOnline(
                command_pb2.GetStatsRequest(
                    name=f"user>>>{user}>>>online",
                    reset=reset
                )
            ).stat.value
        except grpc.RpcError:
            raise
            return None
