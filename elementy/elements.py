from elementy.element import Element

Hydrogen = Element(**{
    "name": "Hydrogen",
    "symbol": "H",
    "periodic_number": 89,
    "radius_empirical": 0.25,
    "radius_calculated": 0.53,
    "radius_vanDerWaals": 1.2,
    "radius_covalent": 0.31,
    "radius_USE": 0.727,
    "volume_miedema": 1.7,
    "mass": 1.008,
    "group": 1,
    "period": 1,
    "block": "s",
    "series": "non_metal",
    "orbitals": [
        {
            "orbital": "1s",
            "electrons": 1
        }
    ],
    "electrons": 1,
    "protons": 1,
    "neutrons": 0,
    "valence": 1,
    "valence_electrons": 1,
    "electron_affinity": 0.754195,
    "wigner_seitz_electron_density": 3.38,
    "chemical_scale": 2.366,
    "mendeleev_universal_sequence": 90,
    "mendeleev_pettifor": 100,
    "mendeleev_modified": 100,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 2.3,
    "electronegativity_miedema": 5.2,
    "ionisation_energies": [
        1312
    ],
    "chemical_hardness": 12.84,
    "chemical_potential": -7.18,
    "melting_temperature": 13.99,
    "boiling_temperature": 20.271,
    "fusion_enthalpy": 0.117,
    "vaporisation_enthalpy": 0.904,
    "molar_heat_capacity": 28.836,
    "structure": "gas",
    "thermal_conductivity": 0.1805,
    "density": 0.00008988,
    "price": 1.39
})

Helium = Element(**{
    "name": "Helium",
    "symbol": "He",
    "periodic_number": 95,
    "radius_empirical": 1.2,
    "radius_calculated": 0.31,
    "radius_vanDerWaals": 1.4,
    "radius_covalent": 0.28,
    "radius_USE": 1.286,
    "mass": 4.002602,
    "group": 18,
    "period": 1,
    "block": "s",
    "series": "noble",
    "orbitals": [
        {
            "orbital": "1s",
            "electrons": 2
        }
    ],
    "electrons": 2,
    "protons": 2,
    "neutrons": 2,
    "valence": 0,
    "valence_electrons": 2,
    "electron_affinity": -0.52,
    "chemical_scale": 2.418,
    "mendeleev_universal_sequence": 92,
    "mendeleev_pettifor": 1,
    "mendeleev_modified": 1,
    "electronegativity_pauling": 3.1,
    "electronegativity_allen": 4.16,
    "ionisation_energies": [
        2372.3,
        5250.5
    ],
    "chemical_hardness": 24.59,
    "chemical_potential": -12.29,
    "melting_temperature": 0.95,
    "boiling_temperature": 4.222,
    "fusion_enthalpy": 0.0138,
    "vaporisation_enthalpy": 0.0829,
    "molar_heat_capacity": 20.78,
    "structure": "gas",
    "thermal_conductivity": 0.1513,
    "density": 0.0001785,
    "price": 24
})

Lithium = Element(**{
    "name": "Lithium",
    "symbol": "Li",
    "periodic_number": 1,
    "radius_empirical": 1.45,
    "radius_calculated": 1.67,
    "radius_vanDerWaals": 1.82,
    "radius_covalent": 1.28,
    "radius_metallic": 1.52,
    "radius_USE": 1.374,
    "volume_miedema": 13.0,
    "mass": 6.94,
    "group": 1,
    "period": 2,
    "block": "s",
    "series": "alkali_metal",
    "orbitals": [
        *Helium.orbitals,
        {
            "orbital": "2s",
            "electrons": 1
        }
    ],
    "electrons": 3,
    "protons": 3,
    "neutrons": 4,
    "valence": 1,
    "valence_electrons": 1,
    "electron_affinity": 0.618049,
    "wigner_seitz_electron_density": 0.94,
    "chemical_scale": 1.141,
    "mendeleev_universal_sequence": 26,
    "mendeleev_pettifor": 12,
    "mendeleev_modified": 12,
    "work_function": 2.93,
    "electronegativity_pauling": 0.98,
    "electronegativity_allen": 0.912,
    "electronegativity_miedema": 2.85,
    "miedema_R": 0.0,
    "ionisation_energies": [
        520.2,
        7298.1
    ],
    "chemical_hardness": 4.77,
    "chemical_potential": -3,
    "melting_temperature": 453.65,
    "boiling_temperature": 1603,
    "fusion_enthalpy": 3,
    "vaporisation_enthalpy": 136,
    "molar_heat_capacity": 24.86,

    "thermal_conductivity": 85,
    "thermal_expansion": 0.000046,
    "structure": "A2",
    "density": 0.535,
    "cohesive_energy": 1.63,
    "debye_temperature": 448,
    "price": 85.6
})

Berylium = Element(**{
    "name": "Berylium",
    "symbol": "Be",
    "periodic_number": 64,
    "radius_empirical": 1.05,
    "radius_calculated": 1.12,
    "radius_vanDerWaals": 1.53,
    "radius_covalent": 0.96,
    "radius_metallic": 1.12,
    "radius_USE": 1.09,
    "volume_miedema": 4.9,
    "mass": 9.0121831,
    "group": 2,
    "period": 2,
    "block": "s",
    "series": "alkaline_earth_metal",
    "orbitals": [
        *Helium.orbitals,
        {
            "orbital": "2s",
            "electrons": 2
        }
    ],
    "electrons": 4,
    "protons": 4,
    "neutrons": 5,
    "valence": 2,
    "valence_electrons": 2,
    "electron_affinity": -0.52,
    "wigner_seitz_electron_density": 4.66,
    "chemical_scale": 1.71,
    "mendeleev_universal_sequence": 62,
    "mendeleev_pettifor": 74,
    "mendeleev_modified": 74,
    "work_function": 4.98,
    "electronegativity_pauling": 1.57,
    "electronegativity_allen": 1.576,
    "electronegativity_miedema": 5.05,
    "miedema_R": 0.4,
    "ionisation_energies": [
        899.5,
        1757.1
    ],
    "chemical_hardness": 9.32,
    "chemical_potential": -4.66,
    "melting_temperature": 1560,
    "boiling_temperature": 2742,
    "fusion_enthalpy": 12.2,
    "vaporisation_enthalpy": 292,
    "molar_heat_capacity": 16.443,

    "thermal_conductivity": 190,
    "thermal_expansion": 0.0000113,
    "structure": "A3",
    "density": 1.848,
    "cohesive_energy": 3.32,
    "debye_temperature": 1031,
    "price": 857
})

Boron = Element(**{
    "name": "Boron",
    "symbol": "B",
    "periodic_number": 69,
    "radius_empirical": 0.85,
    "radius_calculated": 0.87,
    "radius_vanDerWaals": 1.92,
    "radius_covalent": 0.85,
    "radius_USE": 0.933,
    "volume_miedema": 4.7,
    "mass": 10.81,
    "group": 13,
    "period": 2,
    "block": "p",
    "series": "metalloid",
    "orbitals": [
        *Helium.orbitals,
        {
            "orbital": "2s",
            "electrons": 2
        },
        {
            "orbital": "2p",
            "electrons": 1
        }
    ],
    "electrons": 5,
    "protons": 5,
    "neutrons": 6,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.279723,
    "wigner_seitz_electron_density": 5.36,
    "chemical_scale": 2.106,
    "mendeleev_universal_sequence": 86,
    "mendeleev_pettifor": 83,
    "mendeleev_modified": 83,
    "work_function": 4.45,
    "electronegativity_pauling": 2.04,
    "electronegativity_allen": 2.051,
    "electronegativity_miedema": 5.3,
    "miedema_R": 1.9,
    "ionisation_energies": [
        800.6,
        2427.1
    ],
    "chemical_hardness": 8.02,
    "chemical_potential": -4.29,
    "melting_temperature": 2349,
    "boiling_temperature": 4200,
    "fusion_enthalpy": 50.2,
    "vaporisation_enthalpy": 508,
    "molar_heat_capacity": 11.087,

    "thermal_conductivity": 27,
    "thermal_expansion": 0.000006,
    "structure": "R105",
    "density": 2.46,
    "cohesive_energy": 5.81,
    "debye_temperature": 1362,
    "price": 3.68
})

Carbon = Element(**{
    "name": "Carbon",
    "symbol": "C",
    "periodic_number": 74,
    "radius_empirical": 0.7,
    "radius_calculated": 0.67,
    "radius_vanDerWaals": 1.7,
    "radius_covalent": 0.76,
    "radius_USE": 0.891,
    "volume_miedema": 3.26,
    "mass": 12.011,
    "group": 14,
    "period": 2,
    "block": "p",
    "series": "non_metal",
    "orbitals": [
        *Helium.orbitals,
        {
            "orbital": "2s",
            "electrons": 2
        },
        {
            "orbital": "2p",
            "electrons": 2
        }
    ],
    "electrons": 6,
    "protons": 6,
    "neutrons": 6,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 1.2621226,
    "wigner_seitz_electron_density": 5.55,
    "chemical_scale": 2.43,
    "mendeleev_universal_sequence": 93,
    "mendeleev_pettifor": 92,
    "mendeleev_modified": 84,
    "work_function": 5,
    "electronegativity_pauling": 2.55,
    "electronegativity_allen": 2.544,
    "electronegativity_miedema": 6.24,
    "miedema_R": 2.1,
    "ionisation_energies": [
        1086.5,
        2352.6
    ],
    "chemical_hardness": 10,
    "chemical_potential": -6.26,
    "melting_temperature": 3823.15,
    "boiling_temperature": 4300.15,
    "fusion_enthalpy": 117,
    "vaporisation_enthalpy": 355.08,
    "molar_heat_capacity": 8.517,

    "thermal_conductivity": 140,
    "thermal_expansion": 0.0000071,
    "structure": "Af",
    "density": 2.26,
    "cohesive_energy": 7.37,
    "debye_temperature": 1550,
    "price": 0.122
})

Nitrogen = Element(**{
    "name": "Nitrogen",
    "symbol": "N",
    "periodic_number": 79,
    "radius_empirical": 0.65,
    "radius_calculated": 0.56,
    "radius_vanDerWaals": 1.55,
    "radius_covalent": 0.71,
    "radius_USE": 0.932,
    "volume_miedema": 4.1,
    "mass": 14.007,
    "group": 15,
    "period": 2,
    "block": "p",
    "series": "non_metal",
    "orbitals": [
        *Helium.orbitals,
        {
            "orbital": "2s",
            "electrons": 2
        },
        {
            "orbital": "2p",
            "electrons": 3
        }
    ],
    "electrons": 7,
    "protons": 7,
    "neutrons": 7,
    "valence": 3,
    "valence_electrons": 5,
    "electron_affinity": -0.07,
    "wigner_seitz_electron_density": 4.49,
    "chemical_scale": 2.675,
    "mendeleev_universal_sequence": 94,
    "mendeleev_pettifor": 97,
    "mendeleev_modified": 85,
    "work_function": 2.3,
    "electronegativity_pauling": 3.04,
    "electronegativity_allen": 3.066,
    "electronegativity_miedema": 6.86,
    "ionisation_energies": [
        1402.3,
        2856
    ],
    "chemical_hardness": 14.53,
    "chemical_potential": -7.27,
    "melting_temperature": 63.23,
    "boiling_temperature": 77.355,
    "fusion_enthalpy": 0.72,
    "vaporisation_enthalpy": 5.56,
    "molar_heat_capacity": 29.124,
    "structure": "gas",
    "thermal_conductivity": 0.02583,
    "density": 0.0012506,
    "cohesive_energy": 4.92,
    "price": 0.14
})

Oxygen = Element(**{
    "name": "Oxygen",
    "symbol": "O",
    "periodic_number": 84,
    "radius_empirical": 0.6,
    "radius_calculated": 0.48,
    "radius_vanDerWaals": 1.52,
    "radius_covalent": 0.66,
    "radius_USE": 0.997,
    "mass": 15.999,
    "group": 16,
    "period": 2,
    "block": "p",
    "series": "chalcogen",
    "orbitals": [
        *Helium.orbitals,
        {
            "orbital": "2s",
            "electrons": 2
        },
        {
            "orbital": "2p",
            "electrons": 4
        }
    ],
    "electrons": 8,
    "protons": 8,
    "neutrons": 8,
    "valence": 2,
    "valence_electrons": 6,
    "electron_affinity": 1.4611136,
    "chemical_scale": 2.849,
    "mendeleev_universal_sequence": 95,
    "mendeleev_pettifor": 98,
    "mendeleev_modified": 94,
    "electronegativity_pauling": 3.44,
    "electronegativity_allen": 3.61,
    "ionisation_energies": [
        1313.9,
        3388.3
    ],
    "chemical_hardness": 12.16,
    "chemical_potential": -7.54,
    "melting_temperature": 54.36,
    "boiling_temperature": 90.188,
    "fusion_enthalpy": 0.444,
    "vaporisation_enthalpy": 6.82,
    "molar_heat_capacity": 29.378,
    "structure": "gas",
    "thermal_conductivity": 0.02658,
    "density": 0.001429,
    "cohesive_energy": 2.6,
    "price": 0.154
})

Fluorine = Element(**{
    "name": "Fluorine",
    "symbol": "F",
    "periodic_number": 90,
    "radius_empirical": 0.5,
    "radius_calculated": 0.42,
    "radius_vanDerWaals": 1.47,
    "radius_covalent": 0.57,
    "radius_USE": 1.089,
    "mass": 18.998403163,
    "group": 17,
    "period": 2,
    "block": "p",
    "series": "halogen",
    "orbitals": [
        *Helium.orbitals,
        {
            "orbital": "2s",
            "electrons": 2
        },
        {
            "orbital": "2p",
            "electrons": 5
        }
    ],
    "electrons": 9,
    "protons": 9,
    "neutrons": 10,
    "valence": 1,
    "valence_electrons": 7,
    "electron_affinity": 3.4011898,
    "chemical_scale": 3.08,
    "mendeleev_universal_sequence": 96,
    "mendeleev_pettifor": 99,
    "mendeleev_modified": 99,
    "electronegativity_pauling": 3.98,
    "electronegativity_allen": 4.193,
    "ionisation_energies": [
        1681,
        3374.2
    ],
    "chemical_hardness": 14.02,
    "chemical_potential": -10.41,
    "melting_temperature": 53.48,
    "boiling_temperature": 85.03,
    "vaporisation_enthalpy": 6.51,
    "molar_heat_capacity": 31,
    "structure": "gas",
    "thermal_conductivity": 0.0277,
    "density": 0.001696,
    "cohesive_energy": 0.84,
    "price": 2.16
})

Neon = Element(**{
    "name": "Neon",
    "symbol": "Ne",
    "periodic_number": 96,
    "radius_empirical": 1.6,
    "radius_calculated": 0.38,
    "radius_vanDerWaals": 1.54,
    "radius_covalent": 0.58,
    "radius_USE": 1.409,
    "mass": 20.1797,
    "group": 18,
    "period": 2,
    "block": "p",
    "series": "noble",
    "orbitals": [
        *Helium.orbitals,
        {
            "orbital": "2s",
            "electrons": 2
        },
        {
            "orbital": "2p",
            "electrons": 6
        }
    ],
    "electrons": 10,
    "protons": 10,
    "neutrons": 10,
    "valence": 0,
    "valence_electrons": 8,
    "electron_affinity": -1.22,
    "chemical_scale": 2.373,
    "mendeleev_universal_sequence": 91,
    "mendeleev_pettifor": 2,
    "mendeleev_modified": 2,
    "electronegativity_pauling": 3.2,
    "electronegativity_allen": 4.787,
    "ionisation_energies": [
        2080.7,
        3952.3
    ],
    "chemical_hardness": 21.56,
    "chemical_potential": -10.78,
    "melting_temperature": 24.56,
    "boiling_temperature": 27.104,
    "fusion_enthalpy": 0.335,
    "vaporisation_enthalpy": 1.71,
    "molar_heat_capacity": 20.79,
    "structure": "gas",
    "thermal_conductivity": 0.0491,
    "density": 0.0008999,
    "cohesive_energy": 0.02,
    "price": 240
})

Sodium = Element(**{
    "name": "Sodium",
    "symbol": "Na",
    "periodic_number": 2,
    "radius_empirical": 1.8,
    "radius_calculated": 1.9,
    "radius_vanDerWaals": 2.27,
    "radius_covalent": 1.66,
    "radius_metallic": 1.86,
    "radius_USE": 1.701,
    "volume_miedema": 23.78,
    "mass": 22.98976928,
    "group": 1,
    "period": 3,
    "block": "s",
    "series": "alkali_metal",
    "orbitals": [
        *Neon.orbitals,
        {
            "orbital": "3s",
            "electrons": 1
        }
    ],
    "electrons": 11,
    "protons": 11,
    "neutrons": 12,
    "valence": 1,
    "valence_electrons": 1,
    "electron_affinity": 0.547926,
    "wigner_seitz_electron_density": 0.55,
    "chemical_scale": 0.843,
    "mendeleev_universal_sequence": 10,
    "mendeleev_pettifor": 11,
    "mendeleev_modified": 11,
    "work_function": 2.36,
    "electronegativity_pauling": 0.93,
    "electronegativity_allen": 0.869,
    "electronegativity_miedema": 2.7,
    "miedema_R": 0.0,
    "ionisation_energies": [
        495.8,
        4562
    ],
    "chemical_hardness": 4.59,
    "chemical_potential": -2.84,
    "melting_temperature": 370.944,
    "boiling_temperature": 1156.09,
    "fusion_enthalpy": 2.6,
    "vaporisation_enthalpy": 97.42,
    "molar_heat_capacity": 28.23,

    "thermal_conductivity": 140,
    "thermal_expansion": 0.00007,
    "structure": "A2",
    "density": 0.968,
    "cohesive_energy": 1.113,
    "debye_temperature": 155,
    "price": 3.43
})

Magnesium = Element(**{
    "name": "Magnesium",
    "symbol": "Mg",
    "periodic_number": 65,
    "radius_empirical": 1.5,
    "radius_calculated": 1.45,
    "radius_vanDerWaals": 1.73,
    "radius_covalent": 1.41,
    "radius_metallic": 1.6,
    "radius_USE": 1.508,
    "volume_miedema": 14.0,
    "mass": 24.305,
    "group": 2,
    "period": 3,
    "block": "s",
    "series": "alkaline_earth_metal",
    "orbitals": [
        *Neon.orbitals,
        {
            "orbital": "3s",
            "electrons": 2
        }
    ],
    "electrons": 12,
    "protons": 12,
    "neutrons": 12,
    "valence": 2,
    "valence_electrons": 2,
    "electron_affinity": -0.42,
    "wigner_seitz_electron_density": 1.6,
    "chemical_scale": 1.218,
    "mendeleev_universal_sequence": 28,
    "mendeleev_pettifor": 70,
    "mendeleev_modified": 70,
    "work_function": 3.66,
    "electronegativity_pauling": 1.31,
    "electronegativity_allen": 1.293,
    "electronegativity_miedema": 3.45,
    "miedema_R": 0.4,
    "ionisation_energies": [
        737.7,
        1450.7
    ],
    "chemical_hardness": 7.65,
    "chemical_potential": -3.82,
    "melting_temperature": 923,
    "boiling_temperature": 1363,
    "fusion_enthalpy": 8.48,
    "vaporisation_enthalpy": 128,
    "molar_heat_capacity": 24.869,

    "thermal_conductivity": 160,
    "thermal_expansion": 0.0000248,
    "structure": "A3",
    "density": 1.738,
    "cohesive_energy": 1.51,
    "debye_temperature": 330,
    "price": 2.32
})

Aluminium = Element(**{
    "name": "Aluminium",
    "symbol": "Al",
    "periodic_number": 70,
    "radius_empirical": 1.25,
    "radius_calculated": 1.18,
    "radius_vanDerWaals": 1.84,
    "radius_covalent": 1.21,
    "radius_metallic": 1.43,
    "radius_USE": 1.355,
    "volume_miedema": 10.0,
    "mass": 26.9815385,
    "group": 13,
    "period": 3,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Neon.orbitals,
        {
            "orbital": "3s",
            "electrons": 2
        },
        {
            "orbital": "3p",
            "electrons": 1
        }
    ],
    "electrons": 13,
    "protons": 13,
    "neutrons": 14,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.43283,
    "wigner_seitz_electron_density": 2.7,
    "chemical_scale": 1.514,
    "mendeleev_universal_sequence": 50,
    "mendeleev_pettifor": 77,
    "mendeleev_modified": 75,
    "work_function": 4.2,
    "electronegativity_pauling": 1.61,
    "electronegativity_allen": 1.613,
    "electronegativity_miedema": 4.2,
    "miedema_R": 1.9,
    "ionisation_energies": [
        577.5,
        1816.7
    ],
    "chemical_hardness": 5.55,
    "chemical_potential": -3.21,
    "melting_temperature": 933.47,
    "boiling_temperature": 2743,
    "fusion_enthalpy": 10.71,
    "vaporisation_enthalpy": 284,
    "molar_heat_capacity": 24.2,

    "thermal_conductivity": 235,
    "thermal_expansion": 0.0000231,
    "structure": "A1",
    "density": 2.7,
    "cohesive_energy": 3.39,
    "debye_temperature": 390,
    "price": 1.79
})

Silicon = Element(**{
    "name": "Silicon",
    "symbol": "Si",
    "periodic_number": 75,
    "radius_empirical": 1.1,
    "radius_calculated": 1.11,
    "radius_vanDerWaals": 2.1,
    "radius_covalent": 1.11,
    "radius_metallic": 1.43,
    "radius_USE": 1.269,
    "volume_miedema": 8.6,
    "mass": 28.085,
    "group": 14,
    "period": 3,
    "block": "p",
    "series": "metalloid",
    "orbitals": [
        *Neon.orbitals,
        {
            "orbital": "3s",
            "electrons": 2
        },
        {
            "orbital": "3p",
            "electrons": 2
        }
    ],
    "electrons": 14,
    "protons": 14,
    "neutrons": 14,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 1.3895212,
    "wigner_seitz_electron_density": 3.38,
    "chemical_scale": 1.75,
    "mendeleev_universal_sequence": 66,
    "mendeleev_pettifor": 82,
    "mendeleev_modified": 82,
    "work_function": 4.85,
    "electronegativity_pauling": 1.9,
    "electronegativity_allen": 1.916,
    "electronegativity_miedema": 4.7,
    "miedema_R": 2.1,
    "ionisation_energies": [
        786.5,
        1577.1
    ],
    "chemical_hardness": 6.76,
    "chemical_potential": -4.77,
    "melting_temperature": 1687,
    "boiling_temperature": 3538,
    "fusion_enthalpy": 50.21,
    "vaporisation_enthalpy": 383,
    "molar_heat_capacity": 19.789,

    "thermal_conductivity": 150,
    "thermal_expansion": 0.0000026,
    "structure": "A4",
    "density": 2.329,
    "cohesive_energy": 4.63,
    "debye_temperature": 692,
    "price": 1.7
})

Phosphorus = Element(**{
    "name": "Phosphorus",
    "symbol": "P",
    "periodic_number": 80,
    "radius_empirical": 1,
    "radius_calculated": 0.98,
    "radius_vanDerWaals": 1.8,
    "radius_covalent": 1.07,
    "radius_USE": 1.223,
    "volume_miedema": 8.6,
    "mass": 30.973761998,
    "group": 15,
    "period": 3,
    "block": "p",
    "series": "non_metal",
    "orbitals": [
        *Neon.orbitals,
        {
            "orbital": "3s",
            "electrons": 2
        },
        {
            "orbital": "3p",
            "electrons": 3
        }
    ],
    "electrons": 15,
    "protons": 15,
    "neutrons": 16,
    "valence": 5,
    "valence_electrons": 5,
    "electron_affinity": 0.746607,
    "wigner_seitz_electron_density": 4.49,
    "chemical_scale": 1.953,
    "mendeleev_universal_sequence": 81,
    "mendeleev_pettifor": 87,
    "mendeleev_modified": 86,
    "work_function": 4.5,
    "electronegativity_pauling": 2.19,
    "electronegativity_allen": 2.253,
    "electronegativity_miedema": 5.55,
    "miedema_R": 2.3,
    "ionisation_energies": [
        1011.8,
        1907
    ],
    "chemical_hardness": 9.74,
    "chemical_potential": -5.62,
    "melting_temperature": 317.3,
    "boiling_temperature": 317.3,
    "fusion_enthalpy": 0.66,
    "vaporisation_enthalpy": 51.9,
    "molar_heat_capacity": 23.824,

    "thermal_conductivity": 0.236,
    "thermal_expansion": 0.000127,
    "structure": "A2",
    "density": 1.823,
    "cohesive_energy": 3.43,
    "debye_temperature": 576,
    "price": 2.69
})

Sulfur = Element(**{
    "name": "Sulfur",
    "symbol": "S",
    "periodic_number": 85,
    "radius_empirical": 1,
    "radius_calculated": 0.88,
    "radius_vanDerWaals": 1.8,
    "radius_covalent": 1.05,
    "radius_USE": 1.293,
    "mass": 32.06,
    "group": 16,
    "period": 3,
    "block": "p",
    "series": "chalcogen",
    "orbitals": [
        *Neon.orbitals,
        {
            "orbital": "3s",
            "electrons": 2
        },
        {
            "orbital": "3p",
            "electrons": 4
        }
    ],
    "electrons": 16,
    "protons": 16,
    "neutrons": 16,
    "valence": 6,
    "valence_electrons": 6,
    "electron_affinity": 2.077104,
    "chemical_scale": 2.116,
    "mendeleev_universal_sequence": 87,
    "mendeleev_pettifor": 91,
    "mendeleev_modified": 93,
    "electronegativity_pauling": 2.58,
    "electronegativity_allen": 2.589,
    "ionisation_energies": [
        999.6,
        2252
    ],
    "chemical_hardness": 8.28,
    "chemical_potential": -6.22,
    "melting_temperature": 388.36,
    "boiling_temperature": 717.8,
    "fusion_enthalpy": 1.727,
    "vaporisation_enthalpy": 45,
    "molar_heat_capacity": 22.75,
    "thermal_conductivity": 0.205,
    "structure": "A17",
    "density": 2.07,
    "cohesive_energy": 2.85,
    "debye_temperature": 527,
    "price": 0.0926
})

Chlorine = Element(**{
    "name": "Chlorine",
    "symbol": "Cl",
    "periodic_number": 91,
    "radius_empirical": 1,
    "radius_calculated": 0.79,
    "radius_vanDerWaals": 1.75,
    "radius_covalent": 1.02,
    "radius_USE": 1.431,
    "mass": 35.45,
    "group": 17,
    "period": 3,
    "block": "p",
    "series": "halogen",
    "orbitals": [
        *Neon.orbitals,
        {
            "orbital": "3s",
            "electrons": 2
        },
        {
            "orbital": "3p",
            "electrons": 5
        }
    ],
    "electrons": 17,
    "protons": 17,
    "neutrons": 18,
    "valence": 5,
    "valence_electrons": 7,
    "electron_affinity": 3.612725,
    "chemical_scale": 2.332,
    "mendeleev_universal_sequence": 89,
    "mendeleev_pettifor": 96,
    "mendeleev_modified": 98,
    "electronegativity_pauling": 3.16,
    "electronegativity_allen": 2.869,
    "ionisation_energies": [
        1251.2,
        2298
    ],
    "chemical_hardness": 9.35,
    "chemical_potential": -8.29,
    "melting_temperature": 171.6,
    "boiling_temperature": 239.11,
    "fusion_enthalpy": 6.406,
    "vaporisation_enthalpy": 20.41,
    "molar_heat_capacity": 33.949,
    "structure": "gas",
    "thermal_conductivity": 0.0089,
    "density": 0.003214,
    "cohesive_energy": 1.4,
    "price": 0.082
})

Argon = Element(**{
    "name": "Argon",
    "symbol": "Ar",
    "periodic_number": 97,
    "radius_empirical": 0.71,
    "radius_calculated": 0.71,
    "radius_vanDerWaals": 1.88,
    "radius_covalent": 1.06,
    "radius_USE": 1.933,
    "mass": 39.948,
    "group": 18,
    "period": 3,
    "block": "p",
    "series": "noble",
    "orbitals": [
        *Neon.orbitals,
        {
            "orbital": "3s",
            "electrons": 2
        },
        {
            "orbital": "3p",
            "electrons": 6
        }
    ],
    "electrons": 18,
    "protons": 18,
    "neutrons": 22,
    "valence": 0,
    "valence_electrons": 8,
    "electron_affinity": -1,
    "chemical_scale": 1.885,
    "mendeleev_universal_sequence": 75,
    "mendeleev_pettifor": 3,
    "mendeleev_modified": 3,
    "electronegativity_pauling": 3.1,
    "electronegativity_allen": 3.242,
    "ionisation_energies": [
        1520.6,
        2665.8
    ],
    "chemical_hardness": 15.76,
    "chemical_potential": -7.88,
    "melting_temperature": 83.81,
    "boiling_temperature": 87.302,
    "fusion_enthalpy": 1.18,
    "vaporisation_enthalpy": 6.53,
    "molar_heat_capacity": 20.85,
    "structure": "gas",
    "thermal_conductivity": 0.01772,
    "density": 0.0017837,
    "cohesive_energy": 0.08,
    "price": 0.931
})

Potassium = Element(**{
    "name": "Potassium",
    "symbol": "K",
    "periodic_number": 3,
    "radius_empirical": 2.2,
    "radius_calculated": 2.43,
    "radius_vanDerWaals": 2.75,
    "radius_covalent": 2.03,
    "radius_metallic": 2.27,
    "radius_USE": 2.151,
    "volume_miedema": 45.63,
    "mass": 39.0983,
    "group": 1,
    "period": 4,
    "block": "s",
    "series": "alkali_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 1
        }
    ],
    "electrons": 19,
    "protons": 19,
    "neutrons": 20,
    "valence": 1,
    "valence_electrons": 1,
    "electron_affinity": 0.501459,
    "wigner_seitz_electron_density": 0.27,
    "chemical_scale": 0.411,
    "mendeleev_universal_sequence": 4,
    "mendeleev_pettifor": 10,
    "mendeleev_modified": 10,
    "work_function": 2.29,
    "electronegativity_pauling": 0.82,
    "electronegativity_allen": 0.734,
    "electronegativity_miedema": 2.25,
    "miedema_R": 0.0,
    "ionisation_energies": [
        418.8,
        3052
    ],
    "chemical_hardness": 3.84,
    "chemical_potential": -2.42,
    "melting_temperature": 336.7,
    "boiling_temperature": 1032,
    "fusion_enthalpy": 2.33,
    "vaporisation_enthalpy": 76.9,
    "molar_heat_capacity": 29.6,

    "thermal_conductivity": 100,
    "thermal_expansion": 0.000083,
    "structure": "A2",
    "density": 0.89,
    "cohesive_energy": 0.934,
    "debye_temperature": 100,
    "price": 13.6
})

Calcium = Element(**{
    "name": "Calcium",
    "symbol": "Ca",
    "periodic_number": 7,
    "radius_empirical": 1.8,
    "radius_calculated": 1.94,
    "radius_vanDerWaals": 2.31,
    "radius_covalent": 1.76,
    "radius_metallic": 1.97,
    "radius_USE": 1.761,
    "volume_miedema": 26.2,
    "mass": 40.078,
    "group": 2,
    "period": 4,
    "block": "s",
    "series": "alkaline_earth_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        }
    ],
    "electrons": 20,
    "protons": 20,
    "neutrons": 20,
    "valence": 2,
    "valence_electrons": 2,
    "electron_affinity": 0.02455,
    "wigner_seitz_electron_density": 0.75,
    "chemical_scale": 0.834,
    "mendeleev_universal_sequence": 9,
    "mendeleev_pettifor": 16,
    "mendeleev_modified": 16,
    "work_function": 2.87,
    "electronegativity_pauling": 1,
    "electronegativity_allen": 1.034,
    "electronegativity_miedema": 2.55,
    "miedema_R": 0.4,
    "ionisation_energies": [
        589.8,
        1145.4
    ],
    "chemical_hardness": 6.09,
    "chemical_potential": -3.07,
    "melting_temperature": 1115,
    "boiling_temperature": 1757,
    "fusion_enthalpy": 8.54,
    "vaporisation_enthalpy": 154.7,
    "molar_heat_capacity": 25.929,

    "thermal_conductivity": 200,
    "thermal_expansion": 0.0000223,
    "structure": "A1",
    "density": 1.55,
    "cohesive_energy": 1.84,
    "debye_temperature": 230,
    "price": 2.35
})

Scandium = Element(**{
    "name": "Scandium",
    "symbol": "Sc",
    "periodic_number": 11,
    "radius_empirical": 1.6,
    "radius_calculated": 1.84,
    "radius_vanDerWaals": 2.11,
    "radius_covalent": 1.7,
    "radius_metallic": 1.62,
    "radius_USE": 1.466,
    "volume_miedema": 15.03,
    "mass": 44.955908,
    "group": 3,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "3d",
            "electrons": 1
        }
    ],
    "electrons": 21,
    "protons": 21,
    "neutrons": 24,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.188,
    "wigner_seitz_electron_density": 2.05,
    "chemical_scale": 1.281,
    "mendeleev_universal_sequence": 34,
    "mendeleev_pettifor": 20,
    "mendeleev_modified": 45,
    "work_function": 3.5,
    "electronegativity_pauling": 1.36,
    "electronegativity_allen": 1.19,
    "electronegativity_miedema": 3.25,
    "miedema_R": 0.7,
    "ionisation_energies": [
        633.1,
        1235
    ],
    "chemical_hardness": 6.37,
    "chemical_potential": -3.38,
    "melting_temperature": 1814,
    "boiling_temperature": 3109,
    "fusion_enthalpy": 14.1,
    "vaporisation_enthalpy": 332.7,
    "molar_heat_capacity": 25.52,

    "thermal_conductivity": 16,
    "thermal_expansion": 0.0000102,
    "structure": "A3",
    "density": 2.985,
    "cohesive_energy": 3.9,
    "debye_temperature": 476,
    "price": 3460
})

Titanium = Element(**{
    "name": "Titanium",
    "symbol": "Ti",
    "periodic_number": 40,
    "radius_empirical": 1.4,
    "radius_calculated": 1.76,
    "radius_covalent": 1.6,
    "radius_metallic": 1.47,
    "radius_USE": 1.308,
    "volume_miedema": 10.58,
    "mass": 47.867,
    "group": 4,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "3d",
            "electrons": 2
        }
    ],
    "electrons": 22,
    "protons": 22,
    "neutrons": 22,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 0.07554,
    "wigner_seitz_electron_density": 3.51,
    "chemical_scale": 1.513,
    "mendeleev_universal_sequence": 49,
    "mendeleev_pettifor": 48,
    "mendeleev_modified": 48,
    "work_function": 4.33,
    "electronegativity_pauling": 1.54,
    "electronegativity_allen": 1.38,
    "electronegativity_miedema": 3.8,
    "miedema_R": 1.0,
    "ionisation_energies": [
        658.8,
        1309.8
    ],
    "chemical_hardness": 6.75,
    "chemical_potential": -3.45,
    "melting_temperature": 1941,
    "boiling_temperature": 3560,
    "fusion_enthalpy": 14.15,
    "vaporisation_enthalpy": 425,
    "molar_heat_capacity": 25.06,

    "thermal_conductivity": 22,
    "thermal_expansion": 0.0000086,
    "structure": "A3",
    "density": 4.506,
    "cohesive_energy": 4.85,
    "debye_temperature": 380,
    "price": 11.7
})

Vanadium = Element(**{
    "name": "Vanadium",
    "symbol": "V",
    "periodic_number": 43,
    "radius_empirical": 1.35,
    "radius_calculated": 1.71,
    "radius_covalent": 1.53,
    "radius_metallic": 1.34,
    "radius_USE": 1.209,
    "volume_miedema": 8.36,
    "mass": 50.9415,
    "group": 5,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "3d",
            "electrons": 3
        }
    ],
    "electrons": 23,
    "protons": 23,
    "neutrons": 28,
    "valence": 5,
    "valence_electrons": 5,
    "electron_affinity": 0.52766,
    "wigner_seitz_electron_density": 4.41,
    "chemical_scale": 1.646,
    "mendeleev_universal_sequence": 58,
    "mendeleev_pettifor": 51,
    "mendeleev_modified": 51,
    "work_function": 4.3,
    "electronegativity_pauling": 1.63,
    "electronegativity_allen": 1.53,
    "electronegativity_miedema": 4.25,
    "miedema_R": 1.0,
    "ionisation_energies": [
        650.9,
        1414
    ],
    "chemical_hardness": 6.22,
    "chemical_potential": -3.64,
    "melting_temperature": 2183,
    "boiling_temperature": 3680,
    "fusion_enthalpy": 21.5,
    "vaporisation_enthalpy": 444,
    "molar_heat_capacity": 24.89,

    "thermal_conductivity": 31,
    "thermal_expansion": 0.0000084,
    "structure": "A2",
    "density": 6.11,
    "cohesive_energy": 5.31,
    "debye_temperature": 390,
    "price": 385
})

Chromium = Element(**{
    "name": "Chromium",
    "symbol": "Cr",
    "periodic_number": 46,
    "radius_empirical": 1.4,
    "radius_calculated": 1.66,
    "radius_covalent": 1.39,
    "radius_metallic": 1.28,
    "radius_USE": 1.162,
    "volume_miedema": 7.23,
    "mass": 51.9961,
    "group": 6,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 1
        },
        {
            "orbital": "3d",
            "electrons": 5
        }
    ],
    "electrons": 24,
    "protons": 24,
    "neutrons": 28,
    "valence": 6,
    "valence_electrons": 6,
    "electron_affinity": 0.67584,
    "wigner_seitz_electron_density": 5.18,
    "chemical_scale": 1.702,
    "mendeleev_universal_sequence": 61,
    "mendeleev_pettifor": 54,
    "mendeleev_modified": 52,
    "work_function": 4.5,
    "electronegativity_pauling": 1.66,
    "electronegativity_allen": 1.65,
    "electronegativity_miedema": 4.65,
    "miedema_R": 1.0,
    "ionisation_energies": [
        652.9,
        1590.6
    ],
    "chemical_hardness": 6.09,
    "chemical_potential": -3.72,
    "melting_temperature": 2180,
    "boiling_temperature": 2944,
    "fusion_enthalpy": 21,
    "vaporisation_enthalpy": 347,
    "molar_heat_capacity": 23.35,

    "thermal_conductivity": 94,
    "thermal_expansion": 0.0000049,
    "structure": "A2",
    "density": 7.19,
    "cohesive_energy": 4.1,
    "debye_temperature": 424,
    "price": 9.4
})

Manganese = Element(**{
    "name": "Manganese",
    "symbol": "Mn",
    "periodic_number": 49,
    "radius_empirical": 1.4,
    "radius_calculated": 1.61,
    "radius_covalent": 1.39,
    "radius_metallic": 1.27,
    "radius_USE": 1.136,
    "volume_miedema": 7.35,
    "mass": 54.938044,
    "group": 7,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "3d",
            "electrons": 5
        }
    ],
    "electrons": 25,
    "protons": 25,
    "neutrons": 30,
    "valence": 4,
    "valence_electrons": 7,
    "electron_affinity": -0.5,
    "wigner_seitz_electron_density": 4.17,
    "chemical_scale": 1.661,
    "mendeleev_universal_sequence": 59,
    "mendeleev_pettifor": 57,
    "mendeleev_modified": 69,
    "work_function": 4.1,
    "electronegativity_pauling": 1.55,
    "electronegativity_allen": 1.75,
    "electronegativity_miedema": 4.45,
    "miedema_R": 1.0,
    "ionisation_energies": [
        717.3,
        1509
    ],
    "chemical_hardness": 7.43,
    "chemical_potential": -3.72,
    "melting_temperature": 1519,
    "boiling_temperature": 2334,
    "fusion_enthalpy": 12.91,
    "vaporisation_enthalpy": 221,
    "molar_heat_capacity": 26.32,

    "thermal_conductivity": 7.7,
    "thermal_expansion": 0.0000217,
    "structure": "A2",
    "density": 7.21,
    "cohesive_energy": 2.92,
    "debye_temperature": 363,
    "price": 1.82
})

Iron = Element(**{
    "name": "Iron",
    "symbol": "Fe",
    "periodic_number": 52,
    "radius_empirical": 1.4,
    "radius_calculated": 1.56,
    "radius_covalent": 1.32,
    "radius_metallic": 1.26,
    "radius_USE": 1.131,
    "volume_miedema": 7.09,
    "mass": 55.845,
    "group": 8,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "3d",
            "electrons": 6
        }
    ],
    "electrons": 26,
    "protons": 26,
    "neutrons": 30,
    "valence": 3,
    "valence_electrons": 8,
    "electron_affinity": 0.153236,
    "wigner_seitz_electron_density": 5.55,
    "chemical_scale": 1.824,
    "mendeleev_universal_sequence": 70,
    "mendeleev_pettifor": 58,
    "mendeleev_modified": 68,
    "work_function": 4.67,
    "electronegativity_pauling": 1.83,
    "electronegativity_allen": 1.8,
    "electronegativity_miedema": 4.93,
    "miedema_R": 1.0,
    "ionisation_energies": [
        762.5,
        1561.9
    ],
    "chemical_hardness": 7.75,
    "chemical_potential": -4.03,
    "melting_temperature": 1811,
    "boiling_temperature": 3134,
    "fusion_enthalpy": 13.81,
    "vaporisation_enthalpy": 340,
    "molar_heat_capacity": 25.1,

    "thermal_conductivity": 79,
    "thermal_expansion": 0.0000118,
    "structure": "A2",
    "density": 7.874,
    "cohesive_energy": 4.28,
    "debye_temperature": 373,
    "price": 0.424
})

Cobalt = Element(**{
    "name": "Cobalt",
    "symbol": "Co",
    "periodic_number": 55,
    "radius_empirical": 1.35,
    "radius_calculated": 1.52,
    "radius_covalent": 1.26,
    "radius_metallic": 1.25,
    "radius_USE": 1.137,
    "volume_miedema": 6.7,
    "mass": 58.933194,
    "group": 9,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "3d",
            "electrons": 7
        }
    ],
    "electrons": 27,
    "protons": 27,
    "neutrons": 32,
    "valence": 4,
    "valence_electrons": 9,
    "electron_affinity": 0.66226,
    "wigner_seitz_electron_density": 5.36,
    "chemical_scale": 1.847,
    "mendeleev_universal_sequence": 73,
    "mendeleev_pettifor": 61,
    "mendeleev_modified": 67,
    "work_function": 5,
    "electronegativity_pauling": 1.88,
    "electronegativity_allen": 1.84,
    "electronegativity_miedema": 5.1,
    "miedema_R": 1.0,
    "ionisation_energies": [
        760.4,
        1648
    ],
    "chemical_hardness": 7.22,
    "chemical_potential": -4.27,
    "melting_temperature": 1768,
    "boiling_temperature": 3200,
    "fusion_enthalpy": 16.06,
    "vaporisation_enthalpy": 377,
    "molar_heat_capacity": 24.81,

    "thermal_conductivity": 100,
    "thermal_expansion": 0.000013,
    "structure": "A3",
    "density": 8.9,
    "cohesive_energy": 4.39,
    "debye_temperature": 386,
    "price": 32.8
})

Nickel = Element(**{
    "name": "Nickel",
    "symbol": "Ni",
    "periodic_number": 58,
    "radius_empirical": 1.35,
    "radius_calculated": 1.49,
    "radius_vanDerWaals": 1.63,
    "radius_covalent": 1.24,
    "radius_metallic": 1.24,
    "radius_USE": 1.16,
    "volume_miedema": 6.6,
    "mass": 58.6934,
    "group": 10,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "3d",
            "electrons": 8
        }
    ],
    "electrons": 28,
    "protons": 28,
    "neutrons": 31,
    "valence": 2,
    "valence_electrons": 10,
    "electron_affinity": 1.15716,
    "wigner_seitz_electron_density": 5.36,
    "chemical_scale": 1.845,
    "mendeleev_universal_sequence": 72,
    "mendeleev_pettifor": 64,
    "mendeleev_modified": 66,
    "work_function": 5.22,
    "electronegativity_pauling": 1.91,
    "electronegativity_allen": 1.88,
    "electronegativity_miedema": 5.2,
    "miedema_R": 1.0,
    "ionisation_energies": [
        737.1,
        1753
    ],
    "chemical_hardness": 6.48,
    "chemical_potential": -4.4,
    "melting_temperature": 1728,
    "boiling_temperature": 3003,
    "fusion_enthalpy": 17.48,
    "vaporisation_enthalpy": 379,
    "molar_heat_capacity": 26.07,

    "thermal_conductivity": 91,
    "thermal_expansion": 0.0000134,
    "structure": "A1",
    "density": 8.908,
    "cohesive_energy": 4.44,
    "debye_temperature": 345,
    "price": 13.9
})

Copper = Element(**{
    "name": "Copper",
    "symbol": "Cu",
    "periodic_number": 61,
    "radius_empirical": 1.35,
    "radius_calculated": 1.45,
    "radius_vanDerWaals": 1.4,
    "radius_covalent": 1.32,
    "radius_metallic": 1.28,
    "radius_USE": 1.203,
    "volume_miedema": 7.12,
    "mass": 63.546,
    "group": 11,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 1
        },
        {
            "orbital": "3d",
            "electrons": 10
        }
    ],
    "electrons": 29,
    "protons": 29,
    "neutrons": 35,
    "valence": 2,
    "valence_electrons": 11,
    "electron_affinity": 1.23578,
    "wigner_seitz_electron_density": 3.18,
    "chemical_scale": 1.804,
    "mendeleev_universal_sequence": 68,
    "mendeleev_pettifor": 69,
    "mendeleev_modified": 65,
    "work_function": 5.1,
    "electronegativity_pauling": 1.9,
    "electronegativity_allen": 1.85,
    "electronegativity_miedema": 4.45,
    "miedema_R": 0.3,
    "ionisation_energies": [
        745.5,
        1957.9
    ],
    "chemical_hardness": 6.49,
    "chemical_potential": -4.48,
    "melting_temperature": 1357.77,
    "boiling_temperature": 2835,
    "fusion_enthalpy": 13.26,
    "vaporisation_enthalpy": 300.4,
    "molar_heat_capacity": 24.44,

    "thermal_conductivity": 400,
    "thermal_expansion": 0.0000165,
    "structure": "A1",
    "density": 8.96,
    "cohesive_energy": 3.49,
    "debye_temperature": 310,
    "price": 6
})

Zinc = Element(**{
    "name": "Zinc",
    "symbol": "Zn",
    "periodic_number": 66,
    "radius_empirical": 1.35,
    "radius_calculated": 1.42,
    "radius_vanDerWaals": 1.39,
    "radius_covalent": 1.22,
    "radius_metallic": 1.34,
    "radius_USE": 1.32,
    "volume_miedema": 9.17,
    "mass": 65.38,
    "group": 12,
    "period": 4,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "3d",
            "electrons": 10
        }
    ],
    "electrons": 30,
    "protons": 30,
    "neutrons": 30,
    "valence": 2,
    "valence_electrons": 12,
    "electron_affinity": -0.6,
    "wigner_seitz_electron_density": 2.3,
    "chemical_scale": 1.566,
    "mendeleev_universal_sequence": 53,
    "mendeleev_pettifor": 73,
    "mendeleev_modified": 71,
    "work_function": 3.63,
    "electronegativity_pauling": 1.65,
    "electronegativity_allen": 1.588,
    "electronegativity_miedema": 4.1,
    "miedema_R": 1.4,
    "ionisation_energies": [
        906.4,
        1733.3
    ],
    "chemical_hardness": 9.39,
    "chemical_potential": -4.7,
    "melting_temperature": 692.68,
    "boiling_temperature": 1180,
    "fusion_enthalpy": 7.32,
    "vaporisation_enthalpy": 115,
    "molar_heat_capacity": 25.47,

    "thermal_conductivity": 120,
    "thermal_expansion": 0.0000302,
    "structure": "A3",
    "density": 7.14,
    "cohesive_energy": 1.35,
    "debye_temperature": 237,
    "price": 2.55
})

Gallium = Element(**{
    "name": "Gallium",
    "symbol": "Ga",
    "periodic_number": 71,
    "radius_empirical": 1.3,
    "radius_calculated": 1.36,
    "radius_vanDerWaals": 1.87,
    "radius_covalent": 1.22,
    "radius_metallic": 1.35,
    "radius_USE": 1.365,
    "volume_miedema": 11.82,
    "mass": 69.723,
    "group": 13,
    "period": 4,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "3d",
            "electrons": 10
        },
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "4p",
            "electrons": 1
        }
    ],
    "electrons": 31,
    "protons": 31,
    "neutrons": 39,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.3012,
    "wigner_seitz_electron_density": 2.25,
    "chemical_scale": 1.62,
    "mendeleev_universal_sequence": 57,
    "mendeleev_pettifor": 78,
    "mendeleev_modified": 76,
    "work_function": 4.32,
    "electronegativity_pauling": 1.81,
    "electronegativity_allen": 1.756,
    "electronegativity_miedema": 4.1,
    "miedema_R": 1.9,
    "ionisation_energies": [
        578.8,
        1979.3
    ],
    "chemical_hardness": 5.57,
    "chemical_potential": -3.21,
    "melting_temperature": 302.9146,
    "boiling_temperature": 2673,
    "fusion_enthalpy": 5.59,
    "vaporisation_enthalpy": 256,
    "molar_heat_capacity": 25.86,

    "thermal_conductivity": 29,
    "thermal_expansion": 0.00012,
    "structure": "A11",
    "density": 5.91,
    "cohesive_energy": 2.81,
    "debye_temperature": 240,
    "price": 148
})

Germanium = Element(**{
    "name": "Germanium",
    "symbol": "Ge",
    "periodic_number": 76,
    "radius_empirical": 1.25,
    "radius_calculated": 1.25,
    "radius_vanDerWaals": 2.11,
    "radius_covalent": 1.2,
    "radius_USE": 1.365,
    "volume_miedema": 9.87,
    "mass": 72.63,
    "group": 14,
    "period": 4,
    "block": "p",
    "series": "metalloid",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "3d",
            "electrons": 10
        },
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "4p",
            "electrons": 2
        }
    ],
    "electrons": 32,
    "protons": 32,
    "neutrons": 41,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 1.2326764,
    "wigner_seitz_electron_density": 2.57,
    "chemical_scale": 1.733,
    "mendeleev_universal_sequence": 64,
    "mendeleev_pettifor": 81,
    "mendeleev_modified": 81,
    "work_function": 5,
    "electronegativity_pauling": 2.01,
    "electronegativity_allen": 1.994,
    "electronegativity_miedema": 4.55,
    "miedema_R": 2.1,
    "ionisation_energies": [
        762,
        1537.5
    ],
    "chemical_hardness": 6.67,
    "chemical_potential": -4.57,
    "melting_temperature": 1211.4,
    "boiling_temperature": 3106,
    "fusion_enthalpy": 36.94,
    "vaporisation_enthalpy": 334,
    "molar_heat_capacity": 23.222,

    "thermal_conductivity": 60,
    "thermal_expansion": 0.000006,
    "structure": "A4",
    "density": 5.323,
    "cohesive_energy": 3.85,
    "debye_temperature": 403,
    "price": 1010
})

Arsenic = Element(**{
    "name": "Arsenic",
    "symbol": "As",
    "periodic_number": 81,
    "radius_empirical": 1.15,
    "radius_calculated": 1.14,
    "radius_vanDerWaals": 1.85,
    "radius_covalent": 1.19,
    "radius_USE": 1.369,
    "volume_miedema": 11.85,
    "mass": 74.921595,
    "group": 15,
    "period": 4,
    "block": "p",
    "series": "metalloid",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "3d",
            "electrons": 10
        },
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "4p",
            "electrons": 3
        }
    ],
    "electrons": 33,
    "protons": 33,
    "neutrons": 42,
    "valence": 5,
    "valence_electrons": 5,
    "electron_affinity": 0.8048,
    "wigner_seitz_electron_density": 3,
    "chemical_scale": 1.827,
    "mendeleev_universal_sequence": 71,
    "mendeleev_pettifor": 86,
    "mendeleev_modified": 87,
    "work_function": 3.75,
    "electronegativity_pauling": 2.18,
    "electronegativity_allen": 2.211,
    "electronegativity_miedema": 4.8,
    "miedema_R": 2.3,
    "ionisation_energies": [
        947,
        1798
    ],
    "chemical_hardness": 8.98,
    "chemical_potential": -5.3,
    "melting_temperature": 883,
    "boiling_temperature": 1090.15,
    "fusion_enthalpy": 24.44,
    "vaporisation_enthalpy": 34.76,
    "molar_heat_capacity": 24.64,

    "thermal_conductivity": 50,
    "thermal_expansion": 0.0000047,
    "structure": "A7",
    "density": 5.727,
    "cohesive_energy": 2.96,
    "debye_temperature": 275,
    "price": 1.31
})

Selenium = Element(**{
    "name": "Selenium",
    "symbol": "Se",
    "periodic_number": 86,
    "radius_empirical": 1.15,
    "radius_calculated": 1.03,
    "radius_vanDerWaals": 1.9,
    "radius_covalent": 1.2,
    "radius_USE": 1.418,
    "mass": 78.971,
    "group": 16,
    "period": 4,
    "block": "p",
    "series": "chalcogen",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "3d",
            "electrons": 10
        },
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "4p",
            "electrons": 4
        }
    ],
    "electrons": 34,
    "protons": 34,
    "neutrons": 45,
    "valence": 6,
    "valence_electrons": 6,
    "electron_affinity": 2.0206047,
    "chemical_scale": 1.997,
    "mendeleev_universal_sequence": 84,
    "mendeleev_pettifor": 90,
    "mendeleev_modified": 92,
    "work_function": 5.9,
    "electronegativity_pauling": 2.55,
    "electronegativity_allen": 2.424,
    "ionisation_energies": [
        941,
        2045
    ],
    "chemical_hardness": 7.73,
    "chemical_potential": -5.88,
    "melting_temperature": 494,
    "boiling_temperature": 958,
    "fusion_enthalpy": 6.69,
    "vaporisation_enthalpy": 95.48,
    "molar_heat_capacity": 25.363,

    "thermal_conductivity": 0.52,
    "thermal_expansion": 0.000038,
    "structure": "A8",
    "density": 4.81,
    "cohesive_energy": 2.46,
    "debye_temperature": 90,
    "price": 21.4
})

Bromine = Element(**{
    "name": "Bromine",
    "symbol": "Br",
    "periodic_number": 92,
    "radius_empirical": 1.15,
    "radius_calculated": 0.94,
    "radius_vanDerWaals": 1.85,
    "radius_covalent": 1.2,
    "radius_USE": 1.551,
    "mass": 79.904,
    "group": 17,
    "period": 4,
    "block": "p",
    "series": "halogen",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "3d",
            "electrons": 10
        },
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "4p",
            "electrons": 5
        }
    ],
    "electrons": 35,
    "protons": 35,
    "neutrons": 45,
    "valence": 5,
    "valence_electrons": 7,
    "electron_affinity": 3.363588,
    "chemical_scale": 2.12,
    "mendeleev_universal_sequence": 88,
    "mendeleev_pettifor": 95,
    "mendeleev_modified": 97,
    "electronegativity_pauling": 2.96,
    "electronegativity_allen": 2.685,
    "ionisation_energies": [
        1139.9,
        2103
    ],
    "chemical_hardness": 8.45,
    "chemical_potential": -7.59,
    "melting_temperature": 265.8,
    "boiling_temperature": 332,
    "fusion_enthalpy": 10.571,
    "vaporisation_enthalpy": 29.96,
    "molar_heat_capacity": 75.69,
    "structure": "liquid",
    "thermal_conductivity": 0.12,
    "density": 3.1028,
    "cohesive_energy": 1.22,
    "price": 4.39
})

Krypton = Element(**{
    "name": "Krypton",
    "symbol": "Kr",
    "periodic_number": 98,

    "radius_calculated": 0.88,
    "radius_vanDerWaals": 2.02,
    "radius_covalent": 1.16,
    "radius_USE": 2.077,
    "mass": 83.798,
    "group": 18,
    "period": 4,
    "block": "p",
    "series": "noble",
    "orbitals": [
        *Argon.orbitals,
        {
            "orbital": "3d",
            "electrons": 10
        },
        {
            "orbital": "4s",
            "electrons": 2
        },
        {
            "orbital": "4p",
            "electrons": 6
        }
    ],
    "electrons": 36,
    "protons": 36,
    "neutrons": 48,
    "valence": 2,
    "valence_electrons": 8,
    "electron_affinity": -1,
    "chemical_scale": 1.71,
    "mendeleev_universal_sequence": 63,
    "mendeleev_pettifor": 4,
    "mendeleev_modified": 4,
    "electronegativity_pauling": 3,
    "electronegativity_allen": 2.966,
    "ionisation_energies": [
        1350.8,
        2350.4
    ],
    "chemical_hardness": 14,
    "chemical_potential": -7,
    "melting_temperature": 115.78,
    "boiling_temperature": 119.93,
    "fusion_enthalpy": 1.64,
    "vaporisation_enthalpy": 9.08,
    "molar_heat_capacity": 20.95,
    "structure": "gas",
    "thermal_conductivity": 0.00943,
    "density": 0.003749,
    "cohesive_energy": 0.116,
    "price": 290
})

Rubidium = Element(**{
    "name": "Rubidium",
    "symbol": "Rb",
    "periodic_number": 4,
    "radius_empirical": 2.35,
    "radius_calculated": 2.65,
    "radius_vanDerWaals": 3.03,
    "radius_covalent": 2.2,
    "radius_metallic": 2.48,
    "radius_USE": 2.319,
    "volume_miedema": 56.07,
    "mass": 84.4678,
    "group": 1,
    "period": 5,
    "block": "s",
    "series": "alkali_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 1
        }
    ],
    "electrons": 37,
    "protons": 37,
    "neutrons": 48,
    "valence": 1,
    "valence_electrons": 1,
    "electron_affinity": 0.485916,
    "wigner_seitz_electron_density": 0.22,
    "chemical_scale": 0.272,
    "mendeleev_universal_sequence": 3,
    "mendeleev_pettifor": 9,
    "mendeleev_modified": 9,
    "work_function": 2.261,
    "electronegativity_pauling": 0.82,
    "electronegativity_allen": 0.706,
    "electronegativity_miedema": 2.1,
    "miedema_R": 0.0,
    "ionisation_energies": [
        403,
        2633
    ],
    "chemical_hardness": 3.69,
    "chemical_potential": -2.33,
    "melting_temperature": 312.45,
    "boiling_temperature": 961,
    "fusion_enthalpy": 2.19,
    "vaporisation_enthalpy": 69,
    "molar_heat_capacity": 31.06,

    "thermal_conductivity": 58,
    "thermal_expansion": 0.00009,
    "structure": "A2",
    "density": 1.532,
    "cohesive_energy": 0.852,
    "debye_temperature": 59,
    "price": 15500
})

Strontium = Element(**{
    "name": "Strontium",
    "symbol": "Sr",
    "periodic_number": 8,
    "radius_empirical": 2,
    "radius_calculated": 2.19,
    "radius_vanDerWaals": 2.49,
    "radius_covalent": 1.95,
    "radius_metallic": 2.15,
    "radius_USE": 1.935,
    "volume_miedema": 33.93,
    "mass": 87.62,
    "group": 2,
    "period": 5,
    "block": "s",
    "series": "alkaline_earth_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 2
        }
    ],
    "electrons": 38,
    "protons": 38,
    "neutrons": 50,
    "valence": 2,
    "valence_electrons": 2,
    "electron_affinity": 0.05206,
    "wigner_seitz_electron_density": 0.59,
    "chemical_scale": 0.662,
    "mendeleev_universal_sequence": 7,
    "mendeleev_pettifor": 15,
    "mendeleev_modified": 15,
    "work_function": 2.59,
    "electronegativity_pauling": 0.95,
    "electronegativity_allen": 0.963,
    "electronegativity_miedema": 2.4,
    "miedema_R": 0.4,
    "ionisation_energies": [
        549.5,
        1064.2
    ],
    "chemical_hardness": 5.64,
    "chemical_potential": -2.88,
    "melting_temperature": 1050,
    "boiling_temperature": 1650,
    "fusion_enthalpy": 7.43,
    "vaporisation_enthalpy": 141,
    "molar_heat_capacity": 26.4,

    "thermal_conductivity": 35,
    "thermal_expansion": 0.0000225,
    "structure": "A1",
    "density": 2.64,
    "cohesive_energy": 1.72,
    "debye_temperature": 148,
    "price": 6.68
})

Yttrium = Element(**{
    "name": "Yttrium",
    "symbol": "Y",
    "periodic_number": 12,
    "radius_empirical": 1.8,
    "radius_calculated": 2.12,
    "radius_covalent": 1.9,
    "radius_metallic": 1.8,
    "radius_USE": 1.625,
    "volume_miedema": 19.9,
    "mass": 88.90584,
    "group": 3,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "4d",
            "electrons": 1
        }
    ],
    "electrons": 39,
    "protons": 39,
    "neutrons": 50,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.307,
    "wigner_seitz_electron_density": 1.77,
    "chemical_scale": 1.071,
    "mendeleev_universal_sequence": 19,
    "mendeleev_pettifor": 19,
    "mendeleev_modified": 21,
    "work_function": 3.1,
    "electronegativity_pauling": 1.22,
    "electronegativity_allen": 1.12,
    "electronegativity_miedema": 3.2,
    "miedema_R": 0.7,
    "ionisation_energies": [
        600,
        1180
    ],
    "chemical_hardness": 5.91,
    "chemical_potential": -3.27,
    "melting_temperature": 1799,
    "boiling_temperature": 3203,
    "fusion_enthalpy": 11.42,
    "vaporisation_enthalpy": 363,
    "molar_heat_capacity": 26.53,

    "thermal_conductivity": 17,
    "thermal_expansion": 0.0000106,
    "structure": "A3",
    "density": 4.472,
    "cohesive_energy": 4.37,
    "debye_temperature": 214,
    "price": 31
})

Zirconium = Element(**{
    "name": "Zirconium",
    "symbol": "Zr",
    "periodic_number": 41,
    "radius_empirical": 1.55,
    "radius_calculated": 2.06,
    "radius_covalent": 1.75,
    "radius_metallic": 1.6,
    "radius_USE": 1.463,
    "volume_miedema": 14.0,
    "mass": 91.224,
    "group": 4,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "4d",
            "electrons": 2
        }
    ],
    "electrons": 40,
    "protons": 40,
    "neutrons": 51,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 0.43328,
    "wigner_seitz_electron_density": 2.8,
    "chemical_scale": 1.266,
    "mendeleev_universal_sequence": 32,
    "mendeleev_pettifor": 46,
    "mendeleev_modified": 46,
    "work_function": 4.05,
    "electronegativity_pauling": 1.33,
    "electronegativity_allen": 1.32,
    "electronegativity_miedema": 3.45,
    "miedema_R": 1.0,
    "ionisation_energies": [
        640.1,
        1270
    ],
    "chemical_hardness": 6.21,
    "chemical_potential": -3.53,
    "melting_temperature": 2128,
    "boiling_temperature": 4650,
    "fusion_enthalpy": 14,
    "vaporisation_enthalpy": 591,
    "molar_heat_capacity": 25.36,

    "thermal_conductivity": 23,
    "thermal_expansion": 0.0000057,
    "structure": "A3",
    "density": 6.52,
    "cohesive_energy": 6.25,
    "debye_temperature": 250,
    "price": 37.1
})

Niobium = Element(**{
    "name": "Niobium",
    "symbol": "Nb",
    "periodic_number": 44,
    "radius_empirical": 1.45,
    "radius_calculated": 1.98,
    "radius_covalent": 1.64,
    "radius_metallic": 1.46,
    "radius_USE": 1.362,
    "volume_miedema": 10.8,
    "mass": 92.90637,
    "group": 5,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 1
        },
        {
            "orbital": "4d",
            "electrons": 4
        }
    ],
    "electrons": 41,
    "protons": 41,
    "neutrons": 52,
    "valence": 5,
    "valence_electrons": 5,
    "electron_affinity": 0.9174,
    "wigner_seitz_electron_density": 4.41,
    "chemical_scale": 1.503,
    "mendeleev_universal_sequence": 48,
    "mendeleev_pettifor": 49,
    "mendeleev_modified": 50,
    "work_function": 4.02,
    "electronegativity_pauling": 1.6,
    "electronegativity_allen": 1.41,
    "electronegativity_miedema": 4.05,
    "miedema_R": 1.0,
    "ionisation_energies": [
        652.1,
        1380
    ],
    "chemical_hardness": 5.86,
    "chemical_potential": -3.83,
    "melting_temperature": 2750,
    "boiling_temperature": 5017,
    "fusion_enthalpy": 30,
    "vaporisation_enthalpy": 689.9,
    "molar_heat_capacity": 24.6,

    "thermal_conductivity": 54,
    "thermal_expansion": 0.0000073,
    "structure": "A2",
    "density": 8.57,
    "cohesive_energy": 7.57,
    "debye_temperature": 260,
    "price": 85.6
})

Molybdenum = Element(**{
    "name": "Molybdenum",
    "symbol": "Mo",
    "periodic_number": 47,
    "radius_empirical": 1.45,
    "radius_calculated": 1.9,
    "radius_covalent": 1.54,
    "radius_metallic": 1.39,
    "radius_USE": 1.294,
    "volume_miedema": 9.4,
    "mass": 95.95,
    "group": 6,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 1
        },
        {
            "orbital": "4d",
            "electrons": 5
        }
    ],
    "electrons": 42,
    "protons": 42,
    "neutrons": 54,
    "valence": 6,
    "valence_electrons": 6,
    "electron_affinity": 0.7473,
    "wigner_seitz_electron_density": 5.55,
    "chemical_scale": 1.877,
    "mendeleev_universal_sequence": 74,
    "mendeleev_pettifor": 53,
    "mendeleev_modified": 53,
    "work_function": 4.53,
    "electronegativity_pauling": 2.16,
    "electronegativity_allen": 1.47,
    "electronegativity_miedema": 4.65,
    "miedema_R": 1.0,
    "ionisation_energies": [
        684.3,
        1560
    ],
    "chemical_hardness": 6.35,
    "chemical_potential": -3.92,
    "melting_temperature": 2896,
    "boiling_temperature": 4912,
    "fusion_enthalpy": 37.48,
    "vaporisation_enthalpy": 598,
    "molar_heat_capacity": 24.06,

    "thermal_conductivity": 139,
    "thermal_expansion": 0.0000048,
    "structure": "A2",
    "density": 10.28,
    "cohesive_energy": 6.82,
    "debye_temperature": 377,
    "price": 40.1
})

Technetium = Element(**{
    "name": "Technetium",
    "symbol": "Tc",
    "periodic_number": 50,
    "radius_empirical": 1.35,
    "radius_calculated": 1.83,
    "radius_covalent": 1.47,
    "radius_metallic": 1.36,
    "radius_USE": 1.257,
    "volume_miedema": 8.64,
    "mass": 97,
    "group": 7,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "4d",
            "electrons": 5
        }
    ],
    "electrons": 43,
    "protons": 43,
    "neutrons": 55,
    "valence": 6,
    "valence_electrons": 7,
    "electron_affinity": 0.55,
    "wigner_seitz_electron_density": 5.93,
    "chemical_scale": 1.76,
    "mendeleev_universal_sequence": 67,
    "mendeleev_pettifor": 55,
    "mendeleev_modified": 56,
    "work_function": 4.58,
    "electronegativity_pauling": 1.9,
    "electronegativity_allen": 1.51,
    "electronegativity_miedema": 5.3,
    "miedema_R": 1.0,
    "ionisation_energies": [
        702,
        1470
    ],
    "chemical_hardness": 6.73,
    "chemical_potential": -3.91,
    "melting_temperature": 2430,
    "boiling_temperature": 4538,
    "fusion_enthalpy": 33.29,
    "vaporisation_enthalpy": 585.2,
    "molar_heat_capacity": 24.27,

    "thermal_conductivity": 51,
    "thermal_expansion": 0.0000071,
    "structure": "A3",
    "density": 11,
    "cohesive_energy": 6.85,
    "debye_temperature": 422,
    "price": 100000
})

Ruthenium = Element(**{
    "name": "Ruthenium",
    "symbol": "Ru",
    "periodic_number": 53,
    "radius_empirical": 1.3,
    "radius_calculated": 1.78,
    "radius_covalent": 1.46,
    "radius_metallic": 1.34,
    "radius_USE": 1.249,
    "volume_miedema": 8.2,
    "mass": 101.07,
    "group": 8,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 1
        },
        {
            "orbital": "4d",
            "electrons": 7
        }
    ],
    "electrons": 44,
    "protons": 44,
    "neutrons": 57,
    "valence": 6,
    "valence_electrons": 8,
    "electron_affinity": 1.0468,
    "wigner_seitz_electron_density": 6.13,
    "chemical_scale": 1.937,
    "mendeleev_universal_sequence": 80,
    "mendeleev_pettifor": 60,
    "mendeleev_modified": 58,
    "work_function": 4.71,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 1.54,
    "electronegativity_miedema": 5.4,
    "miedema_R": 1.0,
    "ionisation_energies": [
        710.2,
        1620
    ],
    "chemical_hardness": 6.28,
    "chemical_potential": -4.22,
    "melting_temperature": 2607,
    "boiling_temperature": 4423,
    "fusion_enthalpy": 38.59,
    "vaporisation_enthalpy": 619,
    "molar_heat_capacity": 24.06,

    "thermal_conductivity": 120,
    "thermal_expansion": 0.0000064,
    "structure": "A3",
    "density": 12.45,
    "cohesive_energy": 6.74,
    "debye_temperature": 415,
    "price": 10600
})

Rhodium = Element(**{
    "name": "Rhodium",
    "symbol": "Rh",
    "periodic_number": 56,
    "radius_empirical": 1.35,
    "radius_calculated": 1.73,
    "radius_covalent": 1.42,
    "radius_metallic": 1.34,
    "radius_USE": 1.264,
    "volume_miedema": 8.3,
    "mass": 102.9055,
    "group": 9,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 1
        },
        {
            "orbital": "4d",
            "electrons": 8
        }
    ],
    "electrons": 45,
    "protons": 45,
    "neutrons": 58,
    "valence": 6,
    "valence_electrons": 9,
    "electron_affinity": 1.14289,
    "wigner_seitz_electron_density": 5.45,
    "chemical_scale": 1.97,
    "mendeleev_universal_sequence": 82,
    "mendeleev_pettifor": 63,
    "mendeleev_modified": 60,
    "work_function": 4.98,
    "electronegativity_pauling": 2.28,
    "electronegativity_allen": 1.56,
    "electronegativity_miedema": 5.4,
    "miedema_R": 1.0,
    "ionisation_energies": [
        719.7,
        1740
    ],
    "chemical_hardness": 6.32,
    "chemical_potential": -4.3,
    "melting_temperature": 2237,
    "boiling_temperature": 3968,
    "fusion_enthalpy": 26.59,
    "vaporisation_enthalpy": 493,
    "molar_heat_capacity": 24.98,

    "thermal_conductivity": 150,
    "thermal_expansion": 0.000008,
    "structure": "A1",
    "density": 12.41,
    "cohesive_energy": 5.75,
    "debye_temperature": 350,
    "price": 147000
})

Palladium = Element(**{
    "name": "Palladium",
    "symbol": "Pd",
    "periodic_number": 59,
    "radius_empirical": 1.4,
    "radius_calculated": 1.69,
    "radius_vanDerWaals": 1.63,
    "radius_covalent": 1.39,
    "radius_metallic": 1.37,
    "radius_USE": 1.306,
    "volume_miedema": 8.9,
    "mass": 106.42,
    "group": 10,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "4d",
            "electrons": 10
        }
    ],
    "electrons": 46,
    "protons": 46,
    "neutrons": 60,
    "valence": 4,
    "valence_electrons": 10,
    "electron_affinity": 0.56214,
    "wigner_seitz_electron_density": 4.66,
    "chemical_scale": 1.89,
    "mendeleev_universal_sequence": 76,
    "mendeleev_pettifor": 66,
    "mendeleev_modified": 62,
    "work_function": 4.85,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 1.58,
    "electronegativity_miedema": 5.45,
    "miedema_R": 1.0,
    "ionisation_energies": [
        804.4,
        1870
    ],
    "chemical_hardness": 7.77,
    "chemical_potential": -4.44,
    "melting_temperature": 1828.05,
    "boiling_temperature": 3236,
    "fusion_enthalpy": 16.74,
    "vaporisation_enthalpy": 358,
    "molar_heat_capacity": 25.98,

    "thermal_conductivity": 71,
    "thermal_expansion": 0.0000118,
    "structure": "A1",
    "density": 12.023,
    "cohesive_energy": 3.89,
    "debye_temperature": 275,
    "price": 49500
})

Silver = Element(**{
    "name": "Silver",
    "symbol": "Ag",
    "periodic_number": 62,
    "radius_empirical": 1.6,
    "radius_calculated": 1.65,
    "radius_vanDerWaals": 1.72,
    "radius_covalent": 1.45,
    "radius_metallic": 1.44,
    "radius_USE": 1.379,
    "volume_miedema": 10.24,
    "mass": 107.8682,
    "group": 11,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 1
        },
        {
            "orbital": "4d",
            "electrons": 10
        }
    ],
    "electrons": 47,
    "protons": 47,
    "neutrons": 61,
    "valence": 1,
    "valence_electrons": 11,
    "electron_affinity": 1.30447,
    "wigner_seitz_electron_density": 2.52,
    "chemical_scale": 1.676,
    "mendeleev_universal_sequence": 60,
    "mendeleev_pettifor": 68,
    "mendeleev_modified": 64,
    "work_function": 4.64,
    "electronegativity_pauling": 1.93,
    "electronegativity_allen": 1.87,
    "electronegativity_miedema": 4.35,
    "miedema_R": 0.15,
    "ionisation_energies": [
        731,
        2070
    ],
    "chemical_hardness": 6.27,
    "chemical_potential": -4.44,
    "melting_temperature": 1234.93,
    "boiling_temperature": 2435,
    "fusion_enthalpy": 11.28,
    "vaporisation_enthalpy": 254,
    "molar_heat_capacity": 25.35,

    "thermal_conductivity": 430,
    "thermal_expansion": 0.0000189,
    "structure": "A1",
    "density": 10.49,
    "cohesive_energy": 2.95,
    "debye_temperature": 221,
    "price": 521
})

Cadmium = Element(**{
    "name": "Cadmium",
    "symbol": "Cd",
    "periodic_number": 67,
    "radius_empirical": 1.55,
    "radius_calculated": 1.61,
    "radius_vanDerWaals": 1.58,
    "radius_covalent": 1.44,
    "radius_metallic": 1.51,
    "radius_USE": 1.509,
    "volume_miedema": 13.0,
    "mass": 112.414,
    "group": 12,
    "period": 5,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "4d",
            "electrons": 10
        }
    ],
    "electrons": 48,
    "protons": 48,
    "neutrons": 64,
    "valence": 2,
    "valence_electrons": 12,
    "electron_affinity": -0.7,
    "wigner_seitz_electron_density": 1.91,
    "chemical_scale": 1.433,
    "mendeleev_universal_sequence": 42,
    "mendeleev_pettifor": 72,
    "mendeleev_modified": 72,
    "work_function": 4.08,
    "electronegativity_pauling": 1.69,
    "electronegativity_allen": 1.521,
    "electronegativity_miedema": 4.05,
    "miedema_R": 1.4,
    "ionisation_energies": [
        867.8,
        1631.4
    ],
    "chemical_hardness": 8.99,
    "chemical_potential": -4.5,
    "melting_temperature": 594.22,
    "boiling_temperature": 1040,
    "fusion_enthalpy": 6.21,
    "vaporisation_enthalpy": 99.87,
    "molar_heat_capacity": 26.02,

    "thermal_conductivity": 96,
    "thermal_expansion": 0.0000308,
    "structure": "A3",
    "density": 8.65,
    "cohesive_energy": 1.16,
    "debye_temperature": 221,
    "price": 2.73
})

Indium = Element(**{
    "name": "Indium",
    "symbol": "In",
    "periodic_number": 72,
    "radius_empirical": 1.55,
    "radius_calculated": 1.56,
    "radius_vanDerWaals": 1.93,
    "radius_covalent": 1.42,
    "radius_metallic": 1.67,
    "radius_USE": 1.541,
    "volume_miedema": 15.75,
    "mass": 114.818,
    "group": 13,
    "period": 5,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "4d",
            "electrons": 10
        },
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "5p",
            "electrons": 1
        }
    ],
    "electrons": 49,
    "protons": 49,
    "neutrons": 66,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.38392,
    "wigner_seitz_electron_density": 1.6,
    "chemical_scale": 1.458,
    "mendeleev_universal_sequence": 45,
    "mendeleev_pettifor": 76,
    "mendeleev_modified": 77,
    "work_function": 4.09,
    "electronegativity_pauling": 1.78,
    "electronegativity_allen": 1.656,
    "electronegativity_miedema": 3.9,
    "miedema_R": 1.9,
    "ionisation_energies": [
        558.3,
        1820.7
    ],
    "chemical_hardness": 5.4,
    "chemical_potential": -3.09,
    "melting_temperature": 429.7485,
    "boiling_temperature": 2345,
    "fusion_enthalpy": 3.281,
    "vaporisation_enthalpy": 231.8,
    "molar_heat_capacity": 26.74,

    "thermal_conductivity": 82,
    "thermal_expansion": 0.0000321,
    "structure": "A6",
    "density": 7.31,
    "cohesive_energy": 2.52,
    "debye_temperature": 129,
    "price": 167
})

Tin = Element(**{
    "name": "Tin",
    "symbol": "Sn",
    "periodic_number": 77,
    "radius_empirical": 1.45,
    "radius_calculated": 1.45,
    "radius_vanDerWaals": 2.17,
    "radius_covalent": 1.39,
    "radius_USE": 1.541,
    "volume_miedema": 16.3,
    "mass": 118.71,
    "group": 14,
    "period": 5,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "4d",
            "electrons": 10
        },
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "5p",
            "electrons": 2
        }
    ],
    "electrons": 50,
    "protons": 50,
    "neutrons": 69,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 1.11207,
    "wigner_seitz_electron_density": 1.9,
    "chemical_scale": 1.56,
    "mendeleev_universal_sequence": 52,
    "mendeleev_pettifor": 80,
    "mendeleev_modified": 80,
    "work_function": 4.42,
    "electronegativity_pauling": 1.96,
    "electronegativity_allen": 1.824,
    "electronegativity_miedema": 4.15,
    "miedema_R": 2.1,
    "ionisation_energies": [
        708.6,
        1411.8
    ],
    "chemical_hardness": 6.23,
    "chemical_potential": -4.23,
    "melting_temperature": 505.08,
    "boiling_temperature": 2875,
    "fusion_enthalpy": 7.03,
    "vaporisation_enthalpy": 296.1,
    "molar_heat_capacity": 27.112,

    "thermal_conductivity": 67,
    "thermal_expansion": 0.000022,
    "structure": "A5",
    "density": 7.265,
    "cohesive_energy": 3.14,
    "debye_temperature": 254,
    "price": 18.7
})

Antimony = Element(**{
    "name": "Antimony",
    "symbol": "Sb",
    "periodic_number": 82,
    "radius_empirical": 1.45,
    "radius_calculated": 1.33,
    "radius_vanDerWaals": 2.06,
    "radius_covalent": 1.39,
    "radius_USE": 1.553,
    "volume_miedema": 16.95,
    "mass": 121.76,
    "group": 15,
    "period": 5,
    "block": "p",
    "series": "metalloid",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "4d",
            "electrons": 10
        },
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "5p",
            "electrons": 3
        }
    ],
    "electrons": 51,
    "protons": 51,
    "neutrons": 71,
    "valence": 5,
    "valence_electrons": 5,
    "electron_affinity": 1.047401,
    "wigner_seitz_electron_density": 2,
    "chemical_scale": 1.601,
    "mendeleev_universal_sequence": 56,
    "mendeleev_pettifor": 85,
    "mendeleev_modified": 88,
    "work_function": 4.55,
    "electronegativity_pauling": 2.05,
    "electronegativity_allen": 1.984,
    "electronegativity_miedema": 4.4,
    "miedema_R": 2.3,
    "ionisation_energies": [
        834,
        1594.9
    ],
    "chemical_hardness": 7.56,
    "chemical_potential": -4.82,
    "melting_temperature": 903.78,
    "boiling_temperature": 1908,
    "fusion_enthalpy": 19.79,
    "vaporisation_enthalpy": 193.43,
    "molar_heat_capacity": 25.23,

    "thermal_conductivity": 24,
    "thermal_expansion": 0.000011,
    "structure": "rhombohedral",
    "density": 6.697,
    "cohesive_energy": 2.75,
    "debye_temperature": 200,
    "price": 5.79
})

Tellurium = Element(**{
    "name": "Tellurium",
    "symbol": "Te",
    "periodic_number": 87,
    "radius_empirical": 1.4,
    "radius_calculated": 1.23,
    "radius_vanDerWaals": 2.06,
    "radius_covalent": 1.38,
    "radius_USE": 1.596,
    "volume_miedema": 20.02,
    "mass": 127.6,
    "group": 16,
    "period": 5,
    "block": "p",
    "series": "chalcogen",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "4d",
            "electrons": 10
        },
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "5p",
            "electrons": 4
        }
    ],
    "electrons": 52,
    "protons": 52,
    "neutrons": 76,
    "valence": 6,
    "valence_electrons": 6,
    "electron_affinity": 1.970875,
    "wigner_seitz_electron_density": 2.3526,
    "chemical_scale": 1.594,
    "mendeleev_universal_sequence": 55,
    "mendeleev_pettifor": 89,
    "mendeleev_modified": 91,
    "work_function": 4.95,
    "electronegativity_pauling": 2.1,
    "electronegativity_allen": 2.158,
    "electronegativity_miedema": 4.7,
    "miedema_R": 2.59,
    "ionisation_energies": [
        869.3,
        1790
    ],
    "chemical_hardness": 7.04,
    "chemical_potential": -5.49,
    "melting_temperature": 722.66,
    "boiling_temperature": 1261,
    "fusion_enthalpy": 17.49,
    "vaporisation_enthalpy": 114.1,
    "molar_heat_capacity": 25.73,

    "thermal_conductivity": 3,
    "thermal_expansion": 0.000018,
    "structure": "A8",
    "density": 6.24,
    "cohesive_energy": 2.19,
    "debye_temperature": 139,
    "price": 63.5
})

Iodine = Element(**{
    "name": "Iodine",
    "symbol": "I",
    "periodic_number": 93,
    "radius_empirical": 1.4,
    "radius_calculated": 1.15,
    "radius_vanDerWaals": 1.98,
    "radius_covalent": 1.39,
    "radius_USE": 1.721,
    "mass": 126.90447,
    "group": 17,
    "period": 5,
    "block": "p",
    "series": "halogen",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "4d",
            "electrons": 10
        },
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "5p",
            "electrons": 5
        }
    ],
    "electrons": 53,
    "protons": 53,
    "neutrons": 74,
    "valence": 7,
    "valence_electrons": 7,
    "electron_affinity": 3.0590465,
    "chemical_scale": 1.81,
    "mendeleev_universal_sequence": 69,
    "mendeleev_pettifor": 94,
    "mendeleev_modified": 96,
    "electronegativity_pauling": 2.66,
    "electronegativity_allen": 2.359,
    "ionisation_energies": [
        1008.4,
        1845.9
    ],
    "chemical_hardness": 7.39,
    "chemical_potential": -6.75,
    "melting_temperature": 386.85,
    "boiling_temperature": 457.4,
    "fusion_enthalpy": 15.52,
    "vaporisation_enthalpy": 41.57,
    "molar_heat_capacity": 54.44,

    "thermal_conductivity": 0.449,
    "structure": "A14",
    "density": 4.933,
    "cohesive_energy": 1.11,
    "debye_temperature": 109,
    "price": 35
})

Xenon = Element(**{
    "name": "Xenon",
    "symbol": "Xe",
    "periodic_number": 99,
    "radius_calculated": 1.08,
    "radius_vanDerWaals": 2.16,
    "radius_covalent": 1.4,
    "radius_USE": 2.344,
    "mass": 131.293,
    "group": 18,
    "period": 5,
    "block": "p",
    "series": "noble",
    "orbitals": [
        *Krypton.orbitals,
        {
            "orbital": "4d",
            "electrons": 10
        },
        {
            "orbital": "5s",
            "electrons": 2
        },
        {
            "orbital": "5p",
            "electrons": 6
        }
    ],
    "electrons": 54,
    "protons": 54,
    "neutrons": 77,
    "valence": 6,
    "valence_electrons": 8,
    "electron_affinity": -0.8,
    "chemical_scale": 1.263,
    "mendeleev_universal_sequence": 31,
    "mendeleev_pettifor": 5,
    "mendeleev_modified": 5,
    "electronegativity_pauling": 2.6,
    "electronegativity_allen": 2.582,
    "ionisation_energies": [
        1170.4,
        2046.4
    ],
    "chemical_hardness": 12.13,
    "chemical_potential": -6.07,
    "melting_temperature": 161.4,
    "boiling_temperature": 165.051,
    "fusion_enthalpy": 2.27,
    "vaporisation_enthalpy": 12.64,
    "molar_heat_capacity": 21.01,
    "structure": "gas",
    "thermal_conductivity": 0.00565,
    "density": 0.005894,
    "cohesive_energy": 0.16,
    "price": 1800
})

Caesium = Element(**{
    "name": "Caesium",
    "symbol": "Cs",
    "periodic_number": 5,
    "radius_empirical": 2.65,
    "radius_calculated": 2.98,
    "radius_vanDerWaals": 3.43,
    "radius_covalent": 2.44,
    "radius_metallic": 2.65,
    "radius_USE": 2.535,
    "volume_miedema": 69.23,
    "mass": 132.90545196,
    "group": 1,
    "period": 6,
    "block": "s",
    "series": "alkali_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 1
        }
    ],
    "electrons": 55,
    "protons": 55,
    "neutrons": 78,
    "valence": 1,
    "valence_electrons": 1,
    "electron_affinity": 0.47163,
    "wigner_seitz_electron_density": 0.17,
    "chemical_scale": 0.077,
    "mendeleev_universal_sequence": 2,
    "mendeleev_pettifor": 8,
    "mendeleev_modified": 8,
    "work_function": 1.95,
    "electronegativity_pauling": 0.79,
    "electronegativity_allen": 0.659,
    "electronegativity_miedema": 1.95,
    "miedema_R": 0.0,
    "ionisation_energies": [
        375.7,
        2234.3
    ],
    "chemical_hardness": 3.42,
    "chemical_potential": -2.18,
    "melting_temperature": 301.7,
    "boiling_temperature": 944,
    "fusion_enthalpy": 2.09,
    "vaporisation_enthalpy": 63.9,
    "molar_heat_capacity": 32.21,

    "thermal_conductivity": 36,
    "thermal_expansion": 0.000097,
    "structure": "A2",
    "density": 1.93,
    "cohesive_energy": 0.804,
    "debye_temperature": 43,
    "price": 61800
})

Barium = Element(**{
    "name": "Barium",
    "symbol": "Ba",
    "periodic_number": 9,
    "radius_empirical": 2.15,
    "radius_calculated": 2.53,
    "radius_vanDerWaals": 2.68,
    "radius_covalent": 2.15,
    "radius_metallic": 2.22,
    "radius_USE": 1.962,
    "volume_miedema": 38.2,
    "mass": 137.327,
    "group": 2,
    "period": 6,
    "block": "s",
    "series": "alkaline_earth_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        }
    ],
    "electrons": 56,
    "protons": 56,
    "neutrons": 81,
    "valence": 2,
    "valence_electrons": 2,
    "electron_affinity": 0.14462,
    "wigner_seitz_electron_density": 0.53,
    "chemical_scale": 0.606,
    "mendeleev_universal_sequence": 6,
    "mendeleev_pettifor": 14,
    "mendeleev_modified": 14,
    "work_function": 2.52,
    "electronegativity_pauling": 0.89,
    "electronegativity_allen": 0.881,
    "electronegativity_miedema": 2.32,
    "miedema_R": 0.4,
    "ionisation_energies": [
        502.9,
        965.2
    ],
    "chemical_hardness": 5.07,
    "chemical_potential": -2.68,
    "melting_temperature": 1000,
    "boiling_temperature": 2118,
    "fusion_enthalpy": 7.12,
    "vaporisation_enthalpy": 142,
    "molar_heat_capacity": 28.07,

    "thermal_conductivity": 18,
    "thermal_expansion": 0.0000206,
    "structure": "A2",
    "density": 3.51,
    "cohesive_energy": 1.9,
    "debye_temperature": 116,
    "price": 0.275
})

Lanthanum = Element(**{
    "name": "Lanthanum",
    "symbol": "La",
    "periodic_number": 13,
    "radius_empirical": 1.95,
    "radius_covalent": 2.07,
    "radius_metallic": 1.87,
    "radius_USE": 1.647,
    "volume_miedema": 22.55,
    "mass": 138.90547,
    "group": 3,
    "period": 6,
    "block": "d",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 1
        }
    ],
    "electrons": 57,
    "protons": 57,
    "neutrons": 82,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.557546,
    "wigner_seitz_electron_density": 1.64,
    "chemical_scale": 0.984,
    "mendeleev_universal_sequence": 13,
    "mendeleev_pettifor": 33,
    "mendeleev_modified": 32,
    "work_function": 3.5,
    "electronegativity_pauling": 1.1,
    "electronegativity_miedema": 3.17,
    "miedema_R": 0.7,
    "ionisation_energies": [
        538.1,
        1067
    ],
    "chemical_hardness": 5.11,
    "chemical_potential": -3.03,
    "melting_temperature": 1193,
    "boiling_temperature": 3737,
    "fusion_enthalpy": 6.2,
    "vaporisation_enthalpy": 400,
    "molar_heat_capacity": 27.11,

    "thermal_conductivity": 13,
    "thermal_expansion": 0.0000121,
    "structure": "A3",
    "density": 6.162,
    "cohesive_energy": 4.47,
    "debye_temperature": 135,
    "price": 4.92
})

Cerium = Element(**{
    "name": "Cerium",
    "symbol": "Ce",
    "periodic_number": 15,
    "radius_empirical": 1.85,
    "radius_covalent": 2.04,
    "radius_metallic": 1.818,
    "radius_USE": 1.467,
    "volume_miedema": 21.62,
    "mass": 140.116,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 1
        },
        {
            "orbital": "4f",
            "electrons": 1
        }
    ],
    "electrons": 58,
    "protons": 58,
    "neutrons": 82,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 0.57,
    "wigner_seitz_electron_density": 1.69,
    "chemical_scale": 1.144,
    "mendeleev_universal_sequence": 27,
    "mendeleev_pettifor": 32,
    "mendeleev_modified": 31,
    "work_function": 2.9,
    "electronegativity_pauling": 1.12,
    "electronegativity_miedema": 3.18,
    "miedema_R": 1.0,
    "ionisation_energies": [
        534.4,
        1050
    ],
    "chemical_hardness": 4.91,
    "chemical_potential": -3.09,
    "melting_temperature": 1068,
    "boiling_temperature": 3716,
    "fusion_enthalpy": 5.46,
    "vaporisation_enthalpy": 398,
    "molar_heat_capacity": 26.94,

    "thermal_conductivity": 11,
    "thermal_expansion": 0.0000063,
    "structure": "A3",
    "density": 6.77,
    "cohesive_energy": 4.32,
    "debye_temperature": 138,
    "price": 4.71
})

Praseodymium = Element(**{
    "name": "Praseodymium",
    "symbol": "Pr",
    "periodic_number": 17,
    "radius_empirical": 1.85,
    "radius_calculated": 2.47,
    "radius_covalent": 2.03,
    "radius_metallic": 1.824,
    "radius_USE": 1.367,
    "volume_miedema": 20.79,
    "mass": 140.90766,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 3
        }
    ],
    "electrons": 59,
    "protons": 59,
    "neutrons": 82,
    "valence": 4,
    "valence_electrons": 5,
    "electron_affinity": 0.10923,
    "wigner_seitz_electron_density": 1.73,
    "chemical_scale": 1.232,
    "mendeleev_universal_sequence": 29,
    "mendeleev_pettifor": 31,
    "mendeleev_modified": 30,
    "work_function": 2.7,
    "electronegativity_pauling": 1.13,
    "electronegativity_miedema": 3.19,
    "miedema_R": 1.0,
    "ionisation_energies": [
        527,
        1020
    ],
    "chemical_hardness": 4.51,
    "chemical_potential": -3.22,
    "melting_temperature": 1208,
    "boiling_temperature": 3403,
    "fusion_enthalpy": 6.89,
    "vaporisation_enthalpy": 331,
    "molar_heat_capacity": 27.2,

    "thermal_conductivity": 13,
    "thermal_expansion": 0.0000067,
    "structure": "A3",
    "density": 6.77,
    "cohesive_energy": 3.7,
    "debye_temperature": 138,
    "price": 103
})

Neodymium = Element(**{
    "name": "Neodymium",
    "symbol": "Nd",
    "periodic_number": 19,
    "radius_empirical": 1.85,
    "radius_calculated": 2.06,
    "radius_covalent": 2.01,
    "radius_metallic": 1.814,
    "radius_USE": 1.32,
    "volume_miedema": 20.58,
    "mass": 144.242,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 4
        }
    ],
    "electrons": 60,
    "protons": 60,
    "neutrons": 84,
    "valence": 3,
    "valence_electrons": 6,
    "electron_affinity": 0.09749,
    "wigner_seitz_electron_density": 1.73,
    "chemical_scale": 1.276,
    "mendeleev_universal_sequence": 33,
    "mendeleev_pettifor": 30,
    "mendeleev_modified": 29,
    "work_function": 3.2,
    "electronegativity_pauling": 1.14,
    "electronegativity_miedema": 3.19,
    "miedema_R": 1.0,
    "ionisation_energies": [
        533.1,
        1040
    ],
    "chemical_hardness": 5.36,
    "chemical_potential": -2.85,
    "melting_temperature": 1297,
    "boiling_temperature": 3347,
    "fusion_enthalpy": 7.14,
    "vaporisation_enthalpy": 289,
    "molar_heat_capacity": 27.45,

    "thermal_conductivity": 17,
    "thermal_expansion": 0.0000096,
    "structure": "A3",
    "density": 7.01,
    "cohesive_energy": 3.4,
    "debye_temperature": 148,
    "price": 57.5
})

Promethium = Element(**{
    "name": "Promethium",
    "symbol": "Pm",
    "periodic_number": 21,
    "radius_empirical": 1.85,
    "radius_calculated": 2.05,
    "radius_covalent": 1.99,
    "radius_metallic": 1.834,
    "radius_USE": 1.635,
    "volume_miedema": 20.25,
    "mass": 145,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 5
        }
    ],
    "electrons": 61,
    "protons": 61,
    "neutrons": 84,
    "valence": 3,
    "valence_electrons": 7,
    "electron_affinity": 0.129,
    "wigner_seitz_electron_density": 1.77,
    "chemical_scale": 1.011,
    "mendeleev_universal_sequence": 14,
    "mendeleev_pettifor": 29,
    "mendeleev_modified": 28,
    "electronegativity_pauling": 1.13,
    "electronegativity_miedema": 3.19,
    "ionisation_energies": [
        540,
        1050
    ],
    "chemical_hardness": 5.45,
    "chemical_potential": -2.86,
    "melting_temperature": 1315,
    "boiling_temperature": 3273,
    "fusion_enthalpy": 7.13,
    "vaporisation_enthalpy": 289,

    "thermal_conductivity": 15,
    "thermal_expansion": 0.000011,
    "structure": "A3",
    "density": 7.26,
    "cohesive_energy": 3.25,
    "price": 460000
})

Samarium = Element(**{
    "name": "Samarium",
    "symbol": "Sm",
    "periodic_number": 23,
    "radius_empirical": 1.85,
    "radius_calculated": 2.38,
    "radius_covalent": 1.98,
    "radius_metallic": 1.804,
    "radius_USE": 1.626,
    "volume_miedema": 20.01,
    "mass": 150.36,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 6
        }
    ],
    "electrons": 62,
    "protons": 62,
    "neutrons": 88,
    "valence": 3,
    "valence_electrons": 8,
    "electron_affinity": 0.162,
    "wigner_seitz_electron_density": 1.77,
    "chemical_scale": 1.041,
    "mendeleev_universal_sequence": 16,
    "mendeleev_pettifor": 28,
    "mendeleev_modified": 27,
    "work_function": 2.7,
    "electronegativity_pauling": 1.17,
    "electronegativity_miedema": 3.2,
    "miedema_R": 1.0,
    "ionisation_energies": [
        544.5,
        1070
    ],
    "chemical_hardness": 5.48,
    "chemical_potential": -2.91,
    "melting_temperature": 1345,
    "boiling_temperature": 2173,
    "fusion_enthalpy": 8.62,
    "vaporisation_enthalpy": 192,
    "molar_heat_capacity": 29.54,

    "thermal_conductivity": 13,
    "thermal_expansion": 0.0000127,
    "structure": "C19",
    "density": 7.52,
    "cohesive_energy": 2.14,
    "debye_temperature": 184,
    "price": 13.9
})

Europium = Element(**{
    "name": "Europium",
    "symbol": "Eu",
    "periodic_number": 25,
    "radius_empirical": 1.85,
    "radius_calculated": 2.31,
    "radius_covalent": 1.98,
    "radius_metallic": 1.804,
    "radius_USE": 1.62,
    "volume_miedema": 19.97,
    "mass": 151.964,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 7
        }
    ],
    "electrons": 63,
    "protons": 63,
    "neutrons": 89,
    "valence": 3,
    "valence_electrons": 9,
    "electron_affinity": 0.116,
    "wigner_seitz_electron_density": 1.77,
    "chemical_scale": 1.063,
    "mendeleev_universal_sequence": 18,
    "mendeleev_pettifor": 17,
    "mendeleev_modified": 18,
    "work_function": 2.5,
    "electronegativity_pauling": 1.2,
    "electronegativity_miedema": 3.2,
    "ionisation_energies": [
        547.1,
        1085
    ],
    "chemical_hardness": 5.55,
    "chemical_potential": -2.9,
    "melting_temperature": 1099,
    "boiling_temperature": 1802,
    "fusion_enthalpy": 9.21,
    "vaporisation_enthalpy": 176,
    "molar_heat_capacity": 27.66,

    "thermal_conductivity": 14,
    "thermal_expansion": 0.000035,
    "structure": "A2",
    "density": 5.264,
    "cohesive_energy": 1.86,
    "debye_temperature": 118,
    "price": 31.4
})

Gadolinium = Element(**{
    "name": "Gadolinium",
    "symbol": "Gd",
    "periodic_number": 27,
    "radius_empirical": 1.8,
    "radius_calculated": 2.33,
    "radius_covalent": 1.96,
    "radius_metallic": 1.804,
    "radius_USE": 1.623,
    "volume_miedema": 19.9,
    "mass": 157.25,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 1
        },
        {
            "orbital": "4f",
            "electrons": 7
        }
    ],
    "electrons": 64,
    "protons": 64,
    "neutrons": 93,
    "valence": 3,
    "valence_electrons": 10,
    "electron_affinity": 0.137,
    "wigner_seitz_electron_density": 1.77,
    "chemical_scale": 1.061,
    "mendeleev_universal_sequence": 17,
    "mendeleev_pettifor": 27,
    "mendeleev_modified": 26,
    "work_function": 2.9,
    "electronegativity_pauling": 1.2,
    "electronegativity_miedema": 3.2,
    "miedema_R": 1.0,
    "ionisation_energies": [
        593.4,
        1170
    ],
    "chemical_hardness": 6.01,
    "chemical_potential": -3.15,
    "melting_temperature": 1585,
    "boiling_temperature": 3273,
    "fusion_enthalpy": 10.05,
    "vaporisation_enthalpy": 301.3,
    "molar_heat_capacity": 37.03,

    "thermal_conductivity": 11,
    "thermal_expansion": 0.0000094,
    "structure": "A3",
    "density": 7.9,
    "cohesive_energy": 4.14,
    "debye_temperature": 155,
    "price": 28.6
})

Terbium = Element(**{
    "name": "Terbium",
    "symbol": "Tb",
    "periodic_number": 29,
    "radius_empirical": 1.75,
    "radius_calculated": 2.25,
    "radius_covalent": 1.94,
    "radius_metallic": 1.773,
    "radius_USE": 1.613,
    "volume_miedema": 19.32,
    "mass": 158.92535,
    "period": 6,
    "group": 3,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 9
        }
    ],
    "electrons": 65,
    "protons": 65,
    "neutrons": 94,
    "valence": 3,
    "valence_electrons": 11,
    "electron_affinity": 0.13131,
    "wigner_seitz_electron_density": 1.82,
    "chemical_scale": 1.012,
    "mendeleev_universal_sequence": 15,
    "mendeleev_pettifor": 26,
    "mendeleev_modified": 25,
    "work_function": 3,
    "electronegativity_pauling": 1.1,
    "electronegativity_miedema": 3.21,
    "miedema_R": 0.3,
    "ionisation_energies": [
        565.8,
        1110
    ],
    "chemical_hardness": 5.43,
    "chemical_potential": -3.15,
    "melting_temperature": 1629,
    "boiling_temperature": 3396,
    "fusion_enthalpy": 10.15,
    "vaporisation_enthalpy": 391,
    "molar_heat_capacity": 28.91,

    "thermal_conductivity": 11,
    "thermal_expansion": 0.0000103,
    "structure": "A3",
    "density": 8.23,
    "cohesive_energy": 4.05,
    "debye_temperature": 158,
    "price": 658
})

Dysprosium = Element(**{
    "name": "Dysprosium",
    "symbol": "Dy",
    "periodic_number": 31,
    "radius_empirical": 1.75,
    "radius_calculated": 2.28,
    "radius_covalent": 1.92,
    "radius_metallic": 1.781,
    "radius_USE": 1.613,
    "volume_miedema": 19.0,
    "mass": 162.5,
    "period": 6,
    "block": "f",
    "group": 3,
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 10
        }
    ],
    "electrons": 66,
    "protons": 66,
    "neutrons": 97,
    "valence": 3,
    "valence_electrons": 12,
    "electron_affinity": 0.3,
    "wigner_seitz_electron_density": 1.82,
    "chemical_scale": 1.081,
    "mendeleev_universal_sequence": 20,
    "mendeleev_pettifor": 25,
    "mendeleev_modified": 24,
    "work_function": 3.25,
    "electronegativity_pauling": 1.22,
    "electronegativity_miedema": 3.21,
    "miedema_R": 1.4,
    "ionisation_energies": [
        573,
        1130
    ],
    "chemical_hardness": 5.59,
    "chemical_potential": -3.15,
    "melting_temperature": 1680,
    "boiling_temperature": 2840,
    "fusion_enthalpy": 11.06,
    "vaporisation_enthalpy": 280,
    "molar_heat_capacity": 27.7,

    "thermal_conductivity": 11,
    "thermal_expansion": 0.00001,
    "structure": "A3",
    "density": 8.54,
    "cohesive_energy": 3.04,
    "debye_temperature": 158,
    "price": 307
})

Holmium = Element(**{
    "name": "Holmium",
    "symbol": "Ho",
    "periodic_number": 33,
    "radius_empirical": 1.75,
    "radius_calculated": 2.26,
    "radius_covalent": 1.92,
    "radius_metallic": 1.762,
    "radius_USE": 1.604,
    "volume_miedema": 18.76,
    "mass": 164.93033,
    "period": 6,
    "block": "f",
    "group": 3,
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 11
        }
    ],
    "electrons": 67,
    "protons": 67,
    "neutrons": 98,
    "valence": 3,
    "valence_electrons": 13,
    "electron_affinity": 0.338,
    "wigner_seitz_electron_density": 1.82,
    "chemical_scale": 1.094,
    "mendeleev_universal_sequence": 22,
    "mendeleev_pettifor": 24,
    "mendeleev_modified": 23,
    "work_function": 2.91,
    "electronegativity_pauling": 1.23,
    "electronegativity_miedema": 3.22,
    "miedema_R": 1.9,
    "ionisation_energies": [
        581,
        1140
    ],
    "chemical_hardness": 5.68,
    "chemical_potential": -3.18,
    "melting_temperature": 1734,
    "boiling_temperature": 2873,
    "fusion_enthalpy": 17,
    "vaporisation_enthalpy": 251,
    "molar_heat_capacity": 27.15,

    "thermal_conductivity": 16,
    "thermal_expansion": 0.0000112,
    "structure": "A3",
    "density": 8.79,
    "cohesive_energy": 3.14,
    "debye_temperature": 161,
    "price": 57.1
})

Erbium = Element(**{
    "name": "Erbium",
    "symbol": "Er",
    "periodic_number": 35,
    "radius_empirical": 1.75,
    "radius_calculated": 2.26,
    "radius_covalent": 1.89,
    "radius_metallic": 1.761,
    "radius_USE": 1.602,
    "volume_miedema": 18.45,
    "mass": 167.259,
    "period": 6,
    "block": "f",
    "group": 3,
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 12
        }
    ],
    "electrons": 68,
    "protons": 68,
    "neutrons": 99,
    "valence": 3,
    "valence_electrons": 14,
    "electron_affinity": 0.312,
    "wigner_seitz_electron_density": 1.86,
    "chemical_scale": 1.101,
    "mendeleev_universal_sequence": 23,
    "mendeleev_pettifor": 23,
    "mendeleev_modified": 22,
    "work_function": 3.25,
    "electronegativity_pauling": 1.24,
    "electronegativity_miedema": 3.22,
    "miedema_R": 2.1,
    "ionisation_energies": [
        589.3,
        1150
    ],
    "chemical_hardness": 5.8,
    "chemical_potential": -3.21,
    "melting_temperature": 1802,
    "boiling_temperature": 3141,
    "fusion_enthalpy": 19.9,
    "vaporisation_enthalpy": 280,
    "molar_heat_capacity": 28.12,

    "thermal_conductivity": 15,
    "thermal_expansion": 0.0000122,
    "structure": "A3",
    "density": 9.066,
    "cohesive_energy": 3.29,
    "debye_temperature": 168,
    "price": 26.4
})

Thulium = Element(**{
    "name": "Thulium",
    "symbol": "Tm",
    "periodic_number": 37,
    "radius_empirical": 1.75,
    "radius_calculated": 2.22,
    "radius_covalent": 1.9,
    "radius_metallic": 1.759,
    "radius_USE": 1.602,
    "volume_miedema": 18.12,
    "mass": 168.93422,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 13
        }
    ],
    "electrons": 69,
    "protons": 69,
    "neutrons": 100,
    "valence": 3,
    "valence_electrons": 15,
    "electron_affinity": 1.029,
    "wigner_seitz_electron_density": 1.86,
    "chemical_scale": 1.107,
    "mendeleev_universal_sequence": 24,
    "mendeleev_pettifor": 22,
    "mendeleev_modified": 20,
    "work_function": 3.22,
    "electronegativity_pauling": 1.25,
    "electronegativity_miedema": 3.22,
    "miedema_R": 2.3,
    "ionisation_energies": [
        596.7,
        1160
    ],
    "chemical_hardness": 6.17,
    "chemical_potential": -3.1,
    "melting_temperature": 1818,
    "boiling_temperature": 2223,
    "fusion_enthalpy": 16.84,
    "vaporisation_enthalpy": 191,
    "molar_heat_capacity": 27.03,

    "thermal_conductivity": 17,
    "thermal_expansion": 0.0000133,
    "structure": "A3",
    "density": 9.32,
    "cohesive_energy": 2.42,
    "debye_temperature": 167,
    "price": 3000
})

Ytterbium = Element(**{
    "name": "Ytterbium",
    "symbol": "Yb",
    "periodic_number": 38,
    "radius_empirical": 1.75,
    "radius_calculated": 2.22,
    "radius_covalent": 1.87,
    "radius_metallic": 1.76,
    "radius_USE": 1.759,
    "volume_miedema": 17.97,
    "mass": 173.045,
    "period": 6,
    "group": 3,
    "block": "f",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "4f",
            "electrons": 14
        }
    ],
    "electrons": 70,
    "protons": 70,
    "neutrons": 102,
    "valence": 3,
    "valence_electrons": 16,
    "electron_affinity": -0.02,
    "wigner_seitz_electron_density": 1.86,
    "chemical_scale": 0.892,
    "mendeleev_universal_sequence": 12,
    "mendeleev_pettifor": 17,
    "mendeleev_modified": 18,
    "work_function": 2.6,
    "electronegativity_pauling": 1.1,
    "electronegativity_miedema": 3.22,
    "miedema_R": 2.3,
    "ionisation_energies": [
        603.4,
        1174.8
    ],
    "chemical_hardness": 6.25,
    "chemical_potential": -3.13,
    "melting_temperature": 1097,
    "boiling_temperature": 1469,
    "fusion_enthalpy": 7.66,
    "vaporisation_enthalpy": 129,
    "molar_heat_capacity": 26.74,

    "thermal_conductivity": 39,
    "thermal_expansion": 0.0000263,
    "structure": "A1",
    "density": 6.9,
    "cohesive_energy": 1.6,
    "debye_temperature": 118,
    "price": 17.1
})

Lutetium = Element(**{
    "name": "Lutetium",
    "symbol": "Lu",
    "periodic_number": 39,
    "radius_empirical": 1.75,
    "radius_calculated": 2.17,
    "radius_covalent": 1.87,
    "radius_metallic": 1.738,
    "radius_USE": 1.605,
    "volume_miedema": 17.77,
    "mass": 174.9668,
    "group": 3,
    "period": 6,
    "block": "d",
    "series": "lanthanide",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 1
        }
    ],
    "electrons": 71,
    "protons": 71,
    "neutrons": 104,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.2388,
    "wigner_seitz_electron_density": 1.91,
    "chemical_scale": 1.116,
    "mendeleev_universal_sequence": 25,
    "mendeleev_pettifor": 21,
    "mendeleev_modified": 18,
    "work_function": 3.3,
    "electronegativity_pauling": 1.27,
    "electronegativity_allen": 1.09,
    "electronegativity_miedema": 3.22,
    "miedema_R": 0.7,
    "ionisation_energies": [
        523.5,
        1340
    ],
    "chemical_hardness": 5.09,
    "chemical_potential": -2.88,
    "melting_temperature": 1925,
    "boiling_temperature": 3675,
    "fusion_enthalpy": 22,
    "vaporisation_enthalpy": 414,
    "molar_heat_capacity": 26.86,

    "thermal_conductivity": 16,
    "thermal_expansion": 0.00001,
    "structure": "A3",
    "density": 9.841,
    "cohesive_energy": 4.43,
    "debye_temperature": 116,
    "price": 643
})

Hafnium = Element(**{
    "name": "Hafnium",
    "symbol": "Hf",
    "periodic_number": 42,
    "radius_empirical": 1.55,
    "radius_calculated": 2.08,
    "radius_covalent": 1.75,
    "radius_metallic": 1.59,
    "radius_USE": 1.454,
    "volume_miedema": 13.45,
    "mass": 178.49,
    "group": 4,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 2
        }
    ],
    "electrons": 72,
    "protons": 72,
    "neutrons": 106,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 0.178,
    "wigner_seitz_electron_density": 3.05,
    "chemical_scale": 1.257,
    "mendeleev_universal_sequence": 30,
    "mendeleev_pettifor": 47,
    "mendeleev_modified": 47,
    "work_function": 3.9,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": 1.16,
    "electronegativity_miedema": 3.6,
    "miedema_R": 1.0,
    "ionisation_energies": [
        658.5,
        1440
    ],
    "chemical_hardness": 6.71,
    "chemical_potential": -3.47,
    "melting_temperature": 2506,
    "boiling_temperature": 4876,
    "fusion_enthalpy": 27.2,
    "vaporisation_enthalpy": 648,
    "molar_heat_capacity": 25.73,

    "thermal_conductivity": 23,
    "thermal_expansion": 0.0000059,
    "structure": "A3",
    "density": 13.31,
    "cohesive_energy": 6.44,
    "debye_temperature": 213,
    "price": 900
})

Tantalum = Element(**{
    "name": "Tantalum",
    "symbol": "Ta",
    "periodic_number": 45,
    "radius_empirical": 1.45,
    "radius_calculated": 2,
    "radius_covalent": 1.7,
    "radius_metallic": 1.46,
    "radius_USE": 1.358,
    "volume_miedema": 10.81,
    "mass": 180.94788,
    "group": 5,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 3
        }
    ],
    "electrons": 73,
    "protons": 73,
    "neutrons": 108,
    "valence": 5,
    "valence_electrons": 5,
    "electron_affinity": 0.323,
    "wigner_seitz_electron_density": 4.33,
    "chemical_scale": 1.449,
    "mendeleev_universal_sequence": 44,
    "mendeleev_pettifor": 50,
    "mendeleev_modified": 49,
    "work_function": 4.25,
    "electronegativity_pauling": 1.5,
    "electronegativity_allen": 1.34,
    "electronegativity_miedema": 4.05,
    "miedema_R": 1.0,
    "ionisation_energies": [
        761,
        1500
    ],
    "chemical_hardness": 7.23,
    "chemical_potential": -3.94,
    "melting_temperature": 3290,
    "boiling_temperature": 5731,
    "fusion_enthalpy": 36.57,
    "vaporisation_enthalpy": 753,
    "molar_heat_capacity": 25.36,

    "thermal_conductivity": 57,
    "thermal_expansion": 0.0000063,
    "structure": "A2",
    "density": 16.69,
    "cohesive_energy": 8.1,
    "debye_temperature": 225,
    "price": 312
})

Tungsten = Element(**{
    "name": "Tungsten",
    "symbol": "W",
    "periodic_number": 48,
    "radius_empirical": 1.35,
    "radius_calculated": 1.93,
    "radius_covalent": 1.62,
    "radius_metallic": 1.39,
    "radius_USE": 1.316,
    "volume_miedema": 9.55,
    "mass": 183.84,
    "group": 6,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 4
        }
    ],
    "electrons": 74,
    "protons": 74,
    "neutrons": 110,
    "valence": 6,
    "valence_electrons": 6,
    "electron_affinity": 0.81626,
    "wigner_seitz_electron_density": 5.93,
    "chemical_scale": 1.973,
    "mendeleev_universal_sequence": 83,
    "mendeleev_pettifor": 52,
    "mendeleev_modified": 54,
    "work_function": 4.55,
    "electronegativity_pauling": 2.36,
    "electronegativity_allen": 1.47,
    "electronegativity_miedema": 4.8,
    "miedema_R": 1.0,
    "ionisation_energies": [
        770,
        1700
    ],
    "chemical_hardness": 7.05,
    "chemical_potential": -4.35,
    "melting_temperature": 3695,
    "boiling_temperature": 6203,
    "fusion_enthalpy": 52.31,
    "vaporisation_enthalpy": 774,
    "molar_heat_capacity": 24.27,

    "thermal_conductivity": 170,
    "thermal_expansion": 0.0000045,
    "structure": "A2",
    "density": 19.3,
    "cohesive_energy": 8.9,
    "debye_temperature": 312,
    "price": 35.3
})

Rhenium = Element(**{
    "name": "Rhenium",
    "symbol": "Re",
    "periodic_number": 51,
    "radius_empirical": 1.35,
    "radius_calculated": 1.88,
    "radius_covalent": 1.51,
    "radius_metallic": 1.37,
    "radius_USE": 1.287,
    "volume_miedema": 8.85,
    "mass": 186.207,
    "group": 7,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 5
        }
    ],
    "electrons": 75,
    "protons": 75,
    "neutrons": 111,
    "valence": 7,
    "valence_electrons": 7,
    "electron_affinity": 0.060396,
    "wigner_seitz_electron_density": 6.33,
    "chemical_scale": 1.735,
    "mendeleev_universal_sequence": 65,
    "mendeleev_pettifor": 56,
    "mendeleev_modified": 55,
    "work_function": 4.72,
    "electronegativity_pauling": 1.9,
    "electronegativity_allen": 1.6,
    "electronegativity_miedema": 5.2,
    "miedema_R": 1.0,
    "ionisation_energies": [
        760,
        1260
    ],
    "chemical_hardness": 7.68,
    "chemical_potential": -4,
    "melting_temperature": 3459,
    "boiling_temperature": 5903,
    "fusion_enthalpy": 60.43,
    "vaporisation_enthalpy": 704,
    "molar_heat_capacity": 25.48,

    "thermal_conductivity": 48,
    "thermal_expansion": 0.0000062,
    "structure": "A3",
    "density": 21.02,
    "cohesive_energy": 8.03,
    "debye_temperature": 275,
    "price": 4150
})

Osmium = Element(**{
    "name": "Osmium",
    "symbol": "Os",
    "periodic_number": 54,
    "radius_empirical": 1.3,
    "radius_calculated": 1.85,
    "radius_covalent": 1.44,
    "radius_metallic": 1.35,
    "radius_USE": 1.278,
    "volume_miedema": 8.45,
    "mass": 190.23,
    "group": 8,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 6
        }
    ],
    "electrons": 76,
    "protons": 76,
    "neutrons": 114,
    "valence": 6,
    "valence_electrons": 8,
    "electron_affinity": 1.0778,
    "wigner_seitz_electron_density": 6.33,
    "chemical_scale": 1.913,
    "mendeleev_universal_sequence": 78,
    "mendeleev_pettifor": 59,
    "mendeleev_modified": 57,
    "work_function": 5.93,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 1.65,
    "electronegativity_miedema": 5.4,
    "miedema_R": 1.0,
    "ionisation_energies": [
        840,
        1600
    ],
    "chemical_hardness": 7.36,
    "chemical_potential": -4.76,
    "melting_temperature": 3306,
    "boiling_temperature": 5285,
    "fusion_enthalpy": 31,
    "vaporisation_enthalpy": 378,
    "molar_heat_capacity": 24.7,

    "thermal_conductivity": 87,
    "thermal_expansion": 0.0000051,
    "structure": "A3",
    "density": 22.59,
    "cohesive_energy": 8.17,
    "debye_temperature": 400,
    "price": 12000
})

Iridium = Element(**{
    "name": "Iridium",
    "symbol": "Ir",
    "periodic_number": 57,
    "radius_empirical": 1.35,
    "radius_calculated": 1.8,
    "radius_covalent": 1.41,
    "radius_metallic": 1.355,
    "radius_USE": 1.288,
    "volume_miedema": 8.52,
    "mass": 192.217,
    "group": 9,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 7
        }
    ],
    "electrons": 77,
    "protons": 77,
    "neutrons": 115,
    "valence": 6,
    "valence_electrons": 9,
    "electron_affinity": 1.56436,
    "wigner_seitz_electron_density": 6.13,
    "chemical_scale": 1.905,
    "mendeleev_universal_sequence": 77,
    "mendeleev_pettifor": 62,
    "mendeleev_modified": 59,
    "work_function": 5.67,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 1.68,
    "electronegativity_miedema": 5.55,
    "miedema_R": 1.0,
    "ionisation_energies": [
        880,
        1600
    ],
    "chemical_hardness": 7.4,
    "chemical_potential": -5.27,
    "melting_temperature": 2719,
    "boiling_temperature": 4403,
    "fusion_enthalpy": 41.12,
    "vaporisation_enthalpy": 564,
    "molar_heat_capacity": 25.1,

    "thermal_conductivity": 150,
    "thermal_expansion": 0.0000064,
    "structure": "A1",
    "density": 22.56,
    "cohesive_energy": 6.94,
    "debye_temperature": 228,
    "price": 56200
})

Platinum = Element(**{
    "name": "Platinum",
    "symbol": "Pt",
    "periodic_number": 60,
    "radius_empirical": 1.35,
    "radius_calculated": 1.77,
    "radius_vanDerWaals": 1.75,
    "radius_covalent": 1.36,
    "radius_metallic": 1.385,
    "radius_USE": 1.311,
    "volume_miedema": 9.1,
    "mass": 195.084,
    "group": 10,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 1
        },
        {
            "orbital": "5d",
            "electrons": 9
        }
    ],
    "electrons": 78,
    "protons": 78,
    "neutrons": 117,
    "valence": 6,
    "valence_electrons": 10,
    "electron_affinity": 2.1251,
    "wigner_seitz_electron_density": 5.64,
    "chemical_scale": 1.931,
    "mendeleev_universal_sequence": 79,
    "mendeleev_pettifor": 65,
    "mendeleev_modified": 61,
    "work_function": 5.64,
    "electronegativity_pauling": 2.28,
    "electronegativity_allen": 1.72,
    "electronegativity_miedema": 5.65,
    "miedema_R": 1.0,
    "ionisation_energies": [
        870,
        1791
    ],
    "chemical_hardness": 6.83,
    "chemical_potential": -5.54,
    "melting_temperature": 2041.4,
    "boiling_temperature": 4098,
    "fusion_enthalpy": 22.17,
    "vaporisation_enthalpy": 510,
    "molar_heat_capacity": 25.86,

    "thermal_conductivity": 71,
    "thermal_expansion": 0.0000089,
    "structure": "A1",
    "density": 21.45,
    "cohesive_energy": 5.84,
    "debye_temperature": 225,
    "price": 27800
})

Gold = Element(**{
    "name": "Gold",
    "symbol": "Au",
    "periodic_number": 63,
    "radius_empirical": 1.35,
    "radius_calculated": 1.74,
    "radius_vanDerWaals": 1.66,
    "radius_covalent": 1.36,
    "radius_metallic": 1.44,
    "radius_USE": 1.374,
    "volume_miedema": 10.2,
    "mass": 196.96657,
    "group": 11,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 1
        },
        {
            "orbital": "5d",
            "electrons": 10
        }
    ],
    "electrons": 79,
    "protons": 79,
    "neutrons": 118,
    "valence": 5,
    "valence_electrons": 11,
    "electron_affinity": 2.30861,
    "wigner_seitz_electron_density": 3.87,
    "chemical_scale": 2.027,
    "mendeleev_universal_sequence": 85,
    "mendeleev_pettifor": 67,
    "mendeleev_modified": 63,
    "work_function": 5.47,
    "electronegativity_pauling": 2.54,
    "electronegativity_allen": 1.92,
    "electronegativity_miedema": 5.15,
    "miedema_R": 0.3,
    "ionisation_energies": [
        890.1,
        1980
    ],
    "chemical_hardness": 6.92,
    "chemical_potential": -5.77,
    "melting_temperature": 1337.33,
    "boiling_temperature": 3243,
    "fusion_enthalpy": 12.55,
    "vaporisation_enthalpy": 342,
    "molar_heat_capacity": 25.418,

    "thermal_conductivity": 320,
    "thermal_expansion": 0.0000142,
    "structure": "A1",
    "density": 19.3,
    "cohesive_energy": 3.81,
    "debye_temperature": 178,
    "price": 44800
})

Mercury = Element(**{
    "name": "Mercury",
    "symbol": "Hg",
    "periodic_number": 68,
    "radius_empirical": 1.5,
    "radius_calculated": 1.71,
    "radius_vanDerWaals": 1.55,
    "radius_covalent": 1.32,
    "radius_metallic": 1.51,
    "radius_USE": 1.556,
    "volume_miedema": 14.08,
    "mass": 200.592,
    "group": 12,
    "period": 6,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "5d",
            "electrons": 10
        }
    ],
    "electrons": 80,
    "protons": 80,
    "neutrons": 121,
    "valence": 2,
    "valence_electrons": 12,
    "electron_affinity": -0.5,
    "wigner_seitz_electron_density": 1.91,
    "chemical_scale": 1.571,
    "mendeleev_universal_sequence": 54,
    "mendeleev_pettifor": 71,
    "mendeleev_modified": 73,
    "work_function": 4.5,
    "electronegativity_pauling": 2,
    "electronegativity_allen": 1.765,
    "electronegativity_miedema": 4.2,
    "miedema_R": 1.4,
    "ionisation_energies": [
        1007.1,
        1810
    ],
    "chemical_hardness": 10.44,
    "chemical_potential": -5.22,
    "melting_temperature": 234.321,
    "boiling_temperature": 629.88,
    "fusion_enthalpy": 2.29,
    "vaporisation_enthalpy": 59.11,
    "molar_heat_capacity": 27.983,
    "structure": "liquid",
    "thermal_conductivity": 8.3,
    "thermal_expansion": 0.000181,
    "density": 13.534,
    "cohesive_energy": 0.67,
    "debye_temperature": 92,
    "price": 30.2
})

Thallium = Element(**{
    "name": "Thallium",
    "symbol": "Tl",
    "periodic_number": 73,
    "radius_empirical": 1.9,
    "radius_calculated": 1.56,
    "radius_vanDerWaals": 1.96,
    "radius_covalent": 1.45,
    "radius_metallic": 1.7,
    "radius_USE": 1.617,
    "volume_miedema": 17.23,
    "mass": 204.38,
    "group": 13,
    "period": 6,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "5d",
            "electrons": 10
        },
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "6p",
            "electrons": 1
        }
    ],
    "electrons": 81,
    "protons": 81,
    "neutrons": 123,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.320053,
    "wigner_seitz_electron_density": 1.4,
    "chemical_scale": 1.304,
    "mendeleev_universal_sequence": 35,
    "mendeleev_pettifor": 75,
    "mendeleev_modified": 78,
    "work_function": 3.84,
    "electronegativity_pauling": 1.62,
    "electronegativity_allen": 1.789,
    "electronegativity_miedema": 3.9,
    "miedema_R": 1.9,
    "ionisation_energies": [
        589.4,
        1971
    ],
    "chemical_hardness": 5.73,
    "chemical_potential": -3.24,
    "melting_temperature": 577,
    "boiling_temperature": 1746,
    "fusion_enthalpy": 4.14,
    "vaporisation_enthalpy": 165,
    "molar_heat_capacity": 26.32,

    "thermal_conductivity": 46,
    "thermal_expansion": 0.0000299,
    "structure": "A3",
    "density": 11.85,
    "cohesive_energy": 1.88,
    "debye_temperature": 96,
    "price": 4200
})

Lead = Element(**{
    "name": "Lead",
    "symbol": "Pb",
    "periodic_number": 78,
    "radius_empirical": 1.8,
    "radius_calculated": 1.54,
    "radius_vanDerWaals": 2.02,
    "radius_covalent": 1.46,
    "radius_USE": 1.622,
    "volume_miedema": 18.28,
    "mass": 207.2,
    "group": 14,
    "period": 6,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "5d",
            "electrons": 10
        },
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "6p",
            "electrons": 2
        }
    ],
    "electrons": 82,
    "protons": 82,
    "neutrons": 125,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 0.356721,
    "wigner_seitz_electron_density": 1.52,
    "chemical_scale": 1.442,
    "mendeleev_universal_sequence": 43,
    "mendeleev_pettifor": 79,
    "mendeleev_modified": 79,
    "work_function": 4.25,
    "electronegativity_pauling": 1.87,
    "electronegativity_allen": 1.854,
    "electronegativity_miedema": 4.1,
    "miedema_R": 2.1,
    "ionisation_energies": [
        715.6,
        1450.5
    ],
    "chemical_hardness": 7.05,
    "chemical_potential": -3.88,
    "melting_temperature": 600.61,
    "boiling_temperature": 2022,
    "fusion_enthalpy": 4.77,
    "vaporisation_enthalpy": 179.5,
    "molar_heat_capacity": 26.65,

    "thermal_conductivity": 35,
    "thermal_expansion": 0.0000289,
    "structure": "A1",
    "density": 11.34,
    "cohesive_energy": 2.03,
    "debye_temperature": 87,
    "price": 2
})

Bismuth = Element(**{
    "name": "Bismuth",
    "symbol": "Bi",
    "periodic_number": 83,
    "radius_empirical": 1.6,
    "radius_calculated": 1.43,
    "radius_vanDerWaals": 2.07,
    "radius_covalent": 1.48,
    "radius_USE": 1.635,
    "volume_miedema": 19.62,
    "mass": 208.9804,
    "group": 15,
    "period": 6,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "5d",
            "electrons": 10
        },
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "6p",
            "electrons": 3
        }
    ],
    "electrons": 83,
    "protons": 83,
    "neutrons": 126,
    "valence": 5,
    "valence_electrons": 5,
    "electron_affinity": 0.942362,
    "wigner_seitz_electron_density": 1.56,
    "chemical_scale": 1.517,
    "mendeleev_universal_sequence": 51,
    "mendeleev_pettifor": 84,
    "mendeleev_modified": 89,
    "work_function": 4.34,
    "electronegativity_pauling": 2.02,
    "electronegativity_allen": 2.01,
    "electronegativity_miedema": 4.15,
    "miedema_R": 2.3,
    "ionisation_energies": [
        703,
        1610
    ],
    "chemical_hardness": 6.34,
    "chemical_potential": -4.12,
    "melting_temperature": 544.7,
    "boiling_temperature": 1837,
    "fusion_enthalpy": 11.3,
    "vaporisation_enthalpy": 179,
    "molar_heat_capacity": 25.52,

    "thermal_conductivity": 8,
    "thermal_expansion": 0.0000134,
    "structure": "rhombohedral",
    "density": 9.78,
    "cohesive_energy": 2.18,
    "debye_temperature": 116,
    "price": 6.36
})

Polonium = Element(**{
    "name": "Polonium",
    "symbol": "Po",
    "periodic_number": 88,
    "radius_empirical": 1.9,
    "radius_calculated": 1.35,
    "radius_vanDerWaals": 1.97,
    "radius_covalent": 1.4,
    "radius_USE": 1.67,
    "mass": 209,
    "group": 16,
    "period": 6,
    "block": "p",
    "series": "chalcogen",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "5d",
            "electrons": 10
        },
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "6p",
            "electrons": 4
        }
    ],
    "electrons": 84,
    "protons": 84,
    "neutrons": 125,
    "valence": 6,
    "valence_electrons": 6,
    "electron_affinity": 1.4,
    "chemical_scale": 1.477,
    "mendeleev_universal_sequence": 46,
    "mendeleev_pettifor": 88,
    "mendeleev_modified": 90,
    "electronegativity_pauling": 2,
    "electronegativity_allen": 2.19,
    "ionisation_energies": [
        812.1
    ],
    "chemical_hardness": 6.51,
    "chemical_potential": -5.15,
    "melting_temperature": 527,
    "boiling_temperature": 1235,
    "fusion_enthalpy": 13,
    "vaporisation_enthalpy": 102.91,
    "molar_heat_capacity": 26.4,

    "thermal_expansion": 0.0000235,
    "structure": "Ah",
    "density": 9.196,
    "cohesive_energy": 1.5,
    "price": 49200000000000
})

Astatine = Element(**{
    "name": "Astatine",
    "symbol": "At",
    "periodic_number": 94,

    "radius_calculated": 1.27,
    "radius_vanDerWaals": 2.02,
    "radius_covalent": 1.5,
    "radius_USE": 1.777,
    "mass": 210,
    "group": 17,
    "period": 6,
    "block": "p",
    "series": "halogen",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "5d",
            "electrons": 10
        },
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "6p",
            "electrons": 5
        }
    ],
    "electrons": 85,
    "protons": 85,
    "neutrons": 125,
    "valence": 7,
    "valence_electrons": 7,
    "electron_affinity": 2.41578,
    "chemical_scale": 1.502,
    "mendeleev_universal_sequence": 47,
    "mendeleev_pettifor": 93,
    "mendeleev_modified": 95,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 2.39,
    "ionisation_energies": [
        899.003
    ],
    "chemical_hardness": 6.52,
    "chemical_potential": -6.05,
    "melting_temperature": 503,
    "vaporisation_enthalpy": 54.39,

    "thermal_conductivity": 2,
    "structure": "A1",
    "density": 6.35,
})

Radon = Element(**{
    "name": "Radon",
    "symbol": "Rn",
    "periodic_number": 100,

    "radius_calculated": 1.2,
    "radius_vanDerWaals": 2.2,
    "radius_covalent": 2.21,
    "radius_USE": 2.544,
    "mass": 222,
    "group": 18,
    "period": 6,
    "block": "p",
    "series": "noble",
    "orbitals": [
        *Xenon.orbitals,
        {
            "orbital": "5d",
            "electrons": 10
        },
        {
            "orbital": "4f",
            "electrons": 14
        },
        {
            "orbital": "6s",
            "electrons": 2
        },
        {
            "orbital": "6p",
            "electrons": 6
        }
    ],
    "electrons": 86,
    "protons": 86,
    "neutrons": 136,
    "valence": 0,
    "valence_electrons": 8,
    "electron_affinity": -0.7,
    "chemical_scale": 0.871,
    "mendeleev_universal_sequence": 11,
    "mendeleev_pettifor": 6,
    "mendeleev_modified": 6,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 2.6,
    "ionisation_energies": [
        1037
    ],
    "chemical_hardness": 10.75,
    "chemical_potential": -5.38,
    "melting_temperature": 202,
    "boiling_temperature": 211.5,
    "fusion_enthalpy": 3.247,
    "vaporisation_enthalpy": 18.1,
    "molar_heat_capacity": 20.786,
    "structure": "gas",
    "thermal_conductivity": 0.00361,
    "density": 0.00973,
    "cohesive_energy": 0.202,
})

Francium = Element(**{
    "name": "Francium",
    "symbol": "Fr",
    "periodic_number": 6,

    "radius_vanDerWaals": 3.48,
    "radius_covalent": 2.6,
    "radius_USE": 2.567,
    "mass": 223,
    "group": 1,
    "period": 7,
    "block": "s",
    "series": "alkali_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 1
        }
    ],
    "electrons": 87,
    "protons": 87,
    "neutrons": 136,
    "valence": 1,
    "valence_electrons": 1,
    "electron_affinity": 0.486,
    "chemical_scale": 0,
    "mendeleev_universal_sequence": 1,
    "mendeleev_pettifor": 7,
    "mendeleev_modified": 7,
    "electronegativity_pauling": 0.7,
    "electronegativity_allen": 0.67,
    "ionisation_energies": [
        380
    ],
    "chemical_hardness": 15.21,
    "chemical_potential": -2.28,
    "melting_temperature": 281,
    "boiling_temperature": 890,

    "structure": "A2",
    "density": 2.48,
})

Radium = Element(**{
    "name": "Radium",
    "symbol": "Ra",
    "periodic_number": 10,
    "radius_empirical": 2.15,
    "radius_vanDerWaals": 2.83,
    "radius_covalent": 2.21,
    "radius_USE": 2.114,
    "mass": 226,
    "group": 2,
    "period": 7,
    "block": "s",
    "series": "alkaline_earth_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        }
    ],
    "electrons": 88,
    "protons": 88,
    "neutrons": 138,
    "valence": 2,
    "valence_electrons": 2,
    "electron_affinity": 0.1,
    "chemical_scale": 0.486,
    "mendeleev_universal_sequence": 5,
    "mendeleev_pettifor": 13,
    "mendeleev_modified": 13,
    "electronegativity_pauling": 0.9,
    "electronegativity_allen": 0.89,
    "ionisation_energies": [
        509.3,
        979
    ],
    "chemical_hardness": 5.18,
    "chemical_potential": -2.69,
    "melting_temperature": 973,
    "boiling_temperature": 2010,
    "fusion_enthalpy": 8.5,
    "vaporisation_enthalpy": 113,

    "thermal_conductivity": 19,
    "structure": "A2",
    "density": 5.5,
    "cohesive_energy": 1.66,
    "debye_temperature": 89,
})

Actinium = Element(**{
    "name": "Actinium",
    "symbol": "Ac",
    "periodic_number": 14,
    "radius_empirical": 1.95,
    "radius_covalent": 2.15,
    "radius_USE": 1.838,
    "mass": 227,
    "group": 3,
    "period": 7,
    "block": "d",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 1
        }
    ],
    "electrons": 89,
    "protons": 89,
    "neutrons": 138,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": 0.35,
    "chemical_scale": 0.827,
    "mendeleev_universal_sequence": 8,
    "mendeleev_pettifor": 45,
    "mendeleev_modified": 33,
    "electronegativity_pauling": 1.1,
    "ionisation_energies": [
        499,
        1170
    ],
    "chemical_hardness": 4.82,
    "chemical_potential": -2.76,
    "melting_temperature": 1500,
    "boiling_temperature": 3500,
    "fusion_enthalpy": 14,
    "vaporisation_enthalpy": 400,
    "molar_heat_capacity": 27.2,

    "thermal_conductivity": 12,
    "structure": "A1",
    "density": 10.07,
    "cohesive_energy": 4.25,
    "price": 29000000000000
})

Thorium = Element(**{
    "name": "Thorium",
    "symbol": "Th",
    "periodic_number": 16,
    "radius_empirical": 1.8,
    "radius_covalent": 2.06,
    "radius_metallic": 1.79,
    "radius_USE": 1.655,
    "volume_miedema": 19.8,
    "mass": 232.0377,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 2
        }
    ],
    "electrons": 90,
    "protons": 90,
    "neutrons": 142,
    "valence": 4,
    "valence_electrons": 4,
    "electron_affinity": 0.60769,
    "wigner_seitz_electron_density": 2.1,
    "chemical_scale": 1.091,
    "mendeleev_universal_sequence": 21,
    "mendeleev_pettifor": 44,
    "mendeleev_modified": 34,
    "work_function": 3.4,
    "electronegativity_pauling": 1.3,
    "electronegativity_miedema": 3.3,
    "miedema_R": 0.7,
    "ionisation_energies": [
        587,
        1110
    ],
    "chemical_hardness": 5.94,
    "chemical_potential": -3.35,
    "melting_temperature": 2023,
    "boiling_temperature": 5061,
    "fusion_enthalpy": 13.81,
    "vaporisation_enthalpy": 514,
    "molar_heat_capacity": 26.23,

    "thermal_conductivity": 54,
    "thermal_expansion": 0.000011,
    "structure": "A1",
    "density": 11.724,
    "cohesive_energy": 6.2,
    "debye_temperature": 100,
    "price": 287
})

Protactinium = Element(**{
    "name": "Protactinium",
    "symbol": "Pa",
    "periodic_number": 18,
    "radius_empirical": 1.8,
    "radius_covalent": 2,
    "radius_metallic": 1.63,
    "radius_USE": 1.436,
    "mass": 231.03588,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 1
        },
        {
            "orbital": "5f",
            "electrons": 2
        }
    ],
    "electrons": 91,
    "protons": 91,
    "neutrons": 148,
    "valence": 5,
    "valence_electrons": 5,
    "electron_affinity": 0.55,
    "chemical_scale": 1.385,
    "mendeleev_universal_sequence": 36,
    "mendeleev_pettifor": 43,
    "mendeleev_modified": 35,
    "electronegativity_pauling": 1.5,
    "ionisation_energies": [
        568,
        1128
    ],
    "chemical_hardness": 5.51,
    "chemical_potential": -3.14,
    "melting_temperature": 1841,
    "boiling_temperature": 4300,
    "fusion_enthalpy": 12.34,
    "vaporisation_enthalpy": 481,

    "thermal_conductivity": 47,
    "thermal_expansion": 0.00001,
    "structure": "Aa",
    "density": 15.37,
    "debye_temperature": 262,
    "price": 280000
})

Uranium = Element(**{
    "name": "Uranium",
    "symbol": "U",
    "periodic_number": 20,
    "radius_empirical": 1.75,
    "radius_vanDerWaals": 1.86,
    "radius_covalent": 1.96,
    "radius_metallic": 1.56,
    "radius_USE": 1.339,
    "volume_miedema": 13.15,
    "mass": 238.02891,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 1
        },
        {
            "orbital": "5f",
            "electrons": 3
        }
    ],
    "electrons": 92,
    "protons": 92,
    "neutrons": 146,
    "valence": 6,
    "valence_electrons": 6,
    "electron_affinity": 0.53,
    "wigner_seitz_electron_density": 3.44,
    "chemical_scale": 1.397,
    "mendeleev_universal_sequence": 38,
    "mendeleev_pettifor": 42,
    "mendeleev_modified": 36,
    "work_function": 3.63,
    "electronegativity_pauling": 1.38,
    "electronegativity_miedema": 3.9,
    "miedema_R": 1.0,
    "ionisation_energies": [
        597.6,
        1420
    ],
    "chemical_hardness": 5.82,
    "chemical_potential": -3.29,
    "melting_temperature": 1405.3,
    "boiling_temperature": 4404,
    "fusion_enthalpy": 9.14,
    "vaporisation_enthalpy": 417.1,
    "molar_heat_capacity": 27.665,

    "thermal_conductivity": 27,
    "thermal_expansion": 0.0000139,
    "structure": "A20",
    "density": 19.1,
    "cohesive_energy": 5.55,
    "debye_temperature": 300,
    "price": 101
})

Neptunium = Element(**{
    "name": "Neptunium",
    "symbol": "Np",
    "periodic_number": 22,
    "radius_empirical": 1.75,
    "radius_covalent": 1.9,
    "radius_metallic": 1.55,
    "radius_USE": 1.291,
    "mass": 237,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 1
        },
        {
            "orbital": "5f",
            "electrons": 4
        }
    ],
    "electrons": 93,
    "protons": 93,
    "neutrons": 144,
    "valence": 6,
    "valence_electrons": 7,
    "electron_affinity": 0.48,
    "chemical_scale": 1.425,
    "mendeleev_universal_sequence": 41,
    "mendeleev_pettifor": 41,
    "mendeleev_modified": 37,
    "electronegativity_pauling": 1.36,
    "ionisation_energies": [
        604.5,
        1128
    ],
    "chemical_hardness": 5.95,
    "chemical_potential": -3.29,
    "melting_temperature": 912,
    "boiling_temperature": 4447,
    "fusion_enthalpy": 5.19,
    "vaporisation_enthalpy": 336,
    "molar_heat_capacity": 29.46,

    "thermal_conductivity": 6,
    "structure": "Ac",
    "density": 19.38,
    "cohesive_energy": 4.73,
    "debye_temperature": 163,
    "price": 660000
})

Plutonium = Element(**{
    "name": "Plutonium",
    "symbol": "Pu",
    "periodic_number": 24,
    "radius_empirical": 1.75,
    "radius_covalent": 1.87,
    "radius_metallic": 1.59,
    "radius_USE": 1.271,
    "volume_miedema": 12.06,
    "mass": 244,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "5f",
            "electrons": 6
        }
    ],
    "electrons": 94,
    "protons": 94,
    "neutrons": 150,
    "valence": 6,
    "valence_electrons": 8,
    "electron_affinity": -0.5,
    "wigner_seitz_electron_density": 2.99,
    "chemical_scale": 1.396,
    "mendeleev_universal_sequence": 37,
    "mendeleev_pettifor": 40,
    "mendeleev_modified": 38,
    "electronegativity_pauling": 1.28,
    "electronegativity_miedema": 3.8,
    "miedema_R": 1.0,
    "ionisation_energies": [
        584.7,
        1128
    ],
    "chemical_hardness": 5.94,
    "chemical_potential": -3.07,
    "melting_temperature": 912.5,
    "boiling_temperature": 3505,
    "fusion_enthalpy": 2.82,
    "vaporisation_enthalpy": 333.5,
    "molar_heat_capacity": 35.5,

    "thermal_conductivity": 6,
    "thermal_expansion": 0.0000467,
    "structure": "aPu",
    "density": 19.85,
    "cohesive_energy": 3.6,
    "debye_temperature": 176,
    "price": 6490000
})

Americium = Element(**{
    "name": "Americium",
    "symbol": "Am",
    "periodic_number": 26,
    "radius_empirical": 1.75,
    "radius_covalent": 1.8,
    "radius_metallic": 1.73,
    "radius_USE": 1.261,
    "mass": 243,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "5f",
            "electrons": 7
        }
    ],
    "electrons": 95,
    "protons": 95,
    "neutrons": 148,
    "valence": 4,
    "valence_electrons": 9,
    "electron_affinity": 0.1,
    "chemical_scale": 1.416,
    "mendeleev_universal_sequence": 40,
    "mendeleev_pettifor": 39,
    "mendeleev_modified": 39,
    "electronegativity_pauling": 1.3,
    "ionisation_energies": [
        578.1158
    ],
    "chemical_hardness": 5.9,
    "chemical_potential": -3.03,
    "melting_temperature": 1449,
    "boiling_temperature": 2880,
    "fusion_enthalpy": 14.39,
    "molar_heat_capacity": 28,

    "thermal_conductivity": 10,
    "structure": "A3",
    "density": 12,
    "cohesive_energy": 2.73,
    "price": 750000
})

Curium = Element(**{
    "name": "Curium",
    "symbol": "Cm",
    "periodic_number": 28,
    "radius_empirical": 1.76,
    "radius_covalent": 1.69,
    "radius_metallic": 1.74,
    "radius_USE": 1.279,
    "mass": 247,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 1
        },
        {
            "orbital": "5f",
            "electrons": 7
        }
    ],
    "electrons": 96,
    "protons": 96,
    "neutrons": 151,
    "valence": 4,
    "valence_electrons": 10,
    "electron_affinity": 0.28,
    "chemical_scale": 1.401,
    "mendeleev_universal_sequence": 39,
    "mendeleev_pettifor": 38,
    "mendeleev_modified": 40,
    "electronegativity_pauling": 1.3,
    "ionisation_energies": [
        581,
        1196
    ],
    "chemical_hardness": 5.67,
    "chemical_potential": -3.16,
    "melting_temperature": 1613,
    "boiling_temperature": 3383,
    "fusion_enthalpy": 13.85,

    "structure": "A3",
    "density": 13.51,
    "cohesive_energy": 3.99,
    "price": 160000000000
})

Berkelium = Element(**{
    "name": "Berkelium",
    "symbol": "Bk",
    "periodic_number": 30,
    "radius_metallic": 1.7,
    "mass": 247,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "5f",
            "electrons": 9
        }
    ],
    "electrons": 97,
    "protons": 97,
    "neutrons": 150,
    "valence": 4,
    "valence_electrons": 11,
    "electron_affinity": -1.72,
    "mendeleev_pettifor": 37,
    "mendeleev_modified": 41,
    "electronegativity_pauling": 1.3,
    "ionisation_energies": [
        601,
        1186
    ],
    "chemical_hardness": 6.17,
    "chemical_potential": -3.12,
    "melting_temperature": 1259,
    "boiling_temperature": 2900,
    "fusion_enthalpy": 7.92,

    "thermal_conductivity": 10,
    "structure": "A3",
    "density": 14.78,
    "price": 185000000000
})

Californium = Element(**{
    "name": "Californium",
    "symbol": "Cf",
    "periodic_number": 32,
    "radius_metallic": 1.86,
    "mass": 251,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "5f",
            "electrons": 10
        }
    ],
    "electrons": 98,
    "protons": 98,
    "neutrons": 153,
    "valence": 4,
    "valence_electrons": 12,
    "electron_affinity": -1.01,
    "mendeleev_pettifor": 36,
    "mendeleev_modified": 42,
    "electronegativity_pauling": 1.3,
    "ionisation_energies": [
        608,
        1206
    ],
    "melting_temperature": 1173,
    "boiling_temperature": 1743,

    "structure": "A3",
    "density": 15.1,
    "price": 185000000000
})

Einsteinium = Element(**{
    "name": "Einsteinium",
    "symbol": "Es",
    "periodic_number": 34,
    "radius_metallic": 1.86,
    "mass": 252,
    "group": 3,
    "period": 6,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "5f",
            "electrons": 11
        }
    ],
    "electrons": 99,
    "protons": 99,
    "neutrons": 153,
    "valence": 4,
    "valence_electrons": 13,
    "electron_affinity": -0.3,
    "mendeleev_pettifor": 35,
    "mendeleev_modified": 43,
    "electronegativity_pauling": 1.3,
    "ionisation_energies": [
        619,
        1216
    ],
    "melting_temperature": 1133,
    "boiling_temperature": 1269,

    "structure": "A1",
    "density": 8.84,
})

Fermium = Element(**{
    "name": "Fermium",
    "symbol": "Fm",
    "periodic_number": 36,
    "mass": 257,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "5f",
            "electrons": 12
        }
    ],
    "electrons": 100,
    "protons": 100,
    "neutrons": 157,
    "valence": 3,
    "valence_electrons": 14,
    "electron_affinity": 0.35,
    "mendeleev_pettifor": 34,
    "mendeleev_modified": 44,
    "electronegativity_pauling": 1.3,
    "ionisation_energies": [
        627,
        1225
    ],
    "melting_temperature": 1800,

    "structure": "A1",
    "density": 9.71,
})

Mendelevium = Element(**{
    "name": "Mendelevium",
    "symbol": "Md",
    "mass": 258,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "5f",
            "electrons": 13
        }
    ],
    "electrons": 101,
    "protons": 101,
    "neutrons": 157,
    "valence": 3,
    "valence_electrons": 15,
    "electron_affinity": 0.98,
    "electronegativity_pauling": 1.3,
    "ionisation_energies": [
        635,
        1235
    ],
    "melting_temperature": 1100,

    "structure": "A1",
    "density": 10.37,
})

Nobelium = Element(**{
    "name": "Nobelium",
    "symbol": "No",
    "mass": 259,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "5f",
            "electrons": 14
        }
    ],
    "electrons": 102,
    "protons": 102,
    "neutrons": 157,
    "valence": 3,
    "valence_electrons": 16,
    "electron_affinity": -2.33,
    "electronegativity_pauling": 1.3,
    "ionisation_energies": [
        642,
        1254
    ],
    "melting_temperature": 1100,

    "structure": "A1",
    "density": 9.94,
})

Lawrencium = Element(**{
    "name": "Lawrencium",
    "symbol": "Lr",
    "mass": 262,
    "group": 3,
    "period": 7,
    "block": "f",
    "series": "actinide",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "7p",
            "electrons": 1
        }
    ],
    "electrons": 103,
    "protons": 103,
    "neutrons": 159,
    "valence": 3,
    "valence_electrons": 3,
    "electron_affinity": -0.31,
    "ionisation_energies": [
        470,
        1428
    ],
    "melting_temperature": 1900,

    "structure": "A3",
    "density": 16,
})

Rutherfordium = Element(**{
    "name": "Rutherfordium",
    "symbol": "Rf",
    "mass": 267,
    "group": 4,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 2
        }
    ],
    "electrons": 104,
    "protons": 104,
    "neutrons": 157,
    "valence": 4,
    "valence_electrons": 4,
    "ionisation_energies": [
        580,
        1390
    ],
    "melting_temperature": 2400,
    "boiling_temperature": 5800,

    "structure": "A3",
    "density": 23.2,
})

Dubnium = Element(**{
    "name": "Dubnium",
    "symbol": "Db",
    "mass": 270,
    "group": 5,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 3
        }
    ],
    "electrons": 105,
    "protons": 105,
    "neutrons": 157,
    "valence": 5,
    "valence_electrons": 5,
    "ionisation_energies": [
        665,
        1547
    ],

    "structure": "A2",
    "density": 29.3,
})

Seaborgium = Element(**{
    "name": "Seaborgium",
    "symbol": "Sg",
    "mass": 269,
    "group": 6,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 4
        }
    ],
    "electrons": 106,
    "protons": 106,
    "neutrons": 157,
    "valence": 6,
    "valence_electrons": 6,
    "ionisation_energies": [
        757,
        1733
    ],

    "structure": "A2",
    "density": 35,
})

Bohrium = Element(**{
    "name": "Bohrium",
    "symbol": "Bh",
    "mass": 270,
    "group": 7,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 5
        }
    ],
    "electrons": 107,
    "protons": 107,
    "neutrons": 155,
    "valence": 7,
    "valence_electrons": 7,
    "ionisation_energies": [
        740,
        1690
    ],

    "structure": "A3",
    "density": 37.1,
})


Hassium = Element(**{
    "name": "Hassium",
    "symbol": "Hs",
    "mass": 270,
    "group": 8,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 6
        }
    ],
    "electrons": 108,
    "protons": 108,
    "neutrons": 157,
    "valence_electrons": 8,
    "ionisation_energies": [
        730,
        1760
    ],

    "structure": "A3",
    "density": 41,
})

Meitnerium = Element(**{
    "name": "Meitnerium",
    "symbol": "Mt",
    "mass": 278,
    "group": 9,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 7
        }
    ],
    "electrons": 109,
    "protons": 109,
    "neutrons": 157,
    "valence_electrons": 9,
    "ionisation_energies": [
        800,
        1820
    ],

    "structure": "A1",
    "density": 37.4,
})

Darmstadtium = Element(**{
    "name": "Darmstadtium",
    "symbol": "Ds",
    "mass": 281,
    "group": 10,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 1
        },
        {
            "orbital": "6d",
            "electrons": 9
        }
    ],
    "electrons": 110,
    "protons": 110,
    "neutrons": 151,
    "valence_electrons": 10,
    "ionisation_energies": [
        960,
        1890
    ],

    "structure": "A2",
    "density": 34.8,
})

Roentgenium = Element(**{
    "name": "Roentgenium",
    "symbol": "Rg",
    "mass": 281,
    "group": 11,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 1
        },
        {
            "orbital": "6d",
            "electrons": 10
        }
    ],
    "electrons": 111,
    "protons": 111,
    "neutrons": 161,
    "valence_electrons": 11,
    "electron_affinity": 1.565,
    "ionisation_energies": [
        1020,
        2070
    ],

    "structure": "A2",
    "density": 28.7,
})

Copernicium = Element(**{
    "name": "Copernicium",
    "symbol": "Cn",
    "mass": 285,
    "group": 12,
    "period": 7,
    "block": "d",
    "series": "transition_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "6d",
            "electrons": 10
        }
    ],
    "electrons": 112,
    "protons": 112,
    "neutrons": 165,
    "valence_electrons": 12,
    "ionisation_energies": [
        1155,
        2170
    ],
    "melting_temperature": 283,
    "boiling_temperature": 340,

    "structure": "A3",
    "density": 14,
})

Nihonium = Element(**{
    "name": "Nihonium",
    "symbol": "Nh",
    "mass": 286,
    "group": 13,
    "period": 7,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "6d",
            "electrons": 10
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "7p",
            "electrons": 1
        }
    ],
    "electrons": 113,
    "protons": 113,
    "neutrons": 173,
    "valence_electrons": 3,
    "electron_affinity": 0.69,
    "ionisation_energies": [
        707.2,
        2309
    ],
    "melting_temperature": 700,
    "boiling_temperature": 1430,
    "fusion_enthalpy": 7.61,
    "vaporisation_enthalpy": 130,

    "structure": "A3",
    "density": 16,
})

Flerovium = Element(**{
    "name": "Flerovium",
    "symbol": "Fl",
    "mass": 289,
    "group": 14,
    "period": 7,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "6d",
            "electrons": 10
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "7p",
            "electrons": 2
        }
    ],
    "electrons": 114,
    "protons": 114,
    "neutrons": 175,
    "valence_electrons": 4,
    "ionisation_energies": [
        832.2,
        1600
    ],
    "melting_temperature": 210,
    "vaporisation_enthalpy": 38,

    "structure": "A1",
    "density": 14,
})

Moscovium = Element(**{
    "name": "Moscovium",
    "symbol": "Mc",
    "mass": 289,
    "group": 15,
    "period": 7,
    "block": "p",
    "series": "poor_metal",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "6d",
            "electrons": 10
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "7p",
            "electrons": 3
        }
    ],
    "electrons": 115,
    "protons": 115,
    "neutrons": 174,
    "valence_electrons": 5,
    "electron_affinity": 0.366,
    "ionisation_energies": [
        538.3,
        1760
    ],
    "melting_temperature": 670,
    "boiling_temperature": 1400,
    "fusion_enthalpy": 5.9,
    "vaporisation_enthalpy": 138,

    "density": 13.5,
})

Livermorium = Element(**{
    "name": "Livermorium",
    "symbol": "Lv",
    "mass": 293,
    "group": 16,
    "period": 7,
    "block": "p",
    "series": "chalcogen",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "6d",
            "electrons": 10
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "7p",
            "electrons": 4
        }
    ],
    "electrons": 116,
    "protons": 116,
    "neutrons": 177,
    "valence_electrons": 6,
    "electron_affinity": 0.776,
    "ionisation_energies": [
        663.9,
        1330
    ],
    "melting_temperature": 700,
    "boiling_temperature": 1100,
    "fusion_enthalpy": 7.61,
    "vaporisation_enthalpy": 42,

    "density": 12.9,
})

Tennessine = Element(**{
    "name": "Tennessine",
    "symbol": "Ts",
    "mass": 293,
    "group": 17,
    "period": 7,
    "block": "p",
    "series": "halogen",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "6d",
            "electrons": 10
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "7p",
            "electrons": 5
        }
    ],
    "electrons": 117,
    "protons": 117,
    "neutrons": 176,
    "valence_electrons": 7,
    "electron_affinity": 1.719,
    "ionisation_energies": [
        736.9,
        1435.4
    ],
    "melting_temperature": 700,
    "boiling_temperature": 883,

    "density": 7.2,
})

Oganesson = Element(**{
    "name": "Oganesson",
    "symbol": "Og",
    "mass": 295,
    "group": 18,
    "period": 7,
    "block": "p",
    "series": "noble",
    "orbitals": [
        *Radon.orbitals,
        {
            "orbital": "5f",
            "electrons": 14
        },
        {
            "orbital": "6d",
            "electrons": 10
        },
        {
            "orbital": "7s",
            "electrons": 2
        },
        {
            "orbital": "7p",
            "electrons": 6
        }
    ],
    "electrons": 118,
    "protons": 118,
    "neutrons": 176,
    "valence_electrons": 8,
    "electron_affinity": 0.056,
    "ionisation_energies": [
        860.1,
        1560
    ],
    "melting_temperature": 325,
    "boiling_temperature": 450,
    "fusion_enthalpy": 23.5,
    "vaporisation_enthalpy": 19.4,
    "structure": "A1",
    "density": 5,
})

ELEMENTS = [
    Hydrogen,
    Helium,
    Lithium,
    Berylium,
    Boron,
    Carbon,
    Nitrogen,
    Oxygen,
    Fluorine,
    Neon,
    Sodium,
    Magnesium,
    Aluminium,
    Silicon,
    Phosphorus,
    Sulfur,
    Chlorine,
    Argon,
    Potassium,
    Calcium,
    Scandium,
    Titanium,
    Vanadium,
    Chromium,
    Manganese,
    Iron,
    Cobalt,
    Nickel,
    Copper,
    Zinc,
    Gallium,
    Germanium,
    Arsenic,
    Selenium,
    Bromine,
    Krypton,
    Rubidium,
    Strontium,
    Yttrium,
    Zirconium,
    Niobium,
    Molybdenum,
    Technetium,
    Ruthenium,
    Rhodium,
    Palladium,
    Silver,
    Cadmium,
    Indium,
    Tin,
    Antimony,
    Tellurium,
    Iodine,
    Xenon,
    Caesium,
    Barium,
    Lanthanum,
    Cerium,
    Praseodymium,
    Neodymium,
    Promethium,
    Samarium,
    Europium,
    Gadolinium,
    Terbium,
    Dysprosium,
    Holmium,
    Erbium,
    Thulium,
    Ytterbium,
    Lutetium,
    Hafnium,
    Tantalum,
    Tungsten,
    Rhenium,
    Osmium,
    Iridium,
    Platinum,
    Gold,
    Mercury,
    Thallium,
    Lead,
    Bismuth,
    Polonium,
    Astatine,
    Radon,
    Francium,
    Radium,
    Actinium,
    Thorium,
    Protactinium,
    Uranium,
    Neptunium,
    Plutonium,
    Americium,
    Curium,
    Berkelium,
    Californium,
    Einsteinium,
    Fermium,
    Mendelevium,
    Nobelium,
    Lawrencium,
    Rutherfordium,
    Dubnium,
    Seaborgium,
    Bohrium,
    Hassium,
    Meitnerium,
    Darmstadtium,
    Roentgenium,
    Copernicium,
    Nihonium,
    Flerovium,
    Moscovium,
    Livermorium,
    Tennessine,
    Oganesson
]


def get_elements():
    return ELEMENTS
