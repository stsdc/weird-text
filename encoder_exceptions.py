"""This module contains the encoder exceptions."""


class EncoderError(Exception):
    """Base class for encoder exceptions."""


class NothingEncodeError(EncoderError):
    """
    Raised when passed data is empty. Therefor, there is nothing to encode.
    """

    def __init__(self, message="Error: Nothing to encode."):
        self.message = message
        super().__init__(self.message)
