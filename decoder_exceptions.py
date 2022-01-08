class DecoderError(Exception):
    pass

class NoSeparatorError(DecoderError):
    """
    Raised when the separator is not found.
    """
    def __init__(self, message="Error: No separator found."):
        self.message = message
        super().__init__(self.message)

class EmptyWordListError(DecoderError):
    """
    Raised when the passed word list is empty.
    """
    def __init__(self, message="Error: Word list is empty."):
        self.message = message
        super().__init__(self.message)

class NoMatchWordFoundError(DecoderError):
    """
    Raised when no match found for an encoded word in word list.
    """
    def __init__(self, message="Error: No match found for encoded word in word list."):
        self.message = message
        super().__init__(self.message)