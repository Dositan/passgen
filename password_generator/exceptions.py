class LengthNotInRange(Exception):    
    """Exception raised when the given length was too big."""

    def __init__(self, length, message='Length is not in (4, 50) range.'):
        super().__init__(message)
        self.length = length
        self.message = message

    def __str__(self):
        return f'{self.message} ({self.length} given).'
