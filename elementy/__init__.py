from .periodictable import PeriodicTable

PERIODIC_TABLE = PeriodicTable()
elements = PERIODIC_TABLE.elements
dataframe = PERIODIC_TABLE.dataframe


def get_data(feature_name, elements=None):

    if elements is not None:
        selected_data = dataframe.loc[dataframe['symbol'].isin(elements)][[
            "symbol", feature_name]]
    else:
        selected_data = dataframe[["symbol", feature_name]]

    return selected_data
