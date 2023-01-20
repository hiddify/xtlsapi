from ._base import XRayException


class InboundNotFound(XRayException):
    def __init__(self, details, inbound_tag):
        self.inbound_tag = inbound_tag
        super().__init__(details)
