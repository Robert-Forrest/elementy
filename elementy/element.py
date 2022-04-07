from dataclasses import dataclass, field
from typing import Optional, Union

import numpy as np


@dataclass()
class Element:
    name: str
    symbol: str
    atomic_number: int
    electrons: int
    protons: int
    neutrons: int
    valence_electrons: int
    group: int
    period: int
    block: str
    series: str
    orbitals: dict
    periodic_number: Optional[int] = field(default=None)
    radius_empirical: Optional[float] = field(
        default=None, metadata={'unit': 'angstrom'})
    radius_calculated: Optional[float] = field(
        default=None, metadata={'unit': 'angstrom'})
    radius_vanDerWaals: Optional[float] = field(
        default=None, metadata={'unit': 'angstrom'})
    radius_covalent: Optional[float] = field(
        default=None, metadata={'unit': 'angstrom'})
    radius_metallic: Optional[float] = field(
        default=None, metadata={'unit': 'angstrom'})
    radius_USE: Optional[float] = field(
        default=None, metadata={'unit': 'angstrom'})
    radius: float = field(init=False, metadata={'unit': 'angstrom'})
    atomic_volume: float = field(
        init=False, metadata={'unit': 'cubic angstrom'})
    volume_miedema: Optional[float] = field(default=None)
    mass: Optional[float] = field(default=None, metadata={
                                  'unit': 'atomic mass units'})
    valence: Optional[int] = field(default=None)
    electron_affinity: Optional[float] = field(default=None)
    wigner_seitz_electron_density: Optional[float] = field(default=None)
    chemical_scale: Optional[float] = field(default=None)
    mendeleev_universal_sequence: Optional[int] = field(default=None)
    mendeleev_pettifor: Optional[int] = field(default=None)
    mendeleev_modified: Optional[int] = field(default=None)
    work_function: Optional[float] = field(default=None)
    electronegativity_pauling: Optional[float] = field(default=None)
    electronegativity_allen: Optional[float] = field(default=None)
    electronegativity_miedema: Optional[float] = field(default=None)
    electronegativity_mulliken: float = field(init=False)
    miedema_R: Optional[float] = field(default=None)
    ionisation_energies: Optional[list] = field(
        default=None, metadata={'unit': 'electron-volts'})
    chemical_hardness: Optional[float] = field(default=None)
    chemical_potential: Optional[float] = field(default=None)
    melting_temperature: Optional[float] = field(
        default=None, metadata={'unit': 'kelvin'})
    boiling_temperature: Optional[float] = field(
        default=None, metadata={'unit': 'kelvin'})
    fusion_enthalpy: Optional[float] = field(default=None)
    vaporisation_enthalpy: Optional[float] = field(default=None)
    molar_heat_capacity: Optional[float] = field(default=None)
    molar_volume: float = field(init=False)
    structure: Optional[str] = field(default=None)
    thermal_conductivity: Optional[float] = field(default=None)
    thermal_expansion: Optional[float] = field(default=None)
    density: Optional[float] = field(
        default=None, metadata={'unit': 'grammes per cubic centimetre'})
    cohesive_energy: Optional[float] = field(default=None)
    debye_temperature: Optional[float] = field(
        default=None, metadata={'unit': 'kelvin'})
    price: Optional[float] = field(default=None, metadata={'unit': 'dollars'})

    def __post_init__(self):

        self.radius = calculate_radius(self)
        self.atomic_volume = calculate_atomic_volume(self)
        self.molar_volume = self.mass / self.density
        self.electronegativity_mulliken = calculate_mulliken_electronegativity(
            self)


def calculate_radius(element: Element) -> float | None:

    if element.radius_USE is not None:
        return element.radius_USE
    elif element.radius_empirical is not None:
        return element.radius_empirical
    elif element.radius_metallic is not None:
        return element.radius_metallic
    elif element.radius_covalent is not None:
        return element.radius_covalent


def calculate_atomic_volume(element: Element) -> Union[float, None]:
    if element.radius is not None:
        return (4. / 3.) * np.pi * element.radius**3


def calculate_mulliken_electronegativity(
        element: Element) -> Union[float, None]:

    if(element.electron_affinity is not None and
       element.ionisation_energies is not None):
        return 0.5 * np.abs(element.electron_affinity +
                            (element.ionisation_energies[0] / 96.485))
