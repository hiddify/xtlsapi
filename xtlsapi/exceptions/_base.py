class V2RayException(Exception):
    def __init__(self, details):
        self.details = details
