from pyo3_test.pyo3_test import *
from pyo3_test.pyo3_test import __all__, __doc__

from .additional_class import PythonClass

__all__ = __all__ + ["PythonClass"]

print(__all__)
