
class LengthNotInRange(Exception):
    """Exception raised when the given length did not fit the limits."""

    def __init__(self, length: int):
        super().__init__(f'The length is not in range (given {length}, specify between 4, 50).')
