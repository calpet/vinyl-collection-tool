"""Custom logger for the LPShuffler application."""

import logging

class Singleton(type):
    """
    A metaclass for creating singleton classes.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    """A custom logger wrapper around Python's logging module."""

    def __init__(self, name: str = "LPShuffler"):
        """
        Initialize the custom logger.
        
        Args:
            name: The name of the logger
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Configure console handler if not already configured
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log an info level message."""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log a warning level message."""
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Log an error level message."""
        self.logger.error(message)

    def debug(self, message: str) -> None:
        """Log a debug level message."""
        self.logger.debug(message)