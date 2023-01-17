from ._base import V2RayException


class InboundNotFound(V2RayException):
    def __init__(self, details, inbound_tag):
        self.inbound_tag = inbound_tag
        super().__init__(details)
