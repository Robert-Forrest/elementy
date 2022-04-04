import elementy.mulliken as mulliken
import elementy.radii as radii


class Element():

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        self.electronegativity_mulliken = \
            mulliken.calculate_mulliken_electronegativity(self)

        self.radius = radii.calculate_radius(self)
        self.atomic_volume = radii.calculate_atomic_volume(self)

        self.molar_volume = self.mass / self.density
