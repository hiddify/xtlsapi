from ._base import V2RayException


class EmailNotFound(V2RayException):
    def __init__(self, details, email):
        self.email = email
        super().__init__(details)
