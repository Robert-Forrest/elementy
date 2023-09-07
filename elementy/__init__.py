"""elementy

An interface to data on elements of the periodic table.
"""


from .element import Element
from .periodictable import PeriodicTable

periodic_table = PeriodicTable()

__all__ = ["PeriodicTable", "Element", "periodic_table"]
