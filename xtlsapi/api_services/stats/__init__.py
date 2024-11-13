from .get_client_upload_traffic import GetClientUploadTraffic
from .get_client_download_traffic import GetClientDownloadTraffic
from .get_inbound_upload_traffic import GetInboundUploadTraffic
from .get_inbound_download_traffic import GetInboundDownloadTraffic
from .get_total_upload_traffic import GetTotalUploadTraffic
from .get_total_download_traffic import GetTotalDownloadTraffic
from .get_statsquery import StatsQuery
from .get_statsonline import StatsOnline

class StatsAPIService(
    GetClientUploadTraffic,
    GetClientDownloadTraffic,
    GetInboundUploadTraffic,
    GetInboundDownloadTraffic,
    GetTotalUploadTraffic,
    GetTotalDownloadTraffic,
    StatsQuery,
    StatsOnline
):
    pass
