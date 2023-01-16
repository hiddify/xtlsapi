from .add_client import AddClient
from .remove_client import RemoveClient


class HandlerAPIService(AddClient, RemoveClient):
    pass
