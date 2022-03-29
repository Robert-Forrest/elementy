import pandas as pd

import elementy.elements as elements


class PeriodicTable():
    def __init__(self):
        self.elements = elements.get_elements()

        self.dataframe = pd.DataFrame(
            [element.__dict__ for element in self.elements])

    def get_data(self, feature_names=None, elements=None):

        if elements is not None:
            selected_data = self.dataframe.loc[self.dataframe['symbol'].isin(
                elements)]
        else:
            selected_data = self.dataframe.copy()

        if feature_names is not None:
            if not isinstance(feature_names, list):
                feature_names = [feature_names]
            selected_data = selected_data[["symbol", *feature_names]]

        return selected_data
