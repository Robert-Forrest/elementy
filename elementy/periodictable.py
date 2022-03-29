import pandas as pd

import elementy.elements as elements


class PeriodicTable():
    def __init__(self):
        self.elements = elements.get_elements()

        self.dataframe = pd.DataFrame(
            [element.__dict__ for element in self.elements])
        self.dataframe = self.dataframe.set_index(['symbol'])

        self.data = {}
        for element in self.elements:
            self.data[element.symbol] = element.__dict__

    def get_data(self, feature_names=None, elements=None):

        if elements is not None:
            selected_data = self.dataframe.loc[elements]
        else:
            selected_data = self.dataframe

        if feature_names is not None:
            if not isinstance(feature_names, list):
                feature_names = [feature_names]
            selected_data = selected_data[["symbol", *feature_names]]

        return selected_data
