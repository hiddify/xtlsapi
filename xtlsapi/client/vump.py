from grpc import insecure_channel as grpc_insecure_channel

from vump_grpc_client.api_services import APIService


class VUMPClient(APIService):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._channel = grpc_insecure_channel(f'{host}:{port}')
        super().__init__()
