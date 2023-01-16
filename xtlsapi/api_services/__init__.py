from .stats import StatsAPIService
from .handler import HandlerAPIService
from .logger import LoggerAPIService


class APIService(StatsAPIService, HandlerAPIService, LoggerAPIService):
    pass
