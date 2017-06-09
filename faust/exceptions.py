"""Faust exceptions."""

__all__ = [
    'ImproperlyConfigured',
    'KeyDecodeError',
    'ValueDecodeError',
]


class FaustError(Exception):
    ...


class ImproperlyConfigured(FaustError):
    """The library is not configured/installed correctly."""


class KeyDecodeError(FaustError):
    """Error while decoding/deserializing message key."""


class ValueDecodeError(FaustError):
    """Error while decoding/deserialization message value."""
