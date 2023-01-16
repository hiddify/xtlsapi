from ._base import V2RayException


class EmailAlreadyExists(V2RayException):
    def __init__(self, details, email):
        self.email = email
        super().__init__(details)
