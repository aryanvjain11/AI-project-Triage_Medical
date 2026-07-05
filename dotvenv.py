"""Compatibility wrapper for loading environment variables.

This module provides a small shim so the app can work even when the
`python-dotenv` package is not installed.
"""

try:
    from dotenv import load_dotenv as _load_dotenv
except Exception:  # pragma: no cover - fallback when dependency is unavailable
    def _load_dotenv(*args, **kwargs):
        return False


def load_dotenv(*args, **kwargs):
    return _load_dotenv(*args, **kwargs)


__all__ = ["load_dotenv"]
