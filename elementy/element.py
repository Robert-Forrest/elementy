from dataclasses import dataclass, field
from typing import Optional, Union

import numpy as np


@dataclass(frozen=True)
class Element:
    """Dataclass representing a chemical element.

    :group: elements

    Attributes
    ----------

    name:
        Name of the element.
    electrons
        Number of electrons in non-ionized state.
    protons
        Number of protons.
    neutrons
        Number of neutrons in most abundant isotope.
    valence_electrons
        Number of electrons in the outer shell.
    group
        Index referring to one of the 18 periodic table columns.
    period
        Index referring to one of the 7 periodic table rows.
    block
        Label referring to membership of group of elements with
        the same valence electron orbitals.
    series
        Label referring to membership of group of elements with
        similar properties.
    orbitals
        List of electrons and the orbitals they occupy.
    atomic_number
        Index of element in periodic table when reading
        left to right. Equal to proton number.

    """

    name: str
    symbol: str
    protons: int
    electrons: int
    neutrons: int
    valence_electrons: int
    group: int
    period: int
    block: str
    series: str
    orbitals: list
    atomic_number: int = field(init=False)
    periodic_number: Optional[int] = field(default=None)
    radius_empirical: Optional[float] = field(
        default=None, metadata={"unit": "angstrom"}
    )
    radius_calculated: Optional[float] = field(
        default=None, metadata={"unit": "angstrom"}
    )
    radius_vanDerWaals: Optional[float] = field(
        default=None, metadata={"unit": "angstrom"}
    )
    radius_covalent: Optional[float] = field(
        default=None, metadata={"unit": "angstrom"}
    )
    radius_metallic: Optional[float] = field(
        default=None, metadata={"unit": "angstrom"}
    )
    radius_USE: Optional[float] = field(
        default=None, metadata={"unit": "angstrom"}
    )
    radius: float = field(init=False, metadata={"unit": "angstrom"})
    volume_miedema: Optional[float] = field(default=None)
    mass: Optional[float] = field(
        default=None, metadata={"unit": "atomic mass units"}
    )
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
        default=None, metadata={"unit": "electron-volts"}
    )
    chemical_hardness: Optional[float] = field(default=None)
    chemical_potential: Optional[float] = field(default=None)
    melting_temperature: Optional[float] = field(
        default=None, metadata={"unit": "kelvin"}
    )
    boiling_temperature: Optional[float] = field(
        default=None, metadata={"unit": "kelvin"}
    )
    fusion_enthalpy: Optional[float] = field(default=None)
    vaporisation_enthalpy: Optional[float] = field(default=None)
    molar_heat_capacity: Optional[float] = field(default=None)
    molar_volume: float = field(init=False)
    structure: Optional[str] = field(default=None)
    thermal_conductivity: Optional[float] = field(default=None)
    thermal_expansion: Optional[float] = field(default=None)
    density: Optional[float] = field(
        default=None, metadata={"unit": "grams per cubic centimetre"}
    )
    cohesive_energy: Optional[float] = field(default=None)
    debye_temperature: Optional[float] = field(
        default=None, metadata={"unit": "kelvin"}
    )
    price: Optional[float] = field(default=None, metadata={"unit": "dollars"})

    def __post_init__(self):
        """Set additional attributes that depend on attributes set during
        __init__

        :group: element.util
        """

        super().__setattr__("atomic_number", self.protons)
        super().__setattr__("radius", get_radius(self))
        super().__setattr__("atomic_volume", calculate_atomic_volume(self))
        super().__setattr__("molar_volume", self.mass / self.density)
        super().__setattr__(
            "electronegativity_mulliken",
            calculate_mulliken_electronegativity(self),
        )

    def __getitem__(self, item):
        return getattr(self, item)


def calculate_atomic_volume(self) -> float:
    """Calculate the atomic volume from the atomic radius

    :group: element.util
    """
    if self.radius is not None:
        volume = (4.0 / 3.0) * np.pi * self.radius**3
        return volume


def get_radius(element: Element) -> Optional[float]:
    """Gets one of the radius data entries to represent the element

    :group: element.util
    """
    if element.radius_USE is not None:
        return element.radius_USE
    if element.radius_empirical is not None:
        return element.radius_empirical
    if element.radius_metallic is not None:
        return element.radius_metallic
    if element.radius_covalent is not None:
        return element.radius_covalent


def calculate_mulliken_electronegativity(
    element: Element,
) -> Optional[float]:
    """Calculate the Mulliken electronegativity from the electron affinity and
    ionisation energy

    :group: element.util
    """
    if (
        element.electron_affinity is not None
        and element.ionisation_energies is not None
    ):
        mulliken_electronegativity = 0.5 * np.abs(
            element.electron_affinity
            + (element.ionisation_energies[0] / 96.485)
        )
        return mulliken_electronegativity
