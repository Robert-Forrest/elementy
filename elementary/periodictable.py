import pandas as pd

from .element import Element

class PeriodicTable():
    def __init__(self):
        self.elements = []

        for Z in range(1,119):
            self.elements.append(Element(Z))

        self.data = pd.DataFrame([element.__dict__ for element in self.elements ])


