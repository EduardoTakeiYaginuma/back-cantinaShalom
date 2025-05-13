class ResponseEntity(list):
    def __init__(self, status_code: int, message: str, data=None):
        super().__init__(data if data else [])
        self.status_code = status_code
        self.message = message

    def __setitem__(self, index, value):
        super().__setitem__(index, value)

    def append(self, value):
        super().append(value)