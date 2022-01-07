class DecoderError(Exception):
    pass

class NoSeparatorError(DecoderError):
    """
    Raised when the separator is not found.
    """
    def __init__(self, message="Error: No separator found."):
        self.message = message
        super().__init__(self.message)