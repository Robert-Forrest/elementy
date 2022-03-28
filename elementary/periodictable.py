import pandas as pd

import elementary.elements as elements


class PeriodicTable():
    def __init__(self):
        self.elements = elements.get_elements()

        self.data = pd.DataFrame(
            [element.__dict__ for element in self.elements])
