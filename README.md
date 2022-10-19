# Elementy

![Tests](https://github.com/Robert-Forrest/elementy/actions/workflows/tests.yml/badge.svg)

This package provides an interface to a variety of different data on
elements of the periodic table.

## Installation

The metallurgy package can be installed from
[pypi](https://pypi.org/project/elementy/) using pip:

``pip install elementy``

## Usage

Access to elemental data is easily obtained by creating an instance of the
periodic table:

```python
from elementy import PeriodicTable

periodic_table = PeriodicTable()

>>> periodic_table.elements["Cu"]["mass"]
63.546

>>> periodic_table.elements["Cu"]["valence_electrons"]
11

>>> periodic_table.elements["Cu"]["melting_temperature"]
1357.77
```

### List of data types

The following attributes are found in the Element class. Note that some entries
are `None` due to lack of experimental data available. 

- Name
- Symbol
- Protons
- Electrons
- Neutrons
- Valence electrons
- Group
- Period
- Block
- Series
- Orbitals
- Atomic number
- Periodic number
- Radius
- Atomic volume
- Mass
- Valence
- Electron affinity
- Wigner Seitz electron density
- Chemical scale
- Mendeleev number
- Work function
- Electronegativity pauling
- Electronegativity allen
- Electronegativity miedema
- Electronegativity mulliken
- Ionisation energies
- Chemical hardness
- Chemical potential
- Melting temperature
- Boiling temperature
- Fusion enthalpy
- Vaporisation enthalpy
- Molar heat capacity
- Molar volume
- Structure
- Thermal conductivity
- Thermal expansion
- Density
- Cohesive energy
- Debye temperature
- Price-per-kilogramme

