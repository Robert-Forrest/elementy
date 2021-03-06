from dataclasses import dataclass, field
from typing import Dict

import elementy.elements as elements
from .element import Element


def make_periodic_table():
    periodic_table_elements = {}
    for element in elements.get_elements():
        periodic_table_elements[element.symbol] = element
    return periodic_table_elements


@dataclass
class PeriodicTable:
    elements: Dict[str, Element] = field(
        default_factory=make_periodic_table)
