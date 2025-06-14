class CacheException(Exception):
    """Raised when there is a cache-related error."""
    def __init__(self, message: str = "Cache error occurred"):
        self.message = message
        super().__init__(self.message)


class ConflictException(Exception):
    """Raised when there is a conflict (e.g., duplicate data)."""
    def __init__(self, message: str = "Resource already exists"):
        self.message = message
        super().__init__(self.message)


class NotFoundException(Exception):
    """Raised when a resource is not found."""
    def __init__(self, message: str = "Resource not found"):
        self.message = message
        super().__init__(self.message)


class UnauthorizedException(Exception):
    """Raised when an action is unauthorized."""
    def __init__(self, message: str = "Unauthorized"):
        self.message = message
        super().__init__(self.message)

class InvalidValueException(Exception):
    """Raised when an invalid value is provided."""
    def __init__(self, message: str = "Invalid value provided"):
        self.message = message
        super().__init__(self.message)