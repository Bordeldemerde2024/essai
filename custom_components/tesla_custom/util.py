"""Utilities for tesla."""

try:
    # Home Assistant 2023.4.x+
    from homeassistant.util.ssl import get_default_context

    SSL_CONTEXT = get_default_context()
except ImportError:
    from homeassistant.util.ssl import client_context

    SSL_CONTEXT = client_context()


def safeget(dct, *keys, default=None):
    """Get a recursuive object from a dict."""
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return default
        except TypeError:
            return default
    return dct
