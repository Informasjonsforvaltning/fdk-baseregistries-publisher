"""Service layer module for fdk_baseregistries_publisher."""


class FetchFromServiceException(Exception):
    """Exception representing errors in communication with back-end service."""

    __slots__ = ("status", "message")

    def __init__(self, status: int, message: str) -> None:
        """Initialize the instance with given status and message."""
        self.status = status
        self.message = message
