import pandas as pd

import elementy.elements as elements


class PeriodicTable():
    def __init__(self):
        self.elements = elements.get_elements()

        self.dataframe = pd.DataFrame(
            [element.__dict__ for element in self.elements])

    def get_data(self, feature_name, elements=None):

        if elements is not None:
            selected_data = self.dataframe.loc[self.dataframe['symbol'].isin(
                elements)][["symbol", feature_name]]
        else:
            selected_data = self.dataframe[["symbol", feature_name]]

        return selected_data
