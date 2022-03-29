import pandas as pd

import elementy.elements as elements


class PeriodicTable():
    def __init__(self):
        self.elements = elements.get_elements()

        self.dataframe = pd.DataFrame(
            [element.__dict__ for element in self.elements])
