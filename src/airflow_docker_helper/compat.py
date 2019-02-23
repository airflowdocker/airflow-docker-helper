try:
    import unittest.mock as mock
except ImportError:
    import mock

try:
    import builtins

    BUILTIN_NAME = "builtins"

except ImportError:
    import __builtin__

    BUILTIN_NAME = "__builtin__"
