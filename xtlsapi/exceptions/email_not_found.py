from ._base import XRayException


class EmailNotFound(XRayException):
    def __init__(self, details, email):
        self.email = email
        super().__init__(details)
