import elementy.mulliken as mulliken


class Element():

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        self.electronegativity_mulliken = \
            mulliken.calculate_mulliken_electronegativity(self)
