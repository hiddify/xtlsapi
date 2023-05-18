import grpc
from xtlsapi.singbox_api import stats_pb2

from .._base import BaseService


class StatsQuery(BaseService):
    def stats_query(self, pattern):
        try:
            return self.stats_stub.QueryStats(
                stats_pb2.QueryStatsRequest(
                    pattern=pattern
                )
            ).stat
        except grpc.RpcError:
            raise
            return None
