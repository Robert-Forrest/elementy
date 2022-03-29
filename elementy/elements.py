from elementy.element import Element

Hydrogen = Element(**{
    "name": "Hydrogen",
    "symbol": "H",
    "atomicNumber": 1,
    "periodicNumber": 89,
    "radius_empirical": 0.25,
    "radius_calculated": 0.53,
    "radius_radius_vanDerWaals": 1.2,
    "radius_radius_covalent": 0.31,
    "radius_radius_USE": 0.727,
    "mass": 1.008,
    "group": 1,
    "period": 1,
    "block": "s",
    "series": "nonMetal",
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
    "valenceElectrons": 1,
    "electronAffinity": 0.754195,
    "wignerSeitzElectronDensity": 3.38,
    "chemicalScale": 2.366,
    "mendeleev_universalSequence": 90,
    "mendeleev_pettifor": 100,
    "mendeleev_modified": 100,
    "workFunction": None,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 2.3,
    "ionisationEnergies": [
        1312
    ],
    "chemicalHardness": 12.84,
    "chemicalPotential": -7.18,
    "meltingTemperature": 13.99,
    "boilingTemperature": 20.271,
    "fusionEnthalpy": 0.117,
    "vaporisationEnthalpy": 0.904,
    "molarHeatCapacity": 28.836,
    "phase": "gas",
    "thermalConductivity": 0.1805,
    "thermalExpansion": None,
    "density": 0.00008988,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": 1.39
})

Helium = Element(**{
    "name": "Helium",
    "symbol": "He",
    "atomicNumber": 2,
    "periodicNumber": 95,
    "radius_empirical": 1.2,
    "radius_calculated": 0.31,
    "radius_radius_vanDerWaals": 1.4,
    "radius_radius_covalent": 0.28,
    "radius_radius_USE": 1.286,
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
    "valenceElectrons": 8,
    "electronAffinity": -0.52,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 2.418,
    "mendeleev_universalSequence": 92,
    "mendeleev_pettifor": 1,
    "mendeleev_modified": 1,
    "workFunction": None,
    "electronegativity_pauling": 3.1,
    "electronegativity_allen": 4.16,
    "ionisationEnergies": [
        2372.3,
        5250.5
    ],
    "chemicalHardness": 24.59,
    "chemicalPotential": -12.29,
    "meltingTemperature": 0.95,
    "boilingTemperature": 4.222,
    "fusionEnthalpy": 0.0138,
    "vaporisationEnthalpy": 0.0829,
    "molarHeatCapacity": 20.78,
    "phase": "gas",
    "thermalConductivity": 0.1513,
    "thermalExpansion": None,
    "density": 0.0001785,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": 24
})

Lithium = Element(**{
    "name": "Lithium",
    "symbol": "Li",
    "atomicNumber": 3,
    "periodicNumber": 1,
    "radius_empirical": 1.45,
    "radius_calculated": 1.67,
    "radius_vanDerWaals": 1.82,
    "radius_covalent": 1.28,
    "radius_metallic": 1.52,
    "radius_USE": 1.374, "mass": 6.94,
    "group": 1,
    "period": 2,
    "block": "s",
    "series": "alkaliMetal",
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
    "valenceElectrons": 1,
    "electronAffinity": 0.618049,
    "wignerSeitzElectronDensity": 0.94,
    "chemicalScale": 1.141,
    "mendeleev_universalSequence": 26,
    "mendeleev_pettifor": 12,
    "mendeleev_modified": 12,
    "workFunction": 2.93,
    "electronegativity_pauling": 0.98,
    "electronegativity_allen": 0.912,
    "ionisationEnergies": [
        520.2,
        7298.1
    ],
    "chemicalHardness": 4.77,
    "chemicalPotential": -3,
    "meltingTemperature": 453.65,
    "boilingTemperature": 1603,
    "fusionEnthalpy": 3,
    "vaporisationEnthalpy": 136,
    "molarHeatCapacity": 24.86,
    "phase": "solid",
    "thermalConductivity": 85,
    "thermalExpansion": 0.000046,
    "crystalStructure": "A2",
    "density": 0.535,
    "cohesiveEnergy": 1.63,
    "debyeTemperature": 448,
    "price": 85.6
})

Berylium = Element(**{
    "name": "Berylium",
    "symbol": "Be",
    "atomicNumber": 4,
    "periodicNumber": 64,
    "radius_empirical": 1.05,
    "radius_calculated": 1.12,
    "radius_vanDerWaals": 1.53,
    "radius_covalent": 0.96,
    "radius_metallic": 1.12,
    "radius_USE": 1.09,
    "mass": 9.0121831,
    "group": 2,
    "period": 2,
    "block": "s",
    "series": "alkalineEarthMetal",
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
    "valenceElectrons": 2,
    "electronAffinity": -0.52,
    "wignerSeitzElectronDensity": 4.66,
    "chemicalScale": 1.71,
    "mendeleev_universalSequence": 62,
    "mendeleev_pettifor": 74,
    "mendeleev_modified": 74,
    "workFunction": 4.98,
    "electronegativity_pauling": 1.57,
    "electronegativity_allen": 1.576,
    "ionisationEnergies": [
        899.5,
        1757.1
    ],
    "chemicalHardness": 9.32,
    "chemicalPotential": -4.66,
    "meltingTemperature": 1560,
    "boilingTemperature": 2742,
    "fusionEnthalpy": 12.2,
    "vaporisationEnthalpy": 292,
    "molarHeatCapacity": 16.443,
    "phase": "solid",
    "thermalConductivity": 190,
    "thermalExpansion": 0.0000113,
    "crystalStructure": "A3",
    "density": 1.848,
    "cohesiveEnergy": 3.32,
    "debyeTemperature": 1031,
    "price": 857
})

Boron = Element(**{
    "name": "Boron",
    "symbol": "B",
    "atomicNumber": 5,
    "periodicNumber": 69,
    "radius_empirical": 0.85,
    "radius_calculated": 0.87,
    "radius_vanDerWaals": 1.92,
    "radius_covalent": 0.85,
    "radius_USE": 0.933,
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
    "valenceElectrons": 3,
    "electronAffinity": 0.279723,
    "wignerSeitzElectronDensity": 5.36,
    "chemicalScale": 2.106,
    "mendeleev_universalSequence": 86,
    "mendeleev_pettifor": 83,
    "mendeleev_modified": 83,
    "workFunction": 4.45,
    "electronegativity_pauling": 2.04,
    "electronegativity_allen": 2.051,
    "ionisationEnergies": [
        800.6,
        2427.1
    ],
    "chemicalHardness": 8.02,
    "chemicalPotential": -4.29,
    "meltingTemperature": 2349,
    "boilingTemperature": 4200,
    "fusionEnthalpy": 50.2,
    "vaporisationEnthalpy": 508,
    "molarHeatCapacity": 11.087,
    "phase": "solid",
    "thermalConductivity": 27,
    "thermalExpansion": 0.000006,
    "crystalStructure": "R105",
    "density": 2.46,
    "cohesiveEnergy": 5.81,
    "debyeTemperature": 1362,
    "price": 3.68
})

Carbon = Element(**{
    "name": "Carbon",
    "symbol": "C",
    "atomicNumber": 6,
    "periodicNumber": 74,
    "radius_empirical": 0.7,
    "radius_calculated": 0.67,
    "radius_vanDerWaals": 1.7,
    "radius_covalent": 0.76,
    "radius_USE": 0.891,
    "mass": 12.011,
    "group": 14,
    "period": 2,
    "block": "p",
    "series": "nonMetal",
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
    "valenceElectrons": 4,
    "electronAffinity": 1.2621226,
    "wignerSeitzElectronDensity": 5.55,
    "chemicalScale": 2.43,
    "mendeleev_universalSequence": 93,
    "mendeleev_pettifor": 92,
    "mendeleev_modified": 84,
    "workFunction": 5,
    "electronegativity_pauling": 2.55,
    "electronegativity_allen": 2.544,
    "ionisationEnergies": [
        1086.5,
        2352.6
    ],
    "chemicalHardness": 10,
    "chemicalPotential": -6.26,
    "meltingTemperature": 3823.15,
    "boilingTemperature": 4300.15,
    "fusionEnthalpy": 117,
    "vaporisationEnthalpy": 355.08,
    "molarHeatCapacity": 8.517,
    "phase": "solid",
    "thermalConductivity": 140,
    "thermalExpansion": 0.0000071,
    "crystalStructure": "Af",
    "density": 2.26,
    "cohesiveEnergy": 7.37,
    "debyeTemperature": 1550,
    "price": 0.122
})

Nitrogen = Element(**{
    "name": "Nitrogen",
    "symbol": "N",
    "atomicNumber": 7,
    "periodicNumber": 79,
    "radius_empirical": 0.65,
    "radius_calculated": 0.56,
    "radius_vanDerWaals": 1.55,
    "radius_covalent": 0.71,
    "radius_USE": 0.932,
    "mass": 14.007,
    "group": 15,
    "period": 2,
    "block": "p",
    "series": "nonMetal",
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
    "valenceElectrons": 5,
    "electronAffinity": -0.07,
    "wignerSeitzElectronDensity": 4.49,
    "chemicalScale": 2.675,
    "mendeleev_universalSequence": 94,
    "mendeleev_pettifor": 97,
    "mendeleev_modified": 85,
    "workFunction": None,
    "electronegativity_pauling": 3.04,
    "electronegativity_allen": 3.066,
    "ionisationEnergies": [
        1402.3,
        2856
    ],
    "chemicalHardness": 14.53,
    "chemicalPotential": -7.27,
    "meltingTemperature": 63.23,
    "boilingTemperature": 77.355,
    "fusionEnthalpy": 0.72,
    "vaporisationEnthalpy": 5.56,
    "molarHeatCapacity": 29.124,
    "phase": "gas",
    "thermalConductivity": 0.02583,
    "thermalExpansion": None,
    "density": 0.0012506,
    "cohesiveEnergy": 4.92,
    "debyeTemperature": None,
    "price": 0.14
})

Oxygen = Element(**{
    "name": "Oxygen",
    "symbol": "O",
    "atomicNumber": 8,
    "periodicNumber": 84,
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
    "valenceElectrons": 6,
    "electronAffinity": 1.4611136,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 2.849,
    "mendeleev_universalSequence": 95,
    "mendeleev_pettifor": 98,
    "mendeleev_modified": 94,
    "workFunction": None,
    "electronegativity_pauling": 3.44,
    "electronegativity_allen": 3.61,
    "ionisationEnergies": [
        1313.9,
        3388.3
    ],
    "chemicalHardness": 12.16,
    "chemicalPotential": -7.54,
    "meltingTemperature": 54.36,
    "boilingTemperature": 90.188,
    "fusionEnthalpy": 0.444,
    "vaporisationEnthalpy": 6.82,
    "molarHeatCapacity": 29.378,
    "phase": "gas",
    "thermalConductivity": 0.02658,
    "thermalExpansion": None,
    "density": 0.001429,
    "cohesiveEnergy": 2.6,
    "debyeTemperature": None,
    "price": 0.154
})

Fluorine = Element(**{
    "name": "Fluorine",
    "symbol": "F",
    "atomicNumber": 9,
    "periodicNumber": 90,
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
    "valenceElectrons": 7,
    "electronAffinity": 3.4011898,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 3.08,
    "mendeleev_universalSequence": 96,
    "mendeleev_pettifor": 99,
    "mendeleev_modified": 99,
    "workFunction": None,
    "electronegativity_pauling": 3.98,
    "electronegativity_allen": 4.193,
    "ionisationEnergies": [
        1681,
        3374.2
    ],
    "chemicalHardness": 14.02,
    "chemicalPotential": -10.41,
    "meltingTemperature": 53.48,
    "boilingTemperature": 85.03,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": 6.51,
    "molarHeatCapacity": 31,
    "phase": "gas",
    "thermalConductivity": 0.0277,
    "thermalExpansion": None,
    "density": 0.001696,
    "cohesiveEnergy": 0.84,
    "debyeTemperature": None,
    "price": 2.16
})

Neon = Element(**{
    "name": "Neon",
    "symbol": "Ne",
    "atomicNumber": 10,
    "periodicNumber": 96,
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
    "valenceElectrons": 8,
    "electronAffinity": -1.22,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 2.373,
    "mendeleev_universalSequence": 91,
    "mendeleev_pettifor": 2,
    "mendeleev_modified": 2,
    "workFunction": None,
    "electronegativity_pauling": 3.2,
    "electronegativity_allen": 4.787,
    "ionisationEnergies": [
        2080.7,
        3952.3
    ],
    "chemicalHardness": 21.56,
    "chemicalPotential": -10.78,
    "meltingTemperature": 24.56,
    "boilingTemperature": 27.104,
    "fusionEnthalpy": 0.335,
    "vaporisationEnthalpy": 1.71,
    "molarHeatCapacity": 20.79,
    "phase": "gas",
    "thermalConductivity": 0.0491,
    "thermalExpansion": None,
    "density": 0.0008999,
    "cohesiveEnergy": 0.02,
    "debyeTemperature": None,
    "price": 240
})

Sodium = Element(**{
    "name": "Sodium",
    "symbol": "Na",
    "atomicNumber": 11,
    "periodicNumber": 2,
    "radius_empirical": 1.8,
    "radius_calculated": 1.9,
    "radius_vanDerWaals": 2.27,
    "radius_covalent": 1.66,
    "radius_metallic": 1.86,
    "radius_USE": 1.701,
    "mass": 22.98976928,
    "group": 1,
    "period": 3,
    "block": "s",
    "series": "alkaliMetal",
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
    "valenceElectrons": 1,
    "electronAffinity": 0.547926,
    "wignerSeitzElectronDensity": 0.55,
    "chemicalScale": 0.843,
    "mendeleev_universalSequence": 10,
    "mendeleev_pettifor": 11,
    "mendeleev_modified": 11,
    "workFunction": 2.36,
    "electronegativity_pauling": 0.93,
    "electronegativity_allen": 0.869,
    "ionisationEnergies": [
        495.8,
        4562
    ],
    "chemicalHardness": 4.59,
    "chemicalPotential": -2.84,
    "meltingTemperature": 370.944,
    "boilingTemperature": 1156.09,
    "fusionEnthalpy": 2.6,
    "vaporisationEnthalpy": 97.42,
    "molarHeatCapacity": 28.23,
    "phase": "solid",
    "thermalConductivity": 140,
    "thermalExpansion": 0.00007,
    "crystalStructure": "A2",
    "density": 0.968,
    "cohesiveEnergy": 1.113,
    "debyeTemperature": 155,
    "price": 3.43
})

Magnesium = Element(**{
    "name": "Magnesium",
    "symbol": "Mg",
    "atomicNumber": 12,
    "periodicNumber": 65,
    "radius_empirical": 1.5,
    "radius_calculated": 1.45,
    "radius_vanDerWaals": 1.73,
    "radius_covalent": 1.41,
    "radius_metallic": 1.6,
    "radius_USE": 1.508,
    "mass": 24.305,
    "group": 2,
    "period": 3,
    "block": "s",
    "series": "alkalineEarthMetal",
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
    "valenceElectrons": 2,
    "electronAffinity": -0.42,
    "wignerSeitzElectronDensity": 1.6,
    "chemicalScale": 1.218,
    "mendeleev_universalSequence": 28,
    "mendeleev_pettifor": 70,
    "mendeleev_modified": 70,
    "workFunction": 3.66,
    "electronegativity_pauling": 1.31,
    "electronegativity_allen": 1.293,
    "ionisationEnergies": [
        737.7,
        1450.7
    ],
    "chemicalHardness": 7.65,
    "chemicalPotential": -3.82,
    "meltingTemperature": 923,
    "boilingTemperature": 1363,
    "fusionEnthalpy": 8.48,
    "vaporisationEnthalpy": 128,
    "molarHeatCapacity": 24.869,
    "phase": "solid",
    "thermalConductivity": 160,
    "thermalExpansion": 0.0000248,
    "crystalStructure": "A3",
    "density": 1.738,
    "cohesiveEnergy": 1.51,
    "debyeTemperature": 330,
    "price": 2.32
})

Aluminium = Element(**{
    "name": "Aluminium",
    "symbol": "Al",
    "atomicNumber": 13,
    "periodicNumber": 70,
    "radius_empirical": 1.25,
    "radius_calculated": 1.18,
    "radius_vanDerWaals": 1.84,
    "radius_covalent": 1.21,
    "radius_metallic": 1.43,
    "radius_USE": 1.355,
    "mass": 26.9815385,
    "group": 13,
    "period": 3,
    "block": "p",
    "series": "poorMetal",
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
    "valenceElectrons": 3,
    "electronAffinity": 0.43283,
    "wignerSeitzElectronDensity": 2.7,
    "chemicalScale": 1.514,
    "mendeleev_universalSequence": 50,
    "mendeleev_pettifor": 77,
    "mendeleev_modified": 75,
    "workFunction": 4.2,
    "electronegativity_pauling": 1.61,
    "electronegativity_allen": 1.613,
    "ionisationEnergies": [
        577.5,
        1816.7
    ],
    "chemicalHardness": 5.55,
    "chemicalPotential": -3.21,
    "meltingTemperature": 933.47,
    "boilingTemperature": 2743,
    "fusionEnthalpy": 10.71,
    "vaporisationEnthalpy": 284,
    "molarHeatCapacity": 24.2,
    "phase": "solid",
    "thermalConductivity": 235,
    "thermalExpansion": 0.0000231,
    "crystalStructure": "A1",
    "density": 2.7,
    "cohesiveEnergy": 3.39,
    "debyeTemperature": 390,
    "price": 1.79
})

Silicon = Element(**{
    "name": "Silicon",
    "symbol": "Si",
    "atomicNumber": 14,
    "periodicNumber": 75,
    "radius_empirical": 1.1,
    "radius_calculated": 1.11,
    "radius_vanDerWaals": 2.1,
    "radius_covalent": 1.11,
    "radius_metallic": 1.43,
    "radius_USE": 1.269,
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
    "valenceElectrons": 4,
    "electronAffinity": 1.3895212,
    "wignerSeitzElectronDensity": 3.38,
    "chemicalScale": 1.75,
    "mendeleev_universalSequence": 66,
    "mendeleev_pettifor": 82,
    "mendeleev_modified": 82,
    "workFunction": 4.85,
    "electronegativity_pauling": 1.9,
    "electronegativity_allen": 1.916,
    "ionisationEnergies": [
        786.5,
        1577.1
    ],
    "chemicalHardness": 6.76,
    "chemicalPotential": -4.77,
    "meltingTemperature": 1687,
    "boilingTemperature": 3538,
    "fusionEnthalpy": 50.21,
    "vaporisationEnthalpy": 383,
    "molarHeatCapacity": 19.789,
    "phase": "solid",
    "thermalConductivity": 150,
    "thermalExpansion": 0.0000026,
    "crystalStructure": "A4",
    "density": 2.329,
    "cohesiveEnergy": 4.63,
    "debyeTemperature": 692,
    "price": 1.7
})

Phosphorus = Element(**{
    "name": "Phosphorus",
    "symbol": "P",
    "atomicNumber": 15,
    "periodicNumber": 80,
    "radius_empirical": 1,
    "radius_calculated": 0.98,
    "radius_vanDerWaals": 1.8,
    "radius_covalent": 1.07,
    "radius_USE": 1.223,
    "mass": 30.973761998,
    "group": 15,
    "period": 3,
    "block": "p",
    "series": "nonMetal",
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
    "valenceElectrons": 5,
    "electronAffinity": 0.746607,
    "wignerSeitzElectronDensity": 4.49,
    "chemicalScale": 1.953,
    "mendeleev_universalSequence": 81,
    "mendeleev_pettifor": 87,
    "mendeleev_modified": 86,
    "workFunction": 4.5,
    "electronegativity_pauling": 2.19,
    "electronegativity_allen": 2.253,
    "ionisationEnergies": [
        1011.8,
        1907
    ],
    "chemicalHardness": 9.74,
    "chemicalPotential": -5.62,
    "meltingTemperature": 317.3,
    "boilingTemperature": 317.3,
    "fusionEnthalpy": 0.66,
    "vaporisationEnthalpy": 51.9,
    "molarHeatCapacity": 23.824,
    "phase": "solid",
    "thermalConductivity": 0.236,
    "thermalExpansion": 0.000127,
    "crystalStructure": "A2",
    "density": 1.823,
    "cohesiveEnergy": 3.43,
    "debyeTemperature": 576,
    "price": 2.69
})

Sulfur = Element(**{
    "name": "Sulfur",
    "symbol": "S",
    "atomicNumber": 16,
    "periodicNumber": 85,
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
    "valenceElectrons": 6,
    "electronAffinity": 2.077104,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 2.116,
    "mendeleev_universalSequence": 87,
    "mendeleev_pettifor": 91,
    "mendeleev_modified": 93,
    "workFunction": None,
    "electronegativity_pauling": 2.58,
    "electronegativity_allen": 2.589,
    "ionisationEnergies": [
        999.6,
        2252
    ],
    "chemicalHardness": 8.28,
    "chemicalPotential": -6.22,
    "meltingTemperature": 388.36,
    "boilingTemperature": 717.8,
    "fusionEnthalpy": 1.727,
    "vaporisationEnthalpy": 45,
    "molarHeatCapacity": 22.75,
    "phase": "solid",
    "thermalConductivity": 0.205,
    "thermalExpansion": None,
    "crystalStructure": "A17",
    "density": 2.07,
    "cohesiveEnergy": 2.85,
    "debyeTemperature": 527,
    "price": 0.0926
})

Chlorine = Element(**{
    "name": "Chlorine",
    "symbol": "Cl",
    "atomicNumber": 17,
    "periodicNumber": 91,
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
    "valenceElectrons": 7,
    "electronAffinity": 3.612725,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 2.332,
    "mendeleev_universalSequence": 89,
    "mendeleev_pettifor": 96,
    "mendeleev_modified": 98,
    "workFunction": None,
    "electronegativity_pauling": 3.16,
    "electronegativity_allen": 2.869,
    "ionisationEnergies": [
        1251.2,
        2298
    ],
    "chemicalHardness": 9.35,
    "chemicalPotential": -8.29,
    "meltingTemperature": 171.6,
    "boilingTemperature": 239.11,
    "fusionEnthalpy": 6.406,
    "vaporisationEnthalpy": 20.41,
    "molarHeatCapacity": 33.949,
    "phase": "gas",
    "thermalConductivity": 0.0089,
    "thermalExpansion": None,
    "density": 0.003214,
    "cohesiveEnergy": 1.4,
    "debyeTemperature": None,
    "price": 0.082
})

Argon = Element(**{
    "name": "Argon",
    "symbol": "Ar",
    "atomicNumber": 18,
    "periodicNumber": 97,
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
    "valenceElectrons": 8,
    "electronAffinity": -1,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.885,
    "mendeleev_universalSequence": 75,
    "mendeleev_pettifor": 3,
    "mendeleev_modified": 3,
    "workFunction": None,
    "electronegativity_pauling": 3.1,
    "electronegativity_allen": 3.242,
    "ionisationEnergies": [
        1520.6,
        2665.8
    ],
    "chemicalHardness": 15.76,
    "chemicalPotential": -7.88,
    "meltingTemperature": 83.81,
    "boilingTemperature": 87.302,
    "fusionEnthalpy": 1.18,
    "vaporisationEnthalpy": 6.53,
    "molarHeatCapacity": 20.85,
    "phase": "gas",
    "thermalConductivity": 0.01772,
    "thermalExpansion": None,
    "density": 0.0017837,
    "cohesiveEnergy": 0.08,
    "debyeTemperature": None,
    "price": 0.931
})

Potassium = Element(**{
    "name": "Potassium",
    "symbol": "K",
    "atomicNumber": 19,
    "periodicNumber": 3,
    "radius_empirical": 2.2,
    "radius_calculated": 2.43,
    "radius_vanDerWaals": 2.75,
    "radius_covalent": 2.03,
    "radius_metallic": 2.27,
    "radius_USE": 2.151,
    "mass": 39.0983,
    "group": 1,
    "period": 4,
    "block": "s",
    "series": "alkaliMetal",
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
    "valenceElectrons": 1,
    "electronAffinity": 0.501459,
    "wignerSeitzElectronDensity": 0.27,
    "chemicalScale": 0.411,
    "mendeleev_universalSequence": 4,
    "mendeleev_pettifor": 10,
    "mendeleev_modified": 10,
    "workFunction": 2.29,
    "electronegativity_pauling": 0.82,
    "electronegativity_allen": 0.734,
    "ionisationEnergies": [
        418.8,
        3052
    ],
    "chemicalHardness": 3.84,
    "chemicalPotential": -2.42,
    "meltingTemperature": 336.7,
    "boilingTemperature": 1032,
    "fusionEnthalpy": 2.33,
    "vaporisationEnthalpy": 76.9,
    "molarHeatCapacity": 29.6,
    "phase": "solid",
    "thermalConductivity": 100,
    "thermalExpansion": 0.000083,
    "crystalStructure": "A2",
    "density": 0.89,
    "cohesiveEnergy": 0.934,
    "debyeTemperature": 100,
    "price": 13.6
})

Calcium = Element(**{
    "name": "Calcium",
    "symbol": "Ca",
    "atomicNumber": 20,
    "periodicNumber": 7,
    "radius_empirical": 1.8,
    "radius_calculated": 1.94,
    "radius_vanDerWaals": 2.31,
    "radius_covalent": 1.76,
    "radius_metallic": 1.97,
    "radius_USE": 1.761,
    "mass": 40.078,
    "group": 2,
    "period": 4,
    "block": "s",
    "series": "alkalineEarthMetal",
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
    "valenceElectrons": 2,
    "electronAffinity": 0.02455,
    "wignerSeitzElectronDensity": 0.75,
    "chemicalScale": 0.834,
    "mendeleev_universalSequence": 9,
    "mendeleev_pettifor": 16,
    "mendeleev_modified": 16,
    "workFunction": 2.87,
    "electronegativity_pauling": 1,
    "electronegativity_allen": 1.034,
    "ionisationEnergies": [
        589.8,
        1145.4
    ],
    "chemicalHardness": 6.09,
    "chemicalPotential": -3.07,
    "meltingTemperature": 1115,
    "boilingTemperature": 1757,
    "fusionEnthalpy": 8.54,
    "vaporisationEnthalpy": 154.7,
    "molarHeatCapacity": 25.929,
    "phase": "solid",
    "thermalConductivity": 200,
    "thermalExpansion": 0.0000223,
    "crystalStructure": "A1",
    "density": 1.55,
    "cohesiveEnergy": 1.84,
    "debyeTemperature": 230,
    "price": 2.35
})

Scandium = Element(**{
    "name": "Scandium",
    "symbol": "Sc",
    "atomicNumber": 21,
    "periodicNumber": 11,
    "radius_empirical": 1.6,
    "radius_calculated": 1.84,
    "radius_vanDerWaals": 2.11,
    "radius_covalent": 1.7,
    "radius_metallic": 1.62,
    "radius_USE": 1.466,
    "mass": 44.955908,
    "group": 3,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 3,
    "electronAffinity": 0.188,
    "wignerSeitzElectronDensity": 2.05,
    "chemicalScale": 1.281,
    "mendeleev_universalSequence": 34,
    "mendeleev_pettifor": 20,
    "mendeleev_modified": 45,
    "workFunction": 3.5,
    "electronegativity_pauling": 1.36,
    "electronegativity_allen": 1.19,
    "ionisationEnergies": [
        633.1,
        1235
    ],
    "chemicalHardness": 6.37,
    "chemicalPotential": -3.38,
    "meltingTemperature": 1814,
    "boilingTemperature": 3109,
    "fusionEnthalpy": 14.1,
    "vaporisationEnthalpy": 332.7,
    "molarHeatCapacity": 25.52,
    "phase": "solid",
    "thermalConductivity": 16,
    "thermalExpansion": 0.0000102,
    "crystalStructure": "A3",
    "density": 2.985,
    "cohesiveEnergy": 3.9,
    "debyeTemperature": 476,
    "price": 3460
})

Titanium = Element(**{
    "name": "Titanium",
    "symbol": "Ti",
    "atomicNumber": 22,
    "periodicNumber": 40,
    "radius_empirical": 1.4,
    "radius_calculated": 1.76,
    "radius_covalent": 1.6,
    "radius_metallic": 1.47,
    "radius_USE": 1.308,
    "mass": 47.867,
    "group": 4,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 4,
    "electronAffinity": 0.07554,
    "wignerSeitzElectronDensity": 3.51,
    "chemicalScale": 1.513,
    "mendeleev_universalSequence": 49,
    "mendeleev_pettifor": 48,
    "mendeleev_modified": 48,
    "workFunction": 4.33,
    "electronegativity_pauling": 1.54,
    "electronegativity_allen": 1.38,
    "ionisationEnergies": [
        658.8,
        1309.8
    ],
    "chemicalHardness": 6.75,
    "chemicalPotential": -3.45,
    "meltingTemperature": 1941,
    "boilingTemperature": 3560,
    "fusionEnthalpy": 14.15,
    "vaporisationEnthalpy": 425,
    "molarHeatCapacity": 25.06,
    "phase": "solid",
    "thermalConductivity": 22,
    "thermalExpansion": 0.0000086,
    "crystalStructure": "A3",
    "density": 4.506,
    "cohesiveEnergy": 4.85,
    "debyeTemperature": 380,
    "price": 11.7
})

Vanadium = Element(**{
    "name": "Vanadium",
    "symbol": "V",
    "atomicNumber": 23,
    "periodicNumber": 43,
    "radius_empirical": 1.35,
    "radius_calculated": 1.71,
    "radius_covalent": 1.53,
    "radius_metallic": 1.34,
    "radius_USE": 1.209,
    "mass": 50.9415,
    "group": 5,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 5,
    "electronAffinity": 0.52766,
    "wignerSeitzElectronDensity": 4.41,
    "chemicalScale": 1.646,
    "mendeleev_universalSequence": 58,
    "mendeleev_pettifor": 51,
    "mendeleev_modified": 51,
    "workFunction": 4.3,
    "electronegativity_pauling": 1.63,
    "electronegativity_allen": 1.53,
    "ionisationEnergies": [
        650.9,
        1414
    ],
    "chemicalHardness": 6.22,
    "chemicalPotential": -3.64,
    "meltingTemperature": 2183,
    "boilingTemperature": 3680,
    "fusionEnthalpy": 21.5,
    "vaporisationEnthalpy": 444,
    "molarHeatCapacity": 24.89,
    "phase": "solid",
    "thermalConductivity": 31,
    "thermalExpansion": 0.0000084,
    "crystalStructure": "A2",
    "density": 6.11,
    "cohesiveEnergy": 5.31,
    "debyeTemperature": 390,
    "price": 385
})

Chromium = Element(**{
    "name": "Chromium",
    "symbol": "Cr",
    "atomicNumber": 24,
    "periodicNumber": 46,
    "radius_empirical": 1.4,
    "radius_calculated": 1.66,
    "radius_covalent": 1.39,
    "radius_metallic": 1.28,
    "radius_USE": 1.162,
    "mass": 51.9961,
    "group": 6,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 6,
    "electronAffinity": 0.67584,
    "wignerSeitzElectronDensity": 5.18,
    "chemicalScale": 1.702,
    "mendeleev_universalSequence": 61,
    "mendeleev_pettifor": 54,
    "mendeleev_modified": 52,
    "workFunction": 4.5,
    "electronegativity_pauling": 1.66,
    "electronegativity_allen": 1.65,
    "ionisationEnergies": [
        652.9,
        1590.6
    ],
    "chemicalHardness": 6.09,
    "chemicalPotential": -3.72,
    "meltingTemperature": 2180,
    "boilingTemperature": 2944,
    "fusionEnthalpy": 21,
    "vaporisationEnthalpy": 347,
    "molarHeatCapacity": 23.35,
    "phase": "solid",
    "thermalConductivity": 94,
    "thermalExpansion": 0.0000049,
    "crystalStructure": "A2",
    "density": 7.19,
    "cohesiveEnergy": 4.1,
    "debyeTemperature": 424,
    "price": 9.4
})

Manganese = Element(**{
    "name": "Manganese",
    "symbol": "Mn",
    "atomicNumber": 25,
    "periodicNumber": 49,
    "radius_empirical": 1.4,
    "radius_calculated": 1.61,
    "radius_covalent": 1.39,
    "radius_metallic": 1.27,
    "radius_USE": 1.136,
    "mass": 54.938044,
    "group": 7,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 7,
    "electronAffinity": -0.5,
    "wignerSeitzElectronDensity": 4.17,
    "chemicalScale": 1.661,
    "mendeleev_universalSequence": 59,
    "mendeleev_pettifor": 57,
    "mendeleev_modified": 69,
    "workFunction": 4.1,
    "electronegativity_pauling": 1.55,
    "electronegativity_allen": 1.75,
    "ionisationEnergies": [
        717.3,
        1509
    ],
    "chemicalHardness": 7.43,
    "chemicalPotential": -3.72,
    "meltingTemperature": 1519,
    "boilingTemperature": 2334,
    "fusionEnthalpy": 12.91,
    "vaporisationEnthalpy": 221,
    "molarHeatCapacity": 26.32,
    "phase": "solid",
    "thermalConductivity": 7.7,
    "thermalExpansion": 0.0000217,
    "crystalStructure": "A2",
    "density": 7.21,
    "cohesiveEnergy": 2.92,
    "debyeTemperature": 363,
    "price": 1.82
})

Iron = Element(**{
    "name": "Iron",
    "symbol": "Fe",
    "experimentalMagneticMoment": 2.5,
    "atomicNumber": 26,
    "periodicNumber": 52,
    "radius_empirical": 1.4,
    "radius_calculated": 1.56,
    "radius_covalent": 1.32,
    "radius_metallic": 1.26,
    "radius_USE": 1.131,
    "mass": 55.845,
    "group": 8,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 8,
    "electronAffinity": 0.153236,
    "wignerSeitzElectronDensity": 5.55,
    "chemicalScale": 1.824,
    "mendeleev_universalSequence": 70,
    "mendeleev_pettifor": 58,
    "mendeleev_modified": 68,
    "workFunction": 4.67,
    "electronegativity_pauling": 1.83,
    "electronegativity_allen": 1.8,
    "ionisationEnergies": [
        762.5,
        1561.9
    ],
    "chemicalHardness": 7.75,
    "chemicalPotential": -4.03,
    "meltingTemperature": 1811,
    "boilingTemperature": 3134,
    "fusionEnthalpy": 13.81,
    "vaporisationEnthalpy": 340,
    "molarHeatCapacity": 25.1,
    "phase": "solid",
    "thermalConductivity": 79,
    "thermalExpansion": 0.0000118,
    "crystalStructure": "A2",
    "density": 7.874,
    "cohesiveEnergy": 4.28,
    "debyeTemperature": 373,
    "price": 0.424
})

Cobalt = Element(**{
    "name": "Cobalt",
    "symbol": "Co",
    "experimentalMagneticMoment": 2.5,
    "atomicNumber": 27,
    "periodicNumber": 55,
    "radius_empirical": 1.35,
    "radius_calculated": 1.52,
    "radius_covalent": 1.26,
    "radius_metallic": 1.25,
    "radius_USE": 1.137,
    "mass": 58.933194,
    "group": 9,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 9,
    "electronAffinity": 0.66226,
    "wignerSeitzElectronDensity": 5.36,
    "chemicalScale": 1.847,
    "mendeleev_universalSequence": 73,
    "mendeleev_pettifor": 61,
    "mendeleev_modified": 67,
    "workFunction": 5,
    "electronegativity_pauling": 1.88,
    "electronegativity_allen": 1.84,
    "ionisationEnergies": [
        760.4,
        1648
    ],
    "chemicalHardness": 7.22,
    "chemicalPotential": -4.27,
    "meltingTemperature": 1768,
    "boilingTemperature": 3200,
    "fusionEnthalpy": 16.06,
    "vaporisationEnthalpy": 377,
    "molarHeatCapacity": 24.81,
    "phase": "solid",
    "thermalConductivity": 100,
    "thermalExpansion": 0.000013,
    "crystalStructure": "A3",
    "density": 8.9,
    "cohesiveEnergy": 4.39,
    "debyeTemperature": 386,
    "price": 32.8
})

Nickel = Element(**{
    "name": "Nickel",
    "symbol": "Ni",
    "atomicNumber": 28,
    "periodicNumber": 58,
    "radius_empirical": 1.35,
    "radius_calculated": 1.49,
    "radius_vanDerWaals": 1.63,
    "radius_covalent": 1.24,
    "radius_metallic": 1.24,
    "radius_USE": 1.16,
    "mass": 58.6934,
    "group": 10,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 10,
    "electronAffinity": 1.15716,
    "wignerSeitzElectronDensity": 5.36,
    "chemicalScale": 1.845,
    "mendeleev_universalSequence": 72,
    "mendeleev_pettifor": 64,
    "mendeleev_modified": 66,
    "workFunction": 5.22,
    "electronegativity_pauling": 1.91,
    "electronegativity_allen": 1.88,
    "ionisationEnergies": [
        737.1,
        1753
    ],
    "chemicalHardness": 6.48,
    "chemicalPotential": -4.4,
    "meltingTemperature": 1728,
    "boilingTemperature": 3003,
    "fusionEnthalpy": 17.48,
    "vaporisationEnthalpy": 379,
    "molarHeatCapacity": 26.07,
    "phase": "solid",
    "thermalConductivity": 91,
    "thermalExpansion": 0.0000134,
    "crystalStructure": "A1",
    "density": 8.908,
    "cohesiveEnergy": 4.44,
    "debyeTemperature": 345,
    "price": 13.9
})

Copper = Element(**{
    "name": "Copper",
    "symbol": "Cu",
    "atomicNumber": 29,
    "periodicNumber": 61,
    "radius_empirical": 1.35,
    "radius_calculated": 1.45,
    "radius_vanDerWaals": 1.4,
    "radius_covalent": 1.32,
    "radius_metallic": 1.28,
    "radius_USE": 1.203,
    "mass": 63.546,
    "group": 11,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 11,
    "electronAffinity": 1.23578,
    "wignerSeitzElectronDensity": 3.18,
    "chemicalScale": 1.804,
    "mendeleev_universalSequence": 68,
    "mendeleev_pettifor": 69,
    "mendeleev_modified": 65,
    "workFunction": 5.1,
    "electronegativity_pauling": 1.9,
    "electronegativity_allen": 1.85,
    "ionisationEnergies": [
        745.5,
        1957.9
    ],
    "chemicalHardness": 6.49,
    "chemicalPotential": -4.48,
    "meltingTemperature": 1357.77,
    "boilingTemperature": 2835,
    "fusionEnthalpy": 13.26,
    "vaporisationEnthalpy": 300.4,
    "molarHeatCapacity": 24.44,
    "phase": "solid",
    "thermalConductivity": 400,
    "thermalExpansion": 0.0000165,
    "crystalStructure": "A1",
    "density": 8.96,
    "cohesiveEnergy": 3.49,
    "debyeTemperature": 310,
    "price": 6
})

Zinc = Element(**{
    "name": "Zinc",
    "symbol": "Zn",
    "atomicNumber": 30,
    "periodicNumber": 66,
    "radius_empirical": 1.35,
    "radius_calculated": 1.42,
    "radius_vanDerWaals": 1.39,
    "radius_covalent": 1.22,
    "radius_metallic": 1.34,
    "radius_USE": 1.32,
    "mass": 65.38,
    "group": 12,
    "period": 4,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 12,
    "electronAffinity": -0.6,
    "wignerSeitzElectronDensity": 2.3,
    "chemicalScale": 1.566,
    "mendeleev_universalSequence": 53,
    "mendeleev_pettifor": 73,
    "mendeleev_modified": 71,
    "workFunction": 3.63,
    "electronegativity_pauling": 1.65,
    "electronegativity_allen": 1.588,
    "ionisationEnergies": [
        906.4,
        1733.3
    ],
    "chemicalHardness": 9.39,
    "chemicalPotential": -4.7,
    "meltingTemperature": 692.68,
    "boilingTemperature": 1180,
    "fusionEnthalpy": 7.32,
    "vaporisationEnthalpy": 115,
    "molarHeatCapacity": 25.47,
    "phase": "solid",
    "thermalConductivity": 120,
    "thermalExpansion": 0.0000302,
    "crystalStructure": "A3",
    "density": 7.14,
    "cohesiveEnergy": 1.35,
    "debyeTemperature": 237,
    "price": 2.55
})

Gallium = Element(**{
    "name": "Gallium",
    "symbol": "Ga",
    "atomicNumber": 31,
    "periodicNumber": 71,
    "radius_empirical": 1.3,
    "radius_calculated": 1.36,
    "radius_vanDerWaals": 1.87,
    "radius_covalent": 1.22,
    "radius_metallic": 1.35,
    "radius_USE": 1.365,
    "mass": 69.723,
    "group": 13,
    "period": 4,
    "block": "p",
    "series": "poorMetal",
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
    "valenceElectrons": 3,
    "electronAffinity": 0.3012,
    "wignerSeitzElectronDensity": 2.25,
    "chemicalScale": 1.62,
    "mendeleev_universalSequence": 57,
    "mendeleev_pettifor": 78,
    "mendeleev_modified": 76,
    "workFunction": 4.32,
    "electronegativity_pauling": 1.81,
    "electronegativity_allen": 1.756,
    "ionisationEnergies": [
        578.8,
        1979.3
    ],
    "chemicalHardness": 5.57,
    "chemicalPotential": -3.21,
    "meltingTemperature": 302.9146,
    "boilingTemperature": 2673,
    "fusionEnthalpy": 5.59,
    "vaporisationEnthalpy": 256,
    "molarHeatCapacity": 25.86,
    "phase": "solid",
    "thermalConductivity": 29,
    "thermalExpansion": 0.00012,
    "crystalStructure": "A11",
    "density": 5.91,
    "cohesiveEnergy": 2.81,
    "debyeTemperature": 240,
    "price": 148
})

Germanium = Element(**{
    "name": "Germanium",
    "symbol": "Ge",
    "atomicNumber": 32,
    "periodicNumber": 76,
    "radius_empirical": 1.25,
    "radius_calculated": 1.25,
    "radius_vanDerWaals": 2.11,
    "radius_covalent": 1.2,
    "radius_USE": 1.365,
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
    "valenceElectrons": 4,
    "electronAffinity": 1.2326764,
    "wignerSeitzElectronDensity": 2.57,
    "chemicalScale": 1.733,
    "mendeleev_universalSequence": 64,
    "mendeleev_pettifor": 81,
    "mendeleev_modified": 81,
    "workFunction": 5,
    "electronegativity_pauling": 2.01,
    "electronegativity_allen": 1.994,
    "ionisationEnergies": [
        762,
        1537.5
    ],
    "chemicalHardness": 6.67,
    "chemicalPotential": -4.57,
    "meltingTemperature": 1211.4,
    "boilingTemperature": 3106,
    "fusionEnthalpy": 36.94,
    "vaporisationEnthalpy": 334,
    "molarHeatCapacity": 23.222,
    "phase": "solid",
    "thermalConductivity": 60,
    "thermalExpansion": 0.000006,
    "crystalStructure": "A4",
    "density": 5.323,
    "cohesiveEnergy": 3.85,
    "debyeTemperature": 403,
    "price": 1010
})

Arsenic = Element(**{
    "name": "Arsenic",
    "symbol": "As",
    "atomicNumber": 33,
    "periodicNumber": 81,
    "radius_empirical": 1.15,
    "radius_calculated": 1.14,
    "radius_vanDerWaals": 1.85,
    "radius_covalent": 1.19,
    "radius_USE": 1.369,
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
    "valenceElectrons": 5,
    "electronAffinity": 0.8048,
    "wignerSeitzElectronDensity": 3,
    "chemicalScale": 1.827,
    "mendeleev_universalSequence": 71,
    "mendeleev_pettifor": 86,
    "mendeleev_modified": 87,
    "workFunction": 3.75,
    "electronegativity_pauling": 2.18,
    "electronegativity_allen": 2.211,
    "ionisationEnergies": [
        947,
        1798
    ],
    "chemicalHardness": 8.98,
    "chemicalPotential": -5.3,
    "meltingTemperature": 883,
    "boilingTemperature": 1090.15,
    "fusionEnthalpy": 24.44,
    "vaporisationEnthalpy": 34.76,
    "molarHeatCapacity": 24.64,
    "phase": "solid",
    "thermalConductivity": 50,
    "thermalExpansion": 0.0000047,
    "crystalStructure": "A7",
    "density": 5.727,
    "cohesiveEnergy": 2.96,
    "debyeTemperature": 275,
    "price": 1.31
})

Selenium = Element(**{
    "name": "Selenium",
    "symbol": "Se",
    "atomicNumber": 34,
    "periodicNumber": 86,
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
    "valenceElectrons": 6,
    "electronAffinity": 2.0206047,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.997,
    "mendeleev_universalSequence": 84,
    "mendeleev_pettifor": 90,
    "mendeleev_modified": 92,
    "workFunction": 5.9,
    "electronegativity_pauling": 2.55,
    "electronegativity_allen": 2.424,
    "ionisationEnergies": [
        941,
        2045
    ],
    "chemicalHardness": 7.73,
    "chemicalPotential": -5.88,
    "meltingTemperature": 494,
    "boilingTemperature": 958,
    "fusionEnthalpy": 6.69,
    "vaporisationEnthalpy": 95.48,
    "molarHeatCapacity": 25.363,
    "phase": "solid",
    "thermalConductivity": 0.52,
    "thermalExpansion": 0.000038,
    "crystalStructure": "A8",
    "density": 4.81,
    "cohesiveEnergy": 2.46,
    "debyeTemperature": 90,
    "price": 21.4
})

Bromine = Element(**{
    "name": "Bromine",
    "symbol": "Br",
    "atomicNumber": 35,
    "periodicNumber": 92,
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
    "valenceElectrons": 7,
    "electronAffinity": 3.363588,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 2.12,
    "mendeleev_universalSequence": 88,
    "mendeleev_pettifor": 95,
    "mendeleev_modified": 97,
    "workFunction": None,
    "electronegativity_pauling": 2.96,
    "electronegativity_allen": 2.685,
    "ionisationEnergies": [
        1139.9,
        2103
    ],
    "chemicalHardness": 8.45,
    "chemicalPotential": -7.59,
    "meltingTemperature": 265.8,
    "boilingTemperature": 332,
    "fusionEnthalpy": 10.571,
    "vaporisationEnthalpy": 29.96,
    "molarHeatCapacity": 75.69,
    "phase": "liquid",
    "thermalConductivity": 0.12,
    "thermalExpansion": None,
    "density": 3.1028,
    "cohesiveEnergy": 1.22,
    "debyeTemperature": None,
    "price": 4.39
})

Krypton = Element(**{
    "name": "Krypton",
    "symbol": "Kr",
    "atomicNumber": 36,
    "periodicNumber": 98,

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
    "valenceElectrons": 8,
    "electronAffinity": -1,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.71,
    "mendeleev_universalSequence": 63,
    "mendeleev_pettifor": 4,
    "mendeleev_modified": 4,
    "workFunction": None,
    "electronegativity_pauling": 3,
    "electronegativity_allen": 2.966,
    "ionisationEnergies": [
        1350.8,
        2350.4
    ],
    "chemicalHardness": 14,
    "chemicalPotential": -7,
    "meltingTemperature": 115.78,
    "boilingTemperature": 119.93,
    "fusionEnthalpy": 1.64,
    "vaporisationEnthalpy": 9.08,
    "molarHeatCapacity": 20.95,
    "phase": "gas",
    "thermalConductivity": 0.00943,
    "thermalExpansion": None,
    "density": 0.003749,
    "cohesiveEnergy": 0.116,
    "debyeTemperature": None,
    "price": 290
})

Rubidium = Element(**{
    "name": "Rubidium",
    "symbol": "Rb",
    "atomicNumber": 37,
    "periodicNumber": 4,
    "radius_empirical": 2.35,
    "radius_calculated": 2.65,
    "radius_vanDerWaals": 3.03,
    "radius_covalent": 2.2,
    "radius_metallic": 2.48,
    "radius_USE": 2.319,
    "mass": 84.4678,
    "group": 1,
    "period": 5,
    "block": "s",
    "series": "alkaliMetal",
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
    "valenceElectrons": 1,
    "electronAffinity": 0.485916,
    "wignerSeitzElectronDensity": 0.22,
    "chemicalScale": 0.272,
    "mendeleev_universalSequence": 3,
    "mendeleev_pettifor": 9,
    "mendeleev_modified": 9,
    "workFunction": 2.261,
    "electronegativity_pauling": 0.82,
    "electronegativity_allen": 0.706,
    "ionisationEnergies": [
        403,
        2633
    ],
    "chemicalHardness": 3.69,
    "chemicalPotential": -2.33,
    "meltingTemperature": 312.45,
    "boilingTemperature": 961,
    "fusionEnthalpy": 2.19,
    "vaporisationEnthalpy": 69,
    "molarHeatCapacity": 31.06,
    "phase": "solid",
    "thermalConductivity": 58,
    "thermalExpansion": 0.00009,
    "crystalStructure": "A2",
    "density": 1.532,
    "cohesiveEnergy": 0.852,
    "debyeTemperature": 59,
    "price": 15500
})

Strontium = Element(**{
    "name": "Strontium",
    "symbol": "Sr",
    "atomicNumber": 38,
    "periodicNumber": 8,
    "radius_empirical": 2,
    "radius_calculated": 2.19,
    "radius_vanDerWaals": 2.49,
    "radius_covalent": 1.95,
    "radius_metallic": 2.15,
    "radius_USE": 1.935,
    "mass": 87.62,
    "group": 2,
    "period": 5,
    "block": "s",
    "series": "alkalineEarthMetal",
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
    "valenceElectrons": 2,
    "electronAffinity": 0.05206,
    "wignerSeitzElectronDensity": 0.59,
    "chemicalScale": 0.662,
    "mendeleev_universalSequence": 7,
    "mendeleev_pettifor": 15,
    "mendeleev_modified": 15,
    "workFunction": 2.59,
    "electronegativity_pauling": 0.95,
    "electronegativity_allen": 0.963,
    "ionisationEnergies": [
        549.5,
        1064.2
    ],
    "chemicalHardness": 5.64,
    "chemicalPotential": -2.88,
    "meltingTemperature": 1050,
    "boilingTemperature": 1650,
    "fusionEnthalpy": 7.43,
    "vaporisationEnthalpy": 141,
    "molarHeatCapacity": 26.4,
    "phase": "solid",
    "thermalConductivity": 35,
    "thermalExpansion": 0.0000225,
    "crystalStructure": "A1",
    "density": 2.64,
    "cohesiveEnergy": 1.72,
    "debyeTemperature": 148,
    "price": 6.68
})

Yttrium = Element(**{
    "name": "Yttrium",
    "symbol": "Y",
    "atomicNumber": 39,
    "periodicNumber": 12,
    "radius_empirical": 1.8,
    "radius_calculated": 2.12,
    "radius_covalent": 1.9,
    "radius_metallic": 1.8,
    "radius_USE": 1.625,
    "mass": 88.90584,
    "group": 3,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 3,
    "electronAffinity": 0.307,
    "wignerSeitzElectronDensity": 1.77,
    "chemicalScale": 1.071,
    "mendeleev_universalSequence": 19,
    "mendeleev_pettifor": 19,
    "mendeleev_modified": 21,
    "workFunction": 3.1,
    "electronegativity_pauling": 1.22,
    "electronegativity_allen": 1.12,
    "ionisationEnergies": [
        600,
        1180
    ],
    "chemicalHardness": 5.91,
    "chemicalPotential": -3.27,
    "meltingTemperature": 1799,
    "boilingTemperature": 3203,
    "fusionEnthalpy": 11.42,
    "vaporisationEnthalpy": 363,
    "molarHeatCapacity": 26.53,
    "phase": "solid",
    "thermalConductivity": 17,
    "thermalExpansion": 0.0000106,
    "crystalStructure": "A3",
    "density": 4.472,
    "cohesiveEnergy": 4.37,
    "debyeTemperature": 214,
    "price": 31
})

Zirconium = Element(**{
    "name": "Zirconium",
    "symbol": "Zr",
    "atomicNumber": 40,
    "periodicNumber": 41,
    "radius_empirical": 1.55,
    "radius_calculated": 2.06,
    "radius_covalent": 1.75,
    "radius_metallic": 1.6,
    "radius_USE": 1.463,
    "mass": 91.224,
    "group": 4,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 4,
    "electronAffinity": 0.43328,
    "wignerSeitzElectronDensity": 2.8,
    "chemicalScale": 1.266,
    "mendeleev_universalSequence": 32,
    "mendeleev_pettifor": 46,
    "mendeleev_modified": 46,
    "workFunction": 4.05,
    "electronegativity_pauling": 1.33,
    "electronegativity_allen": 1.32,
    "ionisationEnergies": [
        640.1,
        1270
    ],
    "chemicalHardness": 6.21,
    "chemicalPotential": -3.53,
    "meltingTemperature": 2128,
    "boilingTemperature": 4650,
    "fusionEnthalpy": 14,
    "vaporisationEnthalpy": 591,
    "molarHeatCapacity": 25.36,
    "phase": "solid",
    "thermalConductivity": 23,
    "thermalExpansion": 0.0000057,
    "crystalStructure": "A3",
    "density": 6.52,
    "cohesiveEnergy": 6.25,
    "debyeTemperature": 250,
    "price": 37.1
})

Niobium = Element(**{
    "name": "Niobium",
    "symbol": "Nb",
    "atomicNumber": 41,
    "periodicNumber": 44,
    "radius_empirical": 1.45,
    "radius_calculated": 1.98,
    "radius_covalent": 1.64,
    "radius_metallic": 1.46,
    "radius_USE": 1.362,
    "mass": 92.90637,
    "group": 5,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 5,
    "electronAffinity": 0.9174,
    "wignerSeitzElectronDensity": 4.41,
    "chemicalScale": 1.503,
    "mendeleev_universalSequence": 48,
    "mendeleev_pettifor": 49,
    "mendeleev_modified": 50,
    "workFunction": 4.02,
    "electronegativity_pauling": 1.6,
    "electronegativity_allen": 1.41,
    "ionisationEnergies": [
        652.1,
        1380
    ],
    "chemicalHardness": 5.86,
    "chemicalPotential": -3.83,
    "meltingTemperature": 2750,
    "boilingTemperature": 5017,
    "fusionEnthalpy": 30,
    "vaporisationEnthalpy": 689.9,
    "molarHeatCapacity": 24.6,
    "phase": "solid",
    "thermalConductivity": 54,
    "thermalExpansion": 0.0000073,
    "crystalStructure": "A2",
    "density": 8.57,
    "cohesiveEnergy": 7.57,
    "debyeTemperature": 260,
    "price": 85.6
})

Molybdenum = Element(**{
    "name": "Molybdenum",
    "symbol": "Mo",
    "atomicNumber": 42,
    "periodicNumber": 47,
    "radius_empirical": 1.45,
    "radius_calculated": 1.9,
    "radius_covalent": 1.54,
    "radius_metallic": 1.39,
    "radius_USE": 1.294,
    "mass": 95.95,
    "group": 6,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 6,
    "electronAffinity": 0.7473,
    "wignerSeitzElectronDensity": 5.55,
    "chemicalScale": 1.877,
    "mendeleev_universalSequence": 74,
    "mendeleev_pettifor": 53,
    "mendeleev_modified": 53,
    "workFunction": 4.53,
    "electronegativity_pauling": 2.16,
    "electronegativity_allen": 1.47,
    "ionisationEnergies": [
        684.3,
        1560
    ],
    "chemicalHardness": 6.35,
    "chemicalPotential": -3.92,
    "meltingTemperature": 2896,
    "boilingTemperature": 4912,
    "fusionEnthalpy": 37.48,
    "vaporisationEnthalpy": 598,
    "molarHeatCapacity": 24.06,
    "phase": "solid",
    "thermalConductivity": 139,
    "thermalExpansion": 0.0000048,
    "crystalStructure": "A2",
    "density": 10.28,
    "cohesiveEnergy": 6.82,
    "debyeTemperature": 377,
    "price": 40.1
})

Technetium = Element(**{
    "name": "Technetium",
    "symbol": "Tc",
    "atomicNumber": 43,
    "periodicNumber": 50,
    "radius_empirical": 1.35,
    "radius_calculated": 1.83,
    "radius_covalent": 1.47,
    "radius_metallic": 1.36,
    "radius_USE": 1.257,
    "mass": 97,
    "group": 7,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 7,
    "electronAffinity": 0.55,
    "wignerSeitzElectronDensity": 5.93,
    "chemicalScale": 1.76,
    "mendeleev_universalSequence": 67,
    "mendeleev_pettifor": 55,
    "mendeleev_modified": 56,
    "workFunction": 4.58,
    "electronegativity_pauling": 1.9,
    "electronegativity_allen": 1.51,
    "ionisationEnergies": [
        702,
        1470
    ],
    "chemicalHardness": 6.73,
    "chemicalPotential": -3.91,
    "meltingTemperature": 2430,
    "boilingTemperature": 4538,
    "fusionEnthalpy": 33.29,
    "vaporisationEnthalpy": 585.2,
    "molarHeatCapacity": 24.27,
    "phase": "solid",
    "thermalConductivity": 51,
    "thermalExpansion": 0.0000071,
    "crystalStructure": "A3",
    "density": 11,
    "cohesiveEnergy": 6.85,
    "debyeTemperature": 422,
    "price": 100000
})

Ruthenium = Element(**{
    "name": "Ruthenium",
    "symbol": "Ru",
    "atomicNumber": 44,
    "periodicNumber": 53,
    "radius_empirical": 1.3,
    "radius_calculated": 1.78,
    "radius_covalent": 1.46,
    "radius_metallic": 1.34,
    "radius_USE": 1.249,
    "mass": 101.07,
    "group": 8,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 8,
    "electronAffinity": 1.0468,
    "wignerSeitzElectronDensity": 6.13,
    "chemicalScale": 1.937,
    "mendeleev_universalSequence": 80,
    "mendeleev_pettifor": 60,
    "mendeleev_modified": 58,
    "workFunction": 4.71,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 1.54,
    "ionisationEnergies": [
        710.2,
        1620
    ],
    "chemicalHardness": 6.28,
    "chemicalPotential": -4.22,
    "meltingTemperature": 2607,
    "boilingTemperature": 4423,
    "fusionEnthalpy": 38.59,
    "vaporisationEnthalpy": 619,
    "molarHeatCapacity": 24.06,
    "phase": "solid",
    "thermalConductivity": 120,
    "thermalExpansion": 0.0000064,
    "crystalStructure": "A3",
    "density": 12.45,
    "cohesiveEnergy": 6.74,
    "debyeTemperature": 415,
    "price": 10600
})

Rhodium = Element(**{
    "name": "Rhodium",
    "symbol": "Rh",
    "atomicNumber": 45,
    "periodicNumber": 56,
    "radius_empirical": 1.35,
    "radius_calculated": 1.73,
    "radius_covalent": 1.42,
    "radius_metallic": 1.34,
    "radius_USE": 1.264,
    "mass": 102.9055,
    "group": 9,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 9,
    "electronAffinity": 1.14289,
    "wignerSeitzElectronDensity": 5.45,
    "chemicalScale": 1.97,
    "mendeleev_universalSequence": 82,
    "mendeleev_pettifor": 63,
    "mendeleev_modified": 60,
    "workFunction": 4.98,
    "electronegativity_pauling": 2.28,
    "electronegativity_allen": 1.56,
    "ionisationEnergies": [
        719.7,
        1740
    ],
    "chemicalHardness": 6.32,
    "chemicalPotential": -4.3,
    "meltingTemperature": 2237,
    "boilingTemperature": 3968,
    "fusionEnthalpy": 26.59,
    "vaporisationEnthalpy": 493,
    "molarHeatCapacity": 24.98,
    "phase": "solid",
    "thermalConductivity": 150,
    "thermalExpansion": 0.000008,
    "crystalStructure": "A1",
    "density": 12.41,
    "cohesiveEnergy": 5.75,
    "debyeTemperature": 350,
    "price": 147000
})

Palladium = Element(**{
    "name": "Palladium",
    "symbol": "Pd",
    "atomicNumber": 46,
    "periodicNumber": 59,
    "radius_empirical": 1.4,
    "radius_calculated": 1.69,
    "radius_vanDerWaals": 1.63,
    "radius_covalent": 1.39,
    "radius_metallic": 1.37,
    "radius_USE": 1.306,
    "mass": 106.42,
    "group": 10,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 10,
    "electronAffinity": 0.56214,
    "wignerSeitzElectronDensity": 4.66,
    "chemicalScale": 1.89,
    "mendeleev_universalSequence": 76,
    "mendeleev_pettifor": 66,
    "mendeleev_modified": 62,
    "workFunction": 4.85,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 1.58,
    "ionisationEnergies": [
        804.4,
        1870
    ],
    "chemicalHardness": 7.77,
    "chemicalPotential": -4.44,
    "meltingTemperature": 1828.05,
    "boilingTemperature": 3236,
    "fusionEnthalpy": 16.74,
    "vaporisationEnthalpy": 358,
    "molarHeatCapacity": 25.98,
    "phase": "solid",
    "thermalConductivity": 71,
    "thermalExpansion": 0.0000118,
    "crystalStructure": "A1",
    "density": 12.023,
    "cohesiveEnergy": 3.89,
    "debyeTemperature": 275,
    "price": 49500
})

Silver = Element(**{
    "name": "Silver",
    "symbol": "Ag",
    "atomicNumber": 47,
    "periodicNumber": 62,
    "radius_empirical": 1.6,
    "radius_calculated": 1.65,
    "radius_vanDerWaals": 1.72,
    "radius_covalent": 1.45,
    "radius_metallic": 1.44,
    "radius_USE": 1.379,
    "mass": 107.8682,
    "group": 11,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 11,
    "electronAffinity": 1.30447,
    "wignerSeitzElectronDensity": 2.52,
    "chemicalScale": 1.676,
    "mendeleev_universalSequence": 60,
    "mendeleev_pettifor": 68,
    "mendeleev_modified": 64,
    "workFunction": 4.64,
    "electronegativity_pauling": 1.93,
    "electronegativity_allen": 1.87,
    "ionisationEnergies": [
        731,
        2070
    ],
    "chemicalHardness": 6.27,
    "chemicalPotential": -4.44,
    "meltingTemperature": 1234.93,
    "boilingTemperature": 2435,
    "fusionEnthalpy": 11.28,
    "vaporisationEnthalpy": 254,
    "molarHeatCapacity": 25.35,
    "phase": "solid",
    "thermalConductivity": 430,
    "thermalExpansion": 0.0000189,
    "crystalStructure": "A1",
    "density": 10.49,
    "cohesiveEnergy": 2.95,
    "debyeTemperature": 221,
    "price": 521
})

Cadmium = Element(**{
    "name": "Cadmium",
    "symbol": "Cd",
    "atomicNumber": 48,
    "periodicNumber": 67,
    "radius_empirical": 1.55,
    "radius_calculated": 1.61,
    "radius_vanDerWaals": 1.58,
    "radius_covalent": 1.44,
    "radius_metallic": 1.51,
    "radius_USE": 1.509,
    "mass": 112.414,
    "group": 12,
    "period": 5,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 12,
    "electronAffinity": -0.7,
    "wignerSeitzElectronDensity": 1.91,
    "chemicalScale": 1.433,
    "mendeleev_universalSequence": 42,
    "mendeleev_pettifor": 72,
    "mendeleev_modified": 72,
    "workFunction": 4.08,
    "electronegativity_pauling": 1.69,
    "electronegativity_allen": 1.521,
    "ionisationEnergies": [
        867.8,
        1631.4
    ],
    "chemicalHardness": 8.99,
    "chemicalPotential": -4.5,
    "meltingTemperature": 594.22,
    "boilingTemperature": 1040,
    "fusionEnthalpy": 6.21,
    "vaporisationEnthalpy": 99.87,
    "molarHeatCapacity": 26.02,
    "phase": "solid",
    "thermalConductivity": 96,
    "thermalExpansion": 0.0000308,
    "crystalStructure": "A3",
    "density": 8.65,
    "cohesiveEnergy": 1.16,
    "debyeTemperature": 221,
    "price": 2.73
})

Indium = Element(**{
    "name": "Indium",
    "symbol": "In",
    "atomicNumber": 49,
    "periodicNumber": 72,
    "radius_empirical": 1.55,
    "radius_calculated": 1.56,
    "radius_vanDerWaals": 1.93,
    "radius_covalent": 1.42,
    "radius_metallic": 1.67,
    "radius_USE": 1.541,
    "mass": 114.818,
    "group": 13,
    "period": 5,
    "block": "p",
    "series": "poorMetal",
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
    "valenceElectrons": 3,
    "electronAffinity": 0.38392,
    "wignerSeitzElectronDensity": 1.6,
    "chemicalScale": 1.458,
    "mendeleev_universalSequence": 45,
    "mendeleev_pettifor": 76,
    "mendeleev_modified": 77,
    "workFunction": 4.09,
    "electronegativity_pauling": 1.78,
    "electronegativity_allen": 1.656,
    "ionisationEnergies": [
        558.3,
        1820.7
    ],
    "chemicalHardness": 5.4,
    "chemicalPotential": -3.09,
    "meltingTemperature": 429.7485,
    "boilingTemperature": 2345,
    "fusionEnthalpy": 3.281,
    "vaporisationEnthalpy": 231.8,
    "molarHeatCapacity": 26.74,
    "phase": "solid",
    "thermalConductivity": 82,
    "thermalExpansion": 0.0000321,
    "crystalStructure": "A6",
    "density": 7.31,
    "cohesiveEnergy": 2.52,
    "debyeTemperature": 129,
    "price": 167
})

Tin = Element(**{
    "name": "Tin",
    "symbol": "Sn",
    "atomicNumber": 50,
    "periodicNumber": 77,
    "radius_empirical": 1.45,
    "radius_calculated": 1.45,
    "radius_vanDerWaals": 2.17,
    "radius_covalent": 1.39,
    "radius_USE": 1.541,
    "mass": 118.71,
    "group": 14,
    "period": 5,
    "block": "p",
    "series": "poorMetal",
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
    "valenceElectrons": 4,
    "electronAffinity": 1.11207,
    "wignerSeitzElectronDensity": 1.9,
    "chemicalScale": 1.56,
    "mendeleev_universalSequence": 52,
    "mendeleev_pettifor": 80,
    "mendeleev_modified": 80,
    "workFunction": 4.42,
    "electronegativity_pauling": 1.96,
    "electronegativity_allen": 1.824,
    "ionisationEnergies": [
        708.6,
        1411.8
    ],
    "chemicalHardness": 6.23,
    "chemicalPotential": -4.23,
    "meltingTemperature": 505.08,
    "boilingTemperature": 2875,
    "fusionEnthalpy": 7.03,
    "vaporisationEnthalpy": 296.1,
    "molarHeatCapacity": 27.112,
    "phase": "solid",
    "thermalConductivity": 67,
    "thermalExpansion": 0.000022,
    "crystalStructure": "A5",
    "density": 7.265,
    "cohesiveEnergy": 3.14,
    "debyeTemperature": 254,
    "price": 18.7
})

Antimony = Element(**{
    "name": "Antimony",
    "symbol": "Sb",
    "atomicNumber": 51,
    "periodicNumber": 82,
    "radius_empirical": 1.45,
    "radius_calculated": 1.33,
    "radius_vanDerWaals": 2.06,
    "radius_covalent": 1.39,
    "radius_USE": 1.553,
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
    "valenceElectrons": 5,
    "electronAffinity": 1.047401,
    "wignerSeitzElectronDensity": 2,
    "chemicalScale": 1.601,
    "mendeleev_universalSequence": 56,
    "mendeleev_pettifor": 85,
    "mendeleev_modified": 88,
    "workFunction": 4.55,
    "electronegativity_pauling": 2.05,
    "electronegativity_allen": 1.984,
    "ionisationEnergies": [
        834,
        1594.9
    ],
    "chemicalHardness": 7.56,
    "chemicalPotential": -4.82,
    "meltingTemperature": 903.78,
    "boilingTemperature": 1908,
    "fusionEnthalpy": 19.79,
    "vaporisationEnthalpy": 193.43,
    "molarHeatCapacity": 25.23,
    "phase": "solid",
    "thermalConductivity": 24,
    "thermalExpansion": 0.000011,
    "crystalStructure": "rhombohedral",
    "density": 6.697,
    "cohesiveEnergy": 2.75,
    "debyeTemperature": 200,
    "price": 5.79
})

Tellurium = Element(**{
    "name": "Tellurium",
    "symbol": "Te",
    "atomicNumber": 52,
    "periodicNumber": 87,
    "radius_empirical": 1.4,
    "radius_calculated": 1.23,
    "radius_vanDerWaals": 2.06,
    "radius_covalent": 1.38,
    "radius_USE": 1.596,
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
    "valenceElectrons": 6,
    "electronAffinity": 1.970875,
    "wignerSeitzElectronDensity": 2.3526,
    "chemicalScale": 1.594,
    "mendeleev_universalSequence": 55,
    "mendeleev_pettifor": 89,
    "mendeleev_modified": 91,
    "workFunction": 4.95,
    "electronegativity_pauling": 2.1,
    "electronegativity_allen": 2.158,
    "electronegativity_miedema": 4.7,
    "ionisationEnergies": [
        869.3,
        1790
    ],
    "chemicalHardness": 7.04,
    "chemicalPotential": -5.49,
    "meltingTemperature": 722.66,
    "boilingTemperature": 1261,
    "fusionEnthalpy": 17.49,
    "vaporisationEnthalpy": 114.1,
    "molarHeatCapacity": 25.73,
    "phase": "solid",
    "thermalConductivity": 3,
    "thermalExpansion": 0.000018,
    "crystalStructure": "A8",
    "density": 6.24,
    "cohesiveEnergy": 2.19,
    "debyeTemperature": 139,
    "price": 63.5
})

Iodine = Element(**{
    "name": "Iodine",
    "symbol": "I",
    "atomicNumber": 53,
    "periodicNumber": 93,
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
    "valenceElectrons": 7,
    "electronAffinity": 3.0590465,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.81,
    "mendeleev_universalSequence": 69,
    "mendeleev_pettifor": 94,
    "mendeleev_modified": 96,
    "workFunction": None,
    "electronegativity_pauling": 2.66,
    "electronegativity_allen": 2.359,
    "ionisationEnergies": [
        1008.4,
        1845.9
    ],
    "chemicalHardness": 7.39,
    "chemicalPotential": -6.75,
    "meltingTemperature": 386.85,
    "boilingTemperature": 457.4,
    "fusionEnthalpy": 15.52,
    "vaporisationEnthalpy": 41.57,
    "molarHeatCapacity": 54.44,
    "phase": "solid",
    "thermalConductivity": 0.449,
    "thermalExpansion": None,
    "crystalStructure": "A14",
    "density": 4.933,
    "cohesiveEnergy": 1.11,
    "debyeTemperature": 109,
    "price": 35
})

Xenon = Element(**{
    "name": "Xenon",
    "symbol": "Xe",
    "atomicNumber": 54,
    "periodicNumber": 99,
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
    "valenceElectrons": 8,
    "electronAffinity": -0.8,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.263,
    "mendeleev_universalSequence": 31,
    "mendeleev_pettifor": 5,
    "mendeleev_modified": 5,
    "workFunction": None,
    "electronegativity_pauling": 2.6,
    "electronegativity_allen": 2.582,
    "ionisationEnergies": [
        1170.4,
        2046.4
    ],
    "chemicalHardness": 12.13,
    "chemicalPotential": -6.07,
    "meltingTemperature": 161.4,
    "boilingTemperature": 165.051,
    "fusionEnthalpy": 2.27,
    "vaporisationEnthalpy": 12.64,
    "molarHeatCapacity": 21.01,
    "phase": "gas",
    "thermalConductivity": 0.00565,
    "thermalExpansion": None,
    "density": 0.005894,
    "cohesiveEnergy": 0.16,
    "debyeTemperature": None,
    "price": 1800
})

Caesium = Element(**{
    "name": "Caesium",
    "symbol": "Cs",
    "atomicNumber": 55,
    "periodicNumber": 5,
    "radius_empirical": 2.65,
    "radius_calculated": 2.98,
    "radius_vanDerWaals": 3.43,
    "radius_covalent": 2.44,
    "radius_metallic": 2.65,
    "radius_USE": 2.535,
    "mass": 132.90545196,
    "group": 1,
    "period": 6,
    "block": "s",
    "series": "alkaliMetal",
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
    "valenceElectrons": 1,
    "electronAffinity": 0.47163,
    "wignerSeitzElectronDensity": 0.17,
    "chemicalScale": 0.077,
    "mendeleev_universalSequence": 2,
    "mendeleev_pettifor": 8,
    "mendeleev_modified": 8,
    "workFunction": 1.95,
    "electronegativity_pauling": 0.79,
    "electronegativity_allen": 0.659,
    "ionisationEnergies": [
        375.7,
        2234.3
    ],
    "chemicalHardness": 3.42,
    "chemicalPotential": -2.18,
    "meltingTemperature": 301.7,
    "boilingTemperature": 944,
    "fusionEnthalpy": 2.09,
    "vaporisationEnthalpy": 63.9,
    "molarHeatCapacity": 32.21,
    "phase": "solid",
    "thermalConductivity": 36,
    "thermalExpansion": 0.000097,
    "crystalStructure": "A2",
    "density": 1.93,
    "cohesiveEnergy": 0.804,
    "debyeTemperature": 43,
    "price": 61800
})

Barium = Element(**{
    "name": "Barium",
    "symbol": "Ba",
    "atomicNumber": 56,
    "periodicNumber": 9,
    "radius_empirical": 2.15,
    "radius_calculated": 2.53,
    "radius_vanDerWaals": 2.68,
    "radius_covalent": 2.15,
    "radius_metallic": 2.22,
    "radius_USE": 1.962,
    "mass": 137.327,
    "group": 2,
    "period": 6,
    "block": "s",
    "series": "alkalineEarthMetal",
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
    "valenceElectrons": 2,
    "electronAffinity": 0.14462,
    "wignerSeitzElectronDensity": 0.53,
    "chemicalScale": 0.606,
    "mendeleev_universalSequence": 6,
    "mendeleev_pettifor": 14,
    "mendeleev_modified": 14,
    "workFunction": 2.52,
    "electronegativity_pauling": 0.89,
    "electronegativity_allen": 0.881,
    "ionisationEnergies": [
        502.9,
        965.2
    ],
    "chemicalHardness": 5.07,
    "chemicalPotential": -2.68,
    "meltingTemperature": 1000,
    "boilingTemperature": 2118,
    "fusionEnthalpy": 7.12,
    "vaporisationEnthalpy": 142,
    "molarHeatCapacity": 28.07,
    "phase": "solid",
    "thermalConductivity": 18,
    "thermalExpansion": 0.0000206,
    "crystalStructure": "A2",
    "density": 3.51,
    "cohesiveEnergy": 1.9,
    "debyeTemperature": 116,
    "price": 0.275
})

Lanthanum = Element(**{
    "name": "Lanthanum",
    "symbol": "La",
    "atomicNumber": 57,
    "periodicNumber": 13,
    "radius_empirical": 1.95,
    "radius_covalent": 2.07,
    "radius_metallic": 1.87,
    "radius_USE": 1.647,
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
    "valenceElectrons": 3,
    "electronAffinity": 0.557546,
    "wignerSeitzElectronDensity": 1.64,
    "chemicalScale": 0.984,
    "mendeleev_universalSequence": 13,
    "mendeleev_pettifor": 33,
    "mendeleev_modified": 32,
    "workFunction": 3.5,
    "electronegativity_pauling": 1.1,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        538.1,
        1067
    ],
    "chemicalHardness": 5.11,
    "chemicalPotential": -3.03,
    "meltingTemperature": 1193,
    "boilingTemperature": 3737,
    "fusionEnthalpy": 6.2,
    "vaporisationEnthalpy": 400,
    "molarHeatCapacity": 27.11,
    "phase": "solid",
    "thermalConductivity": 13,
    "thermalExpansion": 0.0000121,
    "crystalStructure": "A3",
    "density": 6.162,
    "cohesiveEnergy": 4.47,
    "debyeTemperature": 135,
    "price": 4.92
})

Cerium = Element(**{
    "name": "Cerium",
    "symbol": "Ce",
    "atomicNumber": 58,
    "periodicNumber": 15,
    "radius_empirical": 1.85,
    "radius_covalent": 2.04,
    "radius_metallic": 1.818,
    "radius_USE": 1.467,
    "mass": 140.116,
    "group": None,
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
    "valenceElectrons": 4,
    "electronAffinity": 0.57,
    "wignerSeitzElectronDensity": 1.69,
    "chemicalScale": 1.144,
    "mendeleev_universalSequence": 27,
    "mendeleev_pettifor": 32,
    "mendeleev_modified": 31,
    "workFunction": 2.9,
    "electronegativity_pauling": 1.12,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        534.4,
        1050
    ],
    "chemicalHardness": 4.91,
    "chemicalPotential": -3.09,
    "meltingTemperature": 1068,
    "boilingTemperature": 3716,
    "fusionEnthalpy": 5.46,
    "vaporisationEnthalpy": 398,
    "molarHeatCapacity": 26.94,
    "phase": "solid",
    "thermalConductivity": 11,
    "thermalExpansion": 0.0000063,
    "crystalStructure": "A3",
    "density": 6.77,
    "cohesiveEnergy": 4.32,
    "debyeTemperature": 138,
    "price": 4.71
})

Praseodymium = Element(**{
    "name": "Praseodymium",
    "symbol": "Pr",
    "atomicNumber": 59,
    "periodicNumber": 17,
    "radius_empirical": 1.85,
    "radius_calculated": 2.47,
    "radius_covalent": 2.03,
    "radius_metallic": 1.824,
    "radius_USE": 1.367,
    "mass": 140.90766,
    "group": None,
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
    "valenceElectrons": 5,
    "electronAffinity": 0.10923,
    "wignerSeitzElectronDensity": 1.73,
    "chemicalScale": 1.232,
    "mendeleev_universalSequence": 29,
    "mendeleev_pettifor": 31,
    "mendeleev_modified": 30,
    "workFunction": 2.7,
    "electronegativity_pauling": 1.13,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        527,
        1020
    ],
    "chemicalHardness": 4.51,
    "chemicalPotential": -3.22,
    "meltingTemperature": 1208,
    "boilingTemperature": 3403,
    "fusionEnthalpy": 6.89,
    "vaporisationEnthalpy": 331,
    "molarHeatCapacity": 27.2,
    "phase": "solid",
    "thermalConductivity": 13,
    "thermalExpansion": 0.0000067,
    "crystalStructure": "A3",
    "density": 6.77,
    "cohesiveEnergy": 3.7,
    "debyeTemperature": 138,
    "price": 103
})

Neodymium = Element(**{
    "name": "Neodymium",
    "symbol": "Nd",
    "atomicNumber": 60,
    "periodicNumber": 19,
    "radius_empirical": 1.85,
    "radius_calculated": 2.06,
    "radius_covalent": 2.01,
    "radius_metallic": 1.814,
    "radius_USE": 1.32,
    "mass": 144.242,
    "group": None,
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
    "valenceElectrons": 6,
    "electronAffinity": 0.09749,
    "wignerSeitzElectronDensity": 1.73,
    "chemicalScale": 1.276,
    "mendeleev_universalSequence": 33,
    "mendeleev_pettifor": 30,
    "mendeleev_modified": 29,
    "workFunction": 3.2,
    "electronegativity_pauling": 1.14,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        533.1,
        1040
    ],
    "chemicalHardness": 5.36,
    "chemicalPotential": -2.85,
    "meltingTemperature": 1297,
    "boilingTemperature": 3347,
    "fusionEnthalpy": 7.14,
    "vaporisationEnthalpy": 289,
    "molarHeatCapacity": 27.45,
    "phase": "solid",
    "thermalConductivity": 17,
    "thermalExpansion": 0.0000096,
    "crystalStructure": "A3",
    "density": 7.01,
    "cohesiveEnergy": 3.4,
    "debyeTemperature": 148,
    "price": 57.5
})

Promethium = Element(**{
    "name": "Promethium",
    "symbol": "Pm",
    "atomicNumber": 61,
    "periodicNumber": 21,
    "radius_empirical": 1.85,
    "radius_calculated": 2.05,
    "radius_covalent": 1.99,
    "radius_metallic": 1.834,
    "radius_USE": 1.635,
    "mass": 145,
    "group": None,
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
    "valenceElectrons": 7,
    "electronAffinity": 0.129,
    "wignerSeitzElectronDensity": 1.77,
    "chemicalScale": 1.011,
    "mendeleev_universalSequence": 14,
    "mendeleev_pettifor": 29,
    "mendeleev_modified": 28,
    "workFunction": None,
    "electronegativity_pauling": 1.13,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        540,
        1050
    ],
    "chemicalHardness": 5.45,
    "chemicalPotential": -2.86,
    "meltingTemperature": 1315,
    "boilingTemperature": 3273,
    "fusionEnthalpy": 7.13,
    "vaporisationEnthalpy": 289,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": 15,
    "thermalExpansion": 0.000011,
    "crystalStructure": "A3",
    "density": 7.26,
    "cohesiveEnergy": 3.25,
    "debyeTemperature": None,
    "price": 460000
})

Samarium = Element(**{
    "name": "Samarium",
    "symbol": "Sm",
    "atomicNumber": 62,
    "periodicNumber": 23,
    "radius_empirical": 1.85,
    "radius_calculated": 2.38,
    "radius_covalent": 1.98,
    "radius_metallic": 1.804,
    "radius_USE": 1.626,
    "mass": 150.36,
    "group": None,
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
    "valenceElectrons": 8,
    "electronAffinity": 0.162,
    "wignerSeitzElectronDensity": 1.77,
    "chemicalScale": 1.041,
    "mendeleev_universalSequence": 16,
    "mendeleev_pettifor": 28,
    "mendeleev_modified": 27,
    "workFunction": 2.7,
    "electronegativity_pauling": 1.17,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        544.5,
        1070
    ],
    "chemicalHardness": 5.48,
    "chemicalPotential": -2.91,
    "meltingTemperature": 1345,
    "boilingTemperature": 2173,
    "fusionEnthalpy": 8.62,
    "vaporisationEnthalpy": 192,
    "molarHeatCapacity": 29.54,
    "phase": "solid",
    "thermalConductivity": 13,
    "thermalExpansion": 0.0000127,
    "crystalStructure": "C19",
    "density": 7.52,
    "cohesiveEnergy": 2.14,
    "debyeTemperature": 184,
    "price": 13.9
})

Europium = Element(**{
    "name": "Europium",
    "symbol": "Eu",
    "atomicNumber": 63,
    "periodicNumber": 25,
    "radius_empirical": 1.85,
    "radius_calculated": 2.31,
    "radius_covalent": 1.98,
    "radius_metallic": 1.804,
    "radius_USE": 1.62,
    "mass": 151.964,
    "group": None,
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
    "valenceElectrons": 9,
    "electronAffinity": 0.116,
    "wignerSeitzElectronDensity": 1.77,
    "chemicalScale": 1.063,
    "mendeleev_universalSequence": 18,
    "mendeleev_pettifor": 17,
    "mendeleev_modified": 18,
    "workFunction": 2.5,
    "electronegativity_pauling": 1.2,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        547.1,
        1085
    ],
    "chemicalHardness": 5.55,
    "chemicalPotential": -2.9,
    "meltingTemperature": 1099,
    "boilingTemperature": 1802,
    "fusionEnthalpy": 9.21,
    "vaporisationEnthalpy": 176,
    "molarHeatCapacity": 27.66,
    "phase": "solid",
    "thermalConductivity": 14,
    "thermalExpansion": 0.000035,
    "crystalStructure": "A2",
    "density": 5.264,
    "cohesiveEnergy": 1.86,
    "debyeTemperature": 118,
    "price": 31.4
})

Gadolinium = Element(**{
    "name": "Gadolinium",
    "symbol": "Gd",
    "atomicNumber": 64,
    "periodicNumber": 27,
    "radius_empirical": 1.8,
    "radius_calculated": 2.33,
    "radius_covalent": 1.96,
    "radius_metallic": 1.804,
    "radius_USE": 1.623,
    "mass": 157.25,
    "group": None,
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
    "valenceElectrons": 10,
    "electronAffinity": 0.137,
    "wignerSeitzElectronDensity": 1.77,
    "chemicalScale": 1.061,
    "mendeleev_universalSequence": 17,
    "mendeleev_pettifor": 27,
    "mendeleev_modified": 26,
    "workFunction": 2.9,
    "electronegativity_pauling": 1.2,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        593.4,
        1170
    ],
    "chemicalHardness": 6.01,
    "chemicalPotential": -3.15,
    "meltingTemperature": 1585,
    "boilingTemperature": 3273,
    "fusionEnthalpy": 10.05,
    "vaporisationEnthalpy": 301.3,
    "molarHeatCapacity": 37.03,
    "phase": "solid",
    "thermalConductivity": 11,
    "thermalExpansion": 0.0000094,
    "crystalStructure": "A3",
    "density": 7.9,
    "cohesiveEnergy": 4.14,
    "debyeTemperature": 155,
    "price": 28.6
})

Terbium = Element(**{
    "name": "Terbium",
    "symbol": "Tb",
    "atomicNumber": 65,
    "periodicNumber": 29,
    "radius_empirical": 1.75,
    "radius_calculated": 2.25,
    "radius_covalent": 1.94,
    "radius_metallic": 1.773,
    "radius_USE": 1.613,
    "mass": 158.92535,
    "group": None,
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
            "electrons": 9
        }
    ],
    "electrons": 65,
    "protons": 65,
    "neutrons": 94,
    "valence": 3,
    "valenceElectrons": 11,
    "electronAffinity": 0.13131,
    "wignerSeitzElectronDensity": 1.82,
    "chemicalScale": 1.012,
    "mendeleev_universalSequence": 15,
    "mendeleev_pettifor": 26,
    "mendeleev_modified": 25,
    "workFunction": 3,
    "electronegativity_pauling": 1.1,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        565.8,
        1110
    ],
    "chemicalHardness": 5.43,
    "chemicalPotential": -3.15,
    "meltingTemperature": 1629,
    "boilingTemperature": 3396,
    "fusionEnthalpy": 10.15,
    "vaporisationEnthalpy": 391,
    "molarHeatCapacity": 28.91,
    "phase": "solid",
    "thermalConductivity": 11,
    "thermalExpansion": 0.0000103,
    "crystalStructure": "A3",
    "density": 8.23,
    "cohesiveEnergy": 4.05,
    "debyeTemperature": 158,
    "price": 658
})

Dysprosium = Element(**{
    "name": "Dysprosium",
    "symbol": "Dy",
    "atomicNumber": 66,
    "periodicNumber": 31,
    "radius_empirical": 1.75,
    "radius_calculated": 2.28,
    "radius_covalent": 1.92,
    "radius_metallic": 1.781,
    "radius_USE": 1.613,
    "mass": 162.5,
    "group": None,
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
            "electrons": 10
        }
    ],
    "electrons": 66,
    "protons": 66,
    "neutrons": 97,
    "valence": 3,
    "valenceElectrons": 12,
    "electronAffinity": 0.3,
    "wignerSeitzElectronDensity": 1.82,
    "chemicalScale": 1.081,
    "mendeleev_universalSequence": 20,
    "mendeleev_pettifor": 25,
    "mendeleev_modified": 24,
    "workFunction": 3.25,
    "electronegativity_pauling": 1.22,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        573,
        1130
    ],
    "chemicalHardness": 5.59,
    "chemicalPotential": -3.15,
    "meltingTemperature": 1680,
    "boilingTemperature": 2840,
    "fusionEnthalpy": 11.06,
    "vaporisationEnthalpy": 280,
    "molarHeatCapacity": 27.7,
    "phase": "solid",
    "thermalConductivity": 11,
    "thermalExpansion": 0.00001,
    "crystalStructure": "A3",
    "density": 8.54,
    "cohesiveEnergy": 3.04,
    "debyeTemperature": 158,
    "price": 307
})

Holmium = Element(**{
    "name": "Holmium",
    "symbol": "Ho",
    "atomicNumber": 67,
    "periodicNumber": 33,
    "radius_empirical": 1.75,
    "radius_calculated": 2.26,
    "radius_covalent": 1.92,
    "radius_metallic": 1.762,
    "radius_USE": 1.604,
    "mass": 164.93033,
    "group": None,
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
            "electrons": 11
        }
    ],
    "electrons": 67,
    "protons": 67,
    "neutrons": 98,
    "valence": 3,
    "valenceElectrons": 13,
    "electronAffinity": 0.338,
    "wignerSeitzElectronDensity": 1.82,
    "chemicalScale": 1.094,
    "mendeleev_universalSequence": 22,
    "mendeleev_pettifor": 24,
    "mendeleev_modified": 23,
    "workFunction": 2.91,
    "electronegativity_pauling": 1.23,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        581,
        1140
    ],
    "chemicalHardness": 5.68,
    "chemicalPotential": -3.18,
    "meltingTemperature": 1734,
    "boilingTemperature": 2873,
    "fusionEnthalpy": 17,
    "vaporisationEnthalpy": 251,
    "molarHeatCapacity": 27.15,
    "phase": "solid",
    "thermalConductivity": 16,
    "thermalExpansion": 0.0000112,
    "crystalStructure": "A3",
    "density": 8.79,
    "cohesiveEnergy": 3.14,
    "debyeTemperature": 161,
    "price": 57.1
})

Erbium = Element(**{
    "name": "Erbium",
    "symbol": "Er",
    "atomicNumber": 68,
    "periodicNumber": 35,
    "radius_empirical": 1.75,
    "radius_calculated": 2.26,
    "radius_covalent": 1.89,
    "radius_metallic": 1.761,
    "radius_USE": 1.602,
    "mass": 167.259,
    "group": None,
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
            "electrons": 12
        }
    ],
    "electrons": 68,
    "protons": 68,
    "neutrons": 99,
    "valence": 3,
    "valenceElectrons": 14,
    "electronAffinity": 0.312,
    "wignerSeitzElectronDensity": 1.86,
    "chemicalScale": 1.101,
    "mendeleev_universalSequence": 23,
    "mendeleev_pettifor": 23,
    "mendeleev_modified": 22,
    "workFunction": 3.25,
    "electronegativity_pauling": 1.24,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        589.3,
        1150
    ],
    "chemicalHardness": 5.8,
    "chemicalPotential": -3.21,
    "meltingTemperature": 1802,
    "boilingTemperature": 3141,
    "fusionEnthalpy": 19.9,
    "vaporisationEnthalpy": 280,
    "molarHeatCapacity": 28.12,
    "phase": "solid",
    "thermalConductivity": 15,
    "thermalExpansion": 0.0000122,
    "crystalStructure": "A3",
    "density": 9.066,
    "cohesiveEnergy": 3.29,
    "debyeTemperature": 168,
    "price": 26.4
})

Thulium = Element(**{
    "name": "Thulium",
    "symbol": "Tm",
    "atomicNumber": 69,
    "periodicNumber": 37,
    "radius_empirical": 1.75,
    "radius_calculated": 2.22,
    "radius_covalent": 1.9,
    "radius_metallic": 1.759,
    "radius_USE": 1.602,
    "mass": 168.93422,
    "group": None,
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
    "valenceElectrons": 15,
    "electronAffinity": 1.029,
    "wignerSeitzElectronDensity": 1.86,
    "chemicalScale": 1.107,
    "mendeleev_universalSequence": 24,
    "mendeleev_pettifor": 22,
    "mendeleev_modified": 20,
    "workFunction": 3.22,
    "electronegativity_pauling": 1.25,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        596.7,
        1160
    ],
    "chemicalHardness": 6.17,
    "chemicalPotential": -3.1,
    "meltingTemperature": 1818,
    "boilingTemperature": 2223,
    "fusionEnthalpy": 16.84,
    "vaporisationEnthalpy": 191,
    "molarHeatCapacity": 27.03,
    "phase": "solid",
    "thermalConductivity": 17,
    "thermalExpansion": 0.0000133,
    "crystalStructure": "A3",
    "density": 9.32,
    "cohesiveEnergy": 2.42,
    "debyeTemperature": 167,
    "price": 3000
})

Ytterbium = Element(**{
    "name": "Ytterbium",
    "symbol": "Yb",
    "atomicNumber": 70,
    "periodicNumber": 38,
    "radius_empirical": 1.75,
    "radius_calculated": 2.22,
    "radius_covalent": 1.87,
    "radius_metallic": 1.76,
    "radius_USE": 1.759,
    "mass": 173.045,
    "group": None,
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
            "electrons": 14
        }
    ],
    "electrons": 70,
    "protons": 70,
    "neutrons": 102,
    "valence": 3,
    "valenceElectrons": 16,
    "electronAffinity": -0.02,
    "wignerSeitzElectronDensity": 1.86,
    "chemicalScale": 0.892,
    "mendeleev_universalSequence": 12,
    "mendeleev_pettifor": 17,
    "mendeleev_modified": 18,
    "workFunction": 2.6,
    "electronegativity_pauling": 1.1,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        603.4,
        1174.8
    ],
    "chemicalHardness": 6.25,
    "chemicalPotential": -3.13,
    "meltingTemperature": 1097,
    "boilingTemperature": 1469,
    "fusionEnthalpy": 7.66,
    "vaporisationEnthalpy": 129,
    "molarHeatCapacity": 26.74,
    "phase": "solid",
    "thermalConductivity": 39,
    "thermalExpansion": 0.0000263,
    "crystalStructure": "A1",
    "density": 6.9,
    "cohesiveEnergy": 1.6,
    "debyeTemperature": 118,
    "price": 17.1
})

Lutetium = Element(**{
    "name": "Lutetium",
    "symbol": "Lu",
    "atomicNumber": 71,
    "periodicNumber": 39,
    "radius_empirical": 1.75,
    "radius_calculated": 2.17,
    "radius_covalent": 1.87,
    "radius_metallic": 1.738,
    "radius_USE": 1.605,
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
    "valenceElectrons": 3,
    "electronAffinity": 0.2388,
    "wignerSeitzElectronDensity": 1.91,
    "chemicalScale": 1.116,
    "mendeleev_universalSequence": 25,
    "mendeleev_pettifor": 21,
    "mendeleev_modified": 18,
    "workFunction": 3.3,
    "electronegativity_pauling": 1.27,
    "electronegativity_allen": 1.09,
    "ionisationEnergies": [
        523.5,
        1340
    ],
    "chemicalHardness": 5.09,
    "chemicalPotential": -2.88,
    "meltingTemperature": 1925,
    "boilingTemperature": 3675,
    "fusionEnthalpy": 22,
    "vaporisationEnthalpy": 414,
    "molarHeatCapacity": 26.86,
    "phase": "solid",
    "thermalConductivity": 16,
    "thermalExpansion": 0.00001,
    "crystalStructure": "A3",
    "density": 9.841,
    "cohesiveEnergy": 4.43,
    "debyeTemperature": 116,
    "price": 643
})

Hafnium = Element(**{
    "name": "Hafnium",
    "symbol": "Hf",
    "atomicNumber": 72,
    "periodicNumber": 42,
    "radius_empirical": 1.55,
    "radius_calculated": 2.08,
    "radius_covalent": 1.75,
    "radius_metallic": 1.59,
    "radius_USE": 1.454,
    "mass": 178.49,
    "group": 4,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 4,
    "electronAffinity": 0.178,
    "wignerSeitzElectronDensity": 3.05,
    "chemicalScale": 1.257,
    "mendeleev_universalSequence": 30,
    "mendeleev_pettifor": 47,
    "mendeleev_modified": 47,
    "workFunction": 3.9,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": 1.16,
    "ionisationEnergies": [
        658.5,
        1440
    ],
    "chemicalHardness": 6.71,
    "chemicalPotential": -3.47,
    "meltingTemperature": 2506,
    "boilingTemperature": 4876,
    "fusionEnthalpy": 27.2,
    "vaporisationEnthalpy": 648,
    "molarHeatCapacity": 25.73,
    "phase": "solid",
    "thermalConductivity": 23,
    "thermalExpansion": 0.0000059,
    "crystalStructure": "A3",
    "density": 13.31,
    "cohesiveEnergy": 6.44,
    "debyeTemperature": 213,
    "price": 900
})

Tantalum = Element(**{
    "name": "Tantalum",
    "symbol": "Ta",
    "atomicNumber": 73,
    "periodicNumber": 45,
    "radius_empirical": 1.45,
    "radius_calculated": 2,
    "radius_covalent": 1.7,
    "radius_metallic": 1.46,
    "radius_USE": 1.358,
    "mass": 180.94788,
    "group": 5,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 5,
    "electronAffinity": 0.323,
    "wignerSeitzElectronDensity": 4.33,
    "chemicalScale": 1.449,
    "mendeleev_universalSequence": 44,
    "mendeleev_pettifor": 50,
    "mendeleev_modified": 49,
    "workFunction": 4.25,
    "electronegativity_pauling": 1.5,
    "electronegativity_allen": 1.34,
    "ionisationEnergies": [
        761,
        1500
    ],
    "chemicalHardness": 7.23,
    "chemicalPotential": -3.94,
    "meltingTemperature": 3290,
    "boilingTemperature": 5731,
    "fusionEnthalpy": 36.57,
    "vaporisationEnthalpy": 753,
    "molarHeatCapacity": 25.36,
    "phase": "solid",
    "thermalConductivity": 57,
    "thermalExpansion": 0.0000063,
    "crystalStructure": "A2",
    "density": 16.69,
    "cohesiveEnergy": 8.1,
    "debyeTemperature": 225,
    "price": 312
})

Tungsten = Element(**{
    "name": "Tungsten",
    "symbol": "W",
    "atomicNumber": 74,
    "periodicNumber": 48,
    "radius_empirical": 1.35,
    "radius_calculated": 1.93,
    "radius_covalent": 1.62,
    "radius_metallic": 1.39,
    "radius_USE": 1.316,
    "mass": 183.84,
    "group": 6,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 6,
    "electronAffinity": 0.81626,
    "wignerSeitzElectronDensity": 5.93,
    "chemicalScale": 1.973,
    "mendeleev_universalSequence": 83,
    "mendeleev_pettifor": 52,
    "mendeleev_modified": 54,
    "workFunction": 4.55,
    "electronegativity_pauling": 2.36,
    "electronegativity_allen": 1.47,
    "ionisationEnergies": [
        770,
        1700
    ],
    "chemicalHardness": 7.05,
    "chemicalPotential": -4.35,
    "meltingTemperature": 3695,
    "boilingTemperature": 6203,
    "fusionEnthalpy": 52.31,
    "vaporisationEnthalpy": 774,
    "molarHeatCapacity": 24.27,
    "phase": "solid",
    "thermalConductivity": 170,
    "thermalExpansion": 0.0000045,
    "crystalStructure": "A2",
    "density": 19.3,
    "cohesiveEnergy": 8.9,
    "debyeTemperature": 312,
    "price": 35.3
})

Rhenium = Element(**{
    "name": "Rhenium",
    "symbol": "Re",
    "atomicNumber": 75,
    "periodicNumber": 51,
    "radius_empirical": 1.35,
    "radius_calculated": 1.88,
    "radius_covalent": 1.51,
    "radius_metallic": 1.37,
    "radius_USE": 1.287,
    "mass": 186.207,
    "group": 7,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 7,
    "electronAffinity": 0.060396,
    "wignerSeitzElectronDensity": 6.33,
    "chemicalScale": 1.735,
    "mendeleev_universalSequence": 65,
    "mendeleev_pettifor": 56,
    "mendeleev_modified": 55,
    "workFunction": 4.72,
    "electronegativity_pauling": 1.9,
    "electronegativity_allen": 1.6,
    "ionisationEnergies": [
        760,
        1260
    ],
    "chemicalHardness": 7.68,
    "chemicalPotential": -4,
    "meltingTemperature": 3459,
    "boilingTemperature": 5903,
    "fusionEnthalpy": 60.43,
    "vaporisationEnthalpy": 704,
    "molarHeatCapacity": 25.48,
    "phase": "solid",
    "thermalConductivity": 48,
    "thermalExpansion": 0.0000062,
    "crystalStructure": "A3",
    "density": 21.02,
    "cohesiveEnergy": 8.03,
    "debyeTemperature": 275,
    "price": 4150
})

Osmium = Element(**{
    "name": "Osmium",
    "symbol": "Os",
    "atomicNumber": 76,
    "periodicNumber": 54,
    "radius_empirical": 1.3,
    "radius_calculated": 1.85,
    "radius_covalent": 1.44,
    "radius_metallic": 1.35,
    "radius_USE": 1.278,
    "mass": 190.23,
    "group": 8,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 8,
    "electronAffinity": 1.0778,
    "wignerSeitzElectronDensity": 6.33,
    "chemicalScale": 1.913,
    "mendeleev_universalSequence": 78,
    "mendeleev_pettifor": 59,
    "mendeleev_modified": 57,
    "workFunction": 5.93,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 1.65,
    "ionisationEnergies": [
        840,
        1600
    ],
    "chemicalHardness": 7.36,
    "chemicalPotential": -4.76,
    "meltingTemperature": 3306,
    "boilingTemperature": 5285,
    "fusionEnthalpy": 31,
    "vaporisationEnthalpy": 378,
    "molarHeatCapacity": 24.7,
    "phase": "solid",
    "thermalConductivity": 87,
    "thermalExpansion": 0.0000051,
    "crystalStructure": "A3",
    "density": 22.59,
    "cohesiveEnergy": 8.17,
    "debyeTemperature": 400,
    "price": 12000
})

Iridium = Element(**{
    "name": "Iridium",
    "symbol": "Ir",
    "atomicNumber": 77,
    "periodicNumber": 57,
    "radius_empirical": 1.35,
    "radius_calculated": 1.8,
    "radius_covalent": 1.41,
    "radius_metallic": 1.355,
    "radius_USE": 1.288,
    "mass": 192.217,
    "group": 9,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 9,
    "electronAffinity": 1.56436,
    "wignerSeitzElectronDensity": 6.13,
    "chemicalScale": 1.905,
    "mendeleev_universalSequence": 77,
    "mendeleev_pettifor": 62,
    "mendeleev_modified": 59,
    "workFunction": 5.67,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 1.68,
    "ionisationEnergies": [
        880,
        1600
    ],
    "chemicalHardness": 7.4,
    "chemicalPotential": -5.27,
    "meltingTemperature": 2719,
    "boilingTemperature": 4403,
    "fusionEnthalpy": 41.12,
    "vaporisationEnthalpy": 564,
    "molarHeatCapacity": 25.1,
    "phase": "solid",
    "thermalConductivity": 150,
    "thermalExpansion": 0.0000064,
    "crystalStructure": "A1",
    "density": 22.56,
    "cohesiveEnergy": 6.94,
    "debyeTemperature": 228,
    "price": 56200
})

Platinum = Element(**{
    "name": "Platinum",
    "symbol": "Pt",
    "atomicNumber": 78,
    "periodicNumber": 60,
    "radius_empirical": 1.35,
    "radius_calculated": 1.77,
    "radius_vanDerWaals": 1.75,
    "radius_covalent": 1.36,
    "radius_metallic": 1.385,
    "radius_USE": 1.311,
    "mass": 195.084,
    "group": 10,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 10,
    "electronAffinity": 2.1251,
    "wignerSeitzElectronDensity": 5.64,
    "chemicalScale": 1.931,
    "mendeleev_universalSequence": 79,
    "mendeleev_pettifor": 65,
    "mendeleev_modified": 61,
    "workFunction": 5.64,
    "electronegativity_pauling": 2.28,
    "electronegativity_allen": 1.72,
    "ionisationEnergies": [
        870,
        1791
    ],
    "chemicalHardness": 6.83,
    "chemicalPotential": -5.54,
    "meltingTemperature": 2041.4,
    "boilingTemperature": 4098,
    "fusionEnthalpy": 22.17,
    "vaporisationEnthalpy": 510,
    "molarHeatCapacity": 25.86,
    "phase": "solid",
    "thermalConductivity": 71,
    "thermalExpansion": 0.0000089,
    "crystalStructure": "A1",
    "density": 21.45,
    "cohesiveEnergy": 5.84,
    "debyeTemperature": 225,
    "price": 27800
})

Gold = Element(**{
    "name": "Gold",
    "symbol": "Au",
    "atomicNumber": 79,
    "periodicNumber": 63,
    "radius_empirical": 1.35,
    "radius_calculated": 1.74,
    "radius_vanDerWaals": 1.66,
    "radius_covalent": 1.36,
    "radius_metallic": 1.44,
    "radius_USE": 1.374,
    "mass": 196.96657,
    "group": 11,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 11,
    "electronAffinity": 2.30861,
    "wignerSeitzElectronDensity": 3.87,
    "chemicalScale": 2.027,
    "mendeleev_universalSequence": 85,
    "mendeleev_pettifor": 67,
    "mendeleev_modified": 63,
    "workFunction": 5.47,
    "electronegativity_pauling": 2.54,
    "electronegativity_allen": 1.92,
    "ionisationEnergies": [
        890.1,
        1980
    ],
    "chemicalHardness": 6.92,
    "chemicalPotential": -5.77,
    "meltingTemperature": 1337.33,
    "boilingTemperature": 3243,
    "fusionEnthalpy": 12.55,
    "vaporisationEnthalpy": 342,
    "molarHeatCapacity": 25.418,
    "phase": "solid",
    "thermalConductivity": 320,
    "thermalExpansion": 0.0000142,
    "crystalStructure": "A1",
    "density": 19.3,
    "cohesiveEnergy": 3.81,
    "debyeTemperature": 178,
    "price": 44800
})

Mercury = Element(**{
    "name": "Mercury",
    "symbol": "Hg",
    "atomicNumber": 80,
    "periodicNumber": 68,
    "radius_empirical": 1.5,
    "radius_calculated": 1.71,
    "radius_vanDerWaals": 1.55,
    "radius_covalent": 1.32,
    "radius_metallic": 1.51,
    "radius_USE": 1.556,
    "mass": 200.592,
    "group": 12,
    "period": 6,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 12,
    "electronAffinity": -0.5,
    "wignerSeitzElectronDensity": 1.91,
    "chemicalScale": 1.571,
    "mendeleev_universalSequence": 54,
    "mendeleev_pettifor": 71,
    "mendeleev_modified": 73,
    "workFunction": 4.5,
    "electronegativity_pauling": 2,
    "electronegativity_allen": 1.765,
    "ionisationEnergies": [
        1007.1,
        1810
    ],
    "chemicalHardness": 10.44,
    "chemicalPotential": -5.22,
    "meltingTemperature": 234.321,
    "boilingTemperature": 629.88,
    "fusionEnthalpy": 2.29,
    "vaporisationEnthalpy": 59.11,
    "molarHeatCapacity": 27.983,
    "phase": "liquid",
    "thermalConductivity": 8.3,
    "thermalExpansion": 0.000181,
    "density": 13.534,
    "cohesiveEnergy": 0.67,
    "debyeTemperature": 92,
    "price": 30.2
})

Thallium = Element(**{
    "name": "Thallium",
    "symbol": "Tl",
    "atomicNumber": 81,
    "periodicNumber": 73,
    "radius_empirical": 1.9,
    "radius_calculated": 1.56,
    "radius_vanDerWaals": 1.96,
    "radius_covalent": 1.45,
    "radius_metallic": 1.7,
    "radius_USE": 1.617,
    "mass": 204.38,
    "group": 13,
    "period": 6,
    "block": "p",
    "series": "poorMetal",
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
    "valenceElectrons": 3,
    "electronAffinity": 0.320053,
    "wignerSeitzElectronDensity": 1.4,
    "chemicalScale": 1.304,
    "mendeleev_universalSequence": 35,
    "mendeleev_pettifor": 75,
    "mendeleev_modified": 78,
    "workFunction": 3.84,
    "electronegativity_pauling": 1.62,
    "electronegativity_allen": 1.789,
    "ionisationEnergies": [
        589.4,
        1971
    ],
    "chemicalHardness": 5.73,
    "chemicalPotential": -3.24,
    "meltingTemperature": 577,
    "boilingTemperature": 1746,
    "fusionEnthalpy": 4.14,
    "vaporisationEnthalpy": 165,
    "molarHeatCapacity": 26.32,
    "phase": "solid",
    "thermalConductivity": 46,
    "thermalExpansion": 0.0000299,
    "crystalStructure": "A3",
    "density": 11.85,
    "cohesiveEnergy": 1.88,
    "debyeTemperature": 96,
    "price": 4200
})

Lead = Element(**{
    "name": "Lead",
    "symbol": "Pb",
    "atomicNumber": 82,
    "periodicNumber": 78,
    "radius_empirical": 1.8,
    "radius_calculated": 1.54,
    "radius_vanDerWaals": 2.02,
    "radius_covalent": 1.46,
    "radius_USE": 1.622,
    "mass": 207.2,
    "group": 14,
    "period": 6,
    "block": "p",
    "series": "poorMetal",
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
    "valenceElectrons": 4,
    "electronAffinity": 0.356721,
    "wignerSeitzElectronDensity": 1.52,
    "chemicalScale": 1.442,
    "mendeleev_universalSequence": 43,
    "mendeleev_pettifor": 79,
    "mendeleev_modified": 79,
    "workFunction": 4.25,
    "electronegativity_pauling": 1.87,
    "electronegativity_allen": 1.854,
    "ionisationEnergies": [
        715.6,
        1450.5
    ],
    "chemicalHardness": 7.05,
    "chemicalPotential": -3.88,
    "meltingTemperature": 600.61,
    "boilingTemperature": 2022,
    "fusionEnthalpy": 4.77,
    "vaporisationEnthalpy": 179.5,
    "molarHeatCapacity": 26.65,
    "phase": "solid",
    "thermalConductivity": 35,
    "thermalExpansion": 0.0000289,
    "crystalStructure": "A1",
    "density": 11.34,
    "cohesiveEnergy": 2.03,
    "debyeTemperature": 87,
    "price": 2
})

Bismuth = Element(**{
    "name": "Bismuth",
    "symbol": "Bi",
    "atomicNumber": 83,
    "periodicNumber": 83,
    "radius_empirical": 1.6,
    "radius_calculated": 1.43,
    "radius_vanDerWaals": 2.07,
    "radius_covalent": 1.48,
    "radius_USE": 1.635,
    "mass": 208.9804,
    "group": 15,
    "period": 6,
    "block": "p",
    "series": "poorMetal",
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
    "valenceElectrons": 5,
    "electronAffinity": 0.942362,
    "wignerSeitzElectronDensity": 1.56,
    "chemicalScale": 1.517,
    "mendeleev_universalSequence": 51,
    "mendeleev_pettifor": 84,
    "mendeleev_modified": 89,
    "workFunction": 4.34,
    "electronegativity_pauling": 2.02,
    "electronegativity_allen": 2.01,
    "ionisationEnergies": [
        703,
        1610
    ],
    "chemicalHardness": 6.34,
    "chemicalPotential": -4.12,
    "meltingTemperature": 544.7,
    "boilingTemperature": 1837,
    "fusionEnthalpy": 11.3,
    "vaporisationEnthalpy": 179,
    "molarHeatCapacity": 25.52,
    "phase": "solid",
    "thermalConductivity": 8,
    "thermalExpansion": 0.0000134,
    "crystalStructure": "rhombohedral",
    "density": 9.78,
    "cohesiveEnergy": 2.18,
    "debyeTemperature": 116,
    "price": 6.36
})

Polonium = Element(**{
    "name": "Polonium",
    "symbol": "Po",
    "atomicNumber": 84,
    "periodicNumber": 88,
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
    "valenceElectrons": 6,
    "electronAffinity": 1.4,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.477,
    "mendeleev_universalSequence": 46,
    "mendeleev_pettifor": 88,
    "mendeleev_modified": 90,
    "workFunction": None,
    "electronegativity_pauling": 2,
    "electronegativity_allen": 2.19,
    "ionisationEnergies": [
        812.1
    ],
    "chemicalHardness": 6.51,
    "chemicalPotential": -5.15,
    "meltingTemperature": 527,
    "boilingTemperature": 1235,
    "fusionEnthalpy": 13,
    "vaporisationEnthalpy": 102.91,
    "molarHeatCapacity": 26.4,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": 0.0000235,
    "crystalStructure": "Ah",
    "density": 9.196,
    "cohesiveEnergy": 1.5,
    "debyeTemperature": None,
    "price": 49200000000000
})

Astatine = Element(**{
    "name": "Astatine",
    "symbol": "At",
    "atomicNumber": 85,
    "periodicNumber": 94,

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
    "valenceElectrons": 7,
    "electronAffinity": 2.41578,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.502,
    "mendeleev_universalSequence": 47,
    "mendeleev_pettifor": 93,
    "mendeleev_modified": 95,
    "workFunction": None,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 2.39,
    "ionisationEnergies": [
        899.003
    ],
    "chemicalHardness": 6.52,
    "chemicalPotential": -6.05,
    "meltingTemperature": 503,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": 54.39,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": 2,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 6.35,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Radon = Element(**{
    "name": "Radon",
    "symbol": "Rn",
    "atomicNumber": 86,
    "periodicNumber": 100,

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
    "valenceElectrons": 8,
    "electronAffinity": -0.7,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 0.871,
    "mendeleev_universalSequence": 11,
    "mendeleev_pettifor": 6,
    "mendeleev_modified": 6,
    "workFunction": None,
    "electronegativity_pauling": 2.2,
    "electronegativity_allen": 2.6,
    "ionisationEnergies": [
        1037
    ],
    "chemicalHardness": 10.75,
    "chemicalPotential": -5.38,
    "meltingTemperature": 202,
    "boilingTemperature": 211.5,
    "fusionEnthalpy": 3.247,
    "vaporisationEnthalpy": 18.1,
    "molarHeatCapacity": 20.786,
    "phase": "gas",
    "thermalConductivity": 0.00361,
    "thermalExpansion": None,
    "density": 0.00973,
    "cohesiveEnergy": 0.202,
    "debyeTemperature": None,
    "price": None
})

Francium = Element(**{
    "name": "Francium",
    "symbol": "Fr",
    "atomicNumber": 87,
    "periodicNumber": 6,

    "radius_vanDerWaals": 3.48,
    "radius_covalent": 2.6,
    "radius_USE": 2.567,
    "mass": 223,
    "group": 1,
    "period": 7,
    "block": "s",
    "series": "alkaliMetal",
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
    "valenceElectrons": 1,
    "electronAffinity": 0.486,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 0,
    "mendeleev_universalSequence": 1,
    "mendeleev_pettifor": 7,
    "mendeleev_modified": 7,
    "workFunction": None,
    "electronegativity_pauling": 0.7,
    "electronegativity_allen": 0.67,
    "ionisationEnergies": [
        380
    ],
    "chemicalHardness": 15.21,
    "chemicalPotential": -2.28,
    "meltingTemperature": 281,
    "boilingTemperature": 890,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A2",
    "density": 2.48,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Radium = Element(**{
    "name": "Radium",
    "symbol": "Ra",
    "atomicNumber": 88,
    "periodicNumber": 10,
    "radius_empirical": 2.15,
    "radius_vanDerWaals": 2.83,
    "radius_covalent": 2.21,
    "radius_USE": 2.114,
    "mass": 226,
    "group": 2,
    "period": 7,
    "block": "s",
    "series": "alkalineEarthMetal",
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
    "valenceElectrons": 2,
    "electronAffinity": 0.1,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 0.486,
    "mendeleev_universalSequence": 5,
    "mendeleev_pettifor": 13,
    "mendeleev_modified": 13,
    "workFunction": None,
    "electronegativity_pauling": 0.9,
    "electronegativity_allen": 0.89,
    "ionisationEnergies": [
        509.3,
        979
    ],
    "chemicalHardness": 5.18,
    "chemicalPotential": -2.69,
    "meltingTemperature": 973,
    "boilingTemperature": 2010,
    "fusionEnthalpy": 8.5,
    "vaporisationEnthalpy": 113,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": 19,
    "thermalExpansion": None,
    "crystalStructure": "A2",
    "density": 5.5,
    "cohesiveEnergy": 1.66,
    "debyeTemperature": 89,
    "price": None
})

Actinium = Element(**{
    "name": "Actinium",
    "symbol": "Ac",
    "atomicNumber": 89,
    "periodicNumber": 14,
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
    "valenceElectrons": 3,
    "electronAffinity": 0.35,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 0.827,
    "mendeleev_universalSequence": 8,
    "mendeleev_pettifor": 45,
    "mendeleev_modified": 33,
    "workFunction": None,
    "electronegativity_pauling": 1.1,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        499,
        1170
    ],
    "chemicalHardness": 4.82,
    "chemicalPotential": -2.76,
    "meltingTemperature": 1500,
    "boilingTemperature": 3500,
    "fusionEnthalpy": 14,
    "vaporisationEnthalpy": 400,
    "molarHeatCapacity": 27.2,
    "phase": "solid",
    "thermalConductivity": 12,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 10.07,
    "cohesiveEnergy": 4.25,
    "debyeTemperature": None,
    "price": 29000000000000
})

Thorium = Element(**{
    "name": "Thorium",
    "symbol": "Th",
    "atomicNumber": 90,
    "periodicNumber": 16,
    "radius_empirical": 1.8,
    "radius_covalent": 2.06,
    "radius_metallic": 1.79,
    "radius_USE": 1.655,
    "mass": 232.0377,
    "group": None,
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
    "valenceElectrons": 4,
    "electronAffinity": 0.60769,
    "wignerSeitzElectronDensity": 2.1,
    "chemicalScale": 1.091,
    "mendeleev_universalSequence": 21,
    "mendeleev_pettifor": 44,
    "mendeleev_modified": 34,
    "workFunction": 3.4,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        587,
        1110
    ],
    "chemicalHardness": 5.94,
    "chemicalPotential": -3.35,
    "meltingTemperature": 2023,
    "boilingTemperature": 5061,
    "fusionEnthalpy": 13.81,
    "vaporisationEnthalpy": 514,
    "molarHeatCapacity": 26.23,
    "phase": "solid",
    "thermalConductivity": 54,
    "thermalExpansion": 0.000011,
    "crystalStructure": "A1",
    "density": 11.724,
    "cohesiveEnergy": 6.2,
    "debyeTemperature": 100,
    "price": 287
})

Protactinium = Element(**{
    "name": "Protactinium",
    "symbol": "Pa",
    "atomicNumber": 91,
    "periodicNumber": 18,
    "radius_empirical": 1.8,
    "radius_covalent": 2,
    "radius_metallic": 1.63,
    "radius_USE": 1.436,
    "mass": 231.03588,
    "group": None,
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
    "valenceElectrons": 5,
    "electronAffinity": 0.55,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.385,
    "mendeleev_universalSequence": 36,
    "mendeleev_pettifor": 43,
    "mendeleev_modified": 35,
    "workFunction": None,
    "electronegativity_pauling": 1.5,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        568,
        1128
    ],
    "chemicalHardness": 5.51,
    "chemicalPotential": -3.14,
    "meltingTemperature": 1841,
    "boilingTemperature": 4300,
    "fusionEnthalpy": 12.34,
    "vaporisationEnthalpy": 481,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": 47,
    "thermalExpansion": 0.00001,
    "crystalStructure": "Aa",
    "density": 15.37,
    "cohesiveEnergy": None,
    "debyeTemperature": 262,
    "price": 280000
})

Uranium = Element(**{
    "name": "Uranium",
    "symbol": "U",
    "atomicNumber": 92,
    "periodicNumber": 20,
    "radius_empirical": 1.75,
    "radius_vanDerWaals": 1.86,
    "radius_covalent": 1.96,
    "radius_metallic": 1.56,
    "radius_USE": 1.339,
    "mass": 238.02891,
    "group": None,
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
    "valenceElectrons": 6,
    "electronAffinity": 0.53,
    "wignerSeitzElectronDensity": 3.44,
    "chemicalScale": 1.397,
    "mendeleev_universalSequence": 38,
    "mendeleev_pettifor": 42,
    "mendeleev_modified": 36,
    "workFunction": 3.63,
    "electronegativity_pauling": 1.38,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        597.6,
        1420
    ],
    "chemicalHardness": 5.82,
    "chemicalPotential": -3.29,
    "meltingTemperature": 1405.3,
    "boilingTemperature": 4404,
    "fusionEnthalpy": 9.14,
    "vaporisationEnthalpy": 417.1,
    "molarHeatCapacity": 27.665,
    "phase": "solid",
    "thermalConductivity": 27,
    "thermalExpansion": 0.0000139,
    "crystalStructure": "A20",
    "density": 19.1,
    "cohesiveEnergy": 5.55,
    "debyeTemperature": 300,
    "price": 101
})

Neptunium = Element(**{
    "name": "Neptunium",
    "symbol": "Np",
    "atomicNumber": 93,
    "periodicNumber": 22,
    "radius_empirical": 1.75,
    "radius_covalent": 1.9,
    "radius_metallic": 1.55,
    "radius_USE": 1.291,
    "mass": 237,
    "group": None,
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
    "valenceElectrons": 7,
    "electronAffinity": 0.48,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.425,
    "mendeleev_universalSequence": 41,
    "mendeleev_pettifor": 41,
    "mendeleev_modified": 37,
    "workFunction": None,
    "electronegativity_pauling": 1.36,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        604.5,
        1128
    ],
    "chemicalHardness": 5.95,
    "chemicalPotential": -3.29,
    "meltingTemperature": 912,
    "boilingTemperature": 4447,
    "fusionEnthalpy": 5.19,
    "vaporisationEnthalpy": 336,
    "molarHeatCapacity": 29.46,
    "phase": "solid",
    "thermalConductivity": 6,
    "thermalExpansion": None,
    "crystalStructure": "Ac",
    "density": 19.38,
    "cohesiveEnergy": 4.73,
    "debyeTemperature": 163,
    "price": 660000
})

Plutonium = Element(**{
    "name": "Plutonium",
    "symbol": "Pu",
    "atomicNumber": 94,
    "periodicNumber": 24,
    "radius_empirical": 1.75,
    "radius_covalent": 1.87,
    "radius_metallic": 1.59,
    "radius_USE": 1.271,
    "mass": 244,
    "group": None,
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
    "valenceElectrons": 8,
    "electronAffinity": -0.5,
    "wignerSeitzElectronDensity": 2.99,
    "chemicalScale": 1.396,
    "mendeleev_universalSequence": 37,
    "mendeleev_pettifor": 40,
    "mendeleev_modified": 38,
    "workFunction": None,
    "electronegativity_pauling": 1.28,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        584.7,
        1128
    ],
    "chemicalHardness": 5.94,
    "chemicalPotential": -3.07,
    "meltingTemperature": 912.5,
    "boilingTemperature": 3505,
    "fusionEnthalpy": 2.82,
    "vaporisationEnthalpy": 333.5,
    "molarHeatCapacity": 35.5,
    "phase": "solid",
    "thermalConductivity": 6,
    "thermalExpansion": 0.0000467,
    "crystalStructure": "aPu",
    "density": 19.85,
    "cohesiveEnergy": 3.6,
    "debyeTemperature": 176,
    "price": 6490000
})

Americium = Element(**{
    "name": "Americium",
    "symbol": "Am",
    "atomicNumber": 95,
    "periodicNumber": 26,
    "radius_empirical": 1.75,
    "radius_covalent": 1.8,
    "radius_metallic": 1.73,
    "radius_USE": 1.261,
    "mass": 243,
    "group": None,
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
    "valenceElectrons": 9,
    "electronAffinity": 0.1,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.416,
    "mendeleev_universalSequence": 40,
    "mendeleev_pettifor": 39,
    "mendeleev_modified": 39,
    "workFunction": None,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        578.1158
    ],
    "chemicalHardness": 5.9,
    "chemicalPotential": -3.03,
    "meltingTemperature": 1449,
    "boilingTemperature": 2880,
    "fusionEnthalpy": 14.39,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": 28,
    "phase": "solid",
    "thermalConductivity": 10,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 12,
    "cohesiveEnergy": 2.73,
    "debyeTemperature": None,
    "price": 750000
})

Curium = Element(**{
    "name": "Curium",
    "symbol": "Cm",
    "atomicNumber": 96,
    "periodicNumber": 28,
    "radius_empirical": 1.76,
    "radius_covalent": 1.69,
    "radius_metallic": 1.74,
    "radius_USE": 1.279,
    "mass": 247,
    "group": None,
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
    "valenceElectrons": 10,
    "electronAffinity": 0.28,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": 1.401,
    "mendeleev_universalSequence": 39,
    "mendeleev_pettifor": 38,
    "mendeleev_modified": 40,
    "workFunction": None,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        581,
        1196
    ],
    "chemicalHardness": 5.67,
    "chemicalPotential": -3.16,
    "meltingTemperature": 1613,
    "boilingTemperature": 3383,
    "fusionEnthalpy": 13.85,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 13.51,
    "cohesiveEnergy": 3.99,
    "debyeTemperature": None,
    "price": 160000000000
})

Berkelium = Element(**{
    "name": "Berkelium",
    "symbol": "Bk",
    "atomicNumber": 97,
    "periodicNumber": 30,
    "radius_metallic": 1.7,
    "mass": 247,
    "group": None,
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
    "valenceElectrons": 11,
    "electronAffinity": -1.72,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": 37,
    "mendeleev_modified": 41,
    "workFunction": None,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        601,
        1186
    ],
    "chemicalHardness": 6.17,
    "chemicalPotential": -3.12,
    "meltingTemperature": 1259,
    "boilingTemperature": 2900,
    "fusionEnthalpy": 7.92,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": 10,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 14.78,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": 185000000000
})

Californium = Element(**{
    "name": "Californium",
    "symbol": "Cf",
    "atomicNumber": 98,
    "periodicNumber": 32,

    "radius_metallic": 1.86,
    "mass": 251,
    "group": None,
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
    "valenceElectrons": 12,
    "electronAffinity": -1.01,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": 36,
    "mendeleev_modified": 42,
    "workFunction": None,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        608,
        1206
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 1173,
    "boilingTemperature": 1743,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 15.1,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": 185000000000
})

Einsteinium = Element(**{
    "name": "Einsteinium",
    "symbol": "Es",
    "atomicNumber": 99,
    "periodicNumber": 34,

    "radius_metallic": 1.86,
    "mass": 252,
    "group": None,
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
    "valenceElectrons": 13,
    "electronAffinity": -0.3,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": 35,
    "mendeleev_modified": 43,
    "workFunction": None,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        619,
        1216
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 1133,
    "boilingTemperature": 1269,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 8.84,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Fermium = Element(**{
    "name": "Fermium",
    "symbol": "Fm",
    "atomicNumber": 100,
    "periodicNumber": 36,
    "mass": 257,
    "group": None,
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
    "valenceElectrons": 14,
    "electronAffinity": 0.35,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": 34,
    "mendeleev_modified": 44,
    "workFunction": None,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        627,
        1225
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 1800,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 9.71,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Mendelevium = Element(**{
    "name": "Mendelevium",
    "symbol": "Md",
    "atomicNumber": 101,
    "periodicNumber": None,
    "mass": 258,
    "group": None,
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
    "valenceElectrons": 15,
    "electronAffinity": 0.98,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        635,
        1235
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 1100,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 10.37,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Nobelium = Element(**{
    "name": "Nobelium",
    "symbol": "No",
    "atomicNumber": 102,
    "periodicNumber": None,
    "mass": 259,
    "group": None,
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
    "valenceElectrons": 16,
    "electronAffinity": -2.33,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": 1.3,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        642,
        1254
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 1100,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 9.94,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Lawrencium = Element(**{
    "name": "Lawrencium",
    "symbol": "Lr",
    "atomicNumber": 103,
    "periodicNumber": None,
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
    "valenceElectrons": 3,
    "electronAffinity": -0.31,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        470,
        1428
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 1900,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 16,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Rutherfordium = Element(**{
    "name": "Rutherfordium",
    "symbol": "Rf",
    "atomicNumber": 104,
    "periodicNumber": None,
    "mass": 267,
    "group": 4,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 4,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        580,
        1390
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 2400,
    "boilingTemperature": 5800,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 23.2,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Dubnium = Element(**{
    "name": "Dubnium",
    "symbol": "Db",
    "atomicNumber": 105,
    "periodicNumber": None,
    "mass": 270,
    "group": 5,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 5,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        665,
        1547
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": None,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A2",
    "density": 29.3,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Seaborgium = Element(**{
    "name": "Seaborgium",
    "symbol": "Sg",
    "atomicNumber": 106,
    "periodicNumber": None,
    "mass": 269,
    "group": 6,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 6,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        757,
        1733
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": None,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A2",
    "density": 35,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Bohrium = Element(**{
    "name": "Seaborgium",
    "symbol": "Sg",
    "atomicNumber": 106,
    "periodicNumber": None,
    "mass": 269,
    "group": 6,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valenceElectrons": 6,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        757,
        1733
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": None,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A2",
    "density": 35,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})
Hassium = Element(**{
    "name": "Hassium",
    "symbol": "Hs",
    "atomicNumber": 108,
    "periodicNumber": None,
    "mass": 270,
    "group": 8,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valence": None,
    "valenceElectrons": 8,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        730,
        1760
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": None,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 41,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Meitnerium = Element(**{
    "name": "Meitnerium",
    "symbol": "Mt",
    "atomicNumber": 109,
    "periodicNumber": None,
    "mass": 278,
    "group": 9,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valence": None,
    "valenceElectrons": 9,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        800,
        1820
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": None,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 37.4,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Darmstadtium = Element(**{
    "name": "Darmstadtium",
    "symbol": "Ds",
    "atomicNumber": 110,
    "periodicNumber": None,
    "mass": 281,
    "group": 10,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valence": None,
    "valenceElectrons": 10,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        960,
        1890
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": None,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A2",
    "density": 34.8,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Roentgenium = Element(**{
    "name": "Roentgenium",
    "symbol": "Rg",
    "atomicNumber": 111,
    "periodicNumber": None,
    "mass": 281,
    "group": 11,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valence": None,
    "valenceElectrons": 11,
    "electronAffinity": 1.565,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        1020,
        2070
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": None,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A2",
    "density": 28.7,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Copernicium = Element(**{
    "name": "Copernicium",
    "symbol": "Cn",
    "atomicNumber": 112,
    "periodicNumber": None,
    "mass": 285,
    "group": 12,
    "period": 7,
    "block": "d",
    "series": "transitionMetal",
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
    "valence": None,
    "valenceElectrons": 12,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        1155,
        2170
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 283,
    "boilingTemperature": 340,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 14,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Nihonium = Element(**{
    "name": "Nihonium",
    "symbol": "Nh",
    "atomicNumber": 113,
    "periodicNumber": None,
    "mass": 286,
    "group": 13,
    "period": 7,
    "block": "p",
    "series": "poorMetal",
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
    "valence": None,
    "valenceElectrons": 3,
    "electronAffinity": 0.69,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        707.2,
        2309
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 700,
    "boilingTemperature": 1430,
    "fusionEnthalpy": 7.61,
    "vaporisationEnthalpy": 130,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A3",
    "density": 16,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Flerovium = Element(**{
    "name": "Flerovium",
    "symbol": "Fl",
    "atomicNumber": 114,
    "periodicNumber": None,
    "mass": 289,
    "group": 14,
    "period": 7,
    "block": "p",
    "series": "poorMetal",
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
    "valence": None,
    "valenceElectrons": 4,
    "electronAffinity": None,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        832.2,
        1600
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 210,
    "boilingTemperature": None,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": 38,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 14,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Moscovium = Element(**{
    "name": "Moscovium",
    "symbol": "Mc",
    "atomicNumber": 115,
    "periodicNumber": None,
    "mass": 289,
    "group": 15,
    "period": 7,
    "block": "p",
    "series": "poorMetal",
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
    "valence": None,
    "valenceElectrons": 5,
    "electronAffinity": 0.366,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        538.3,
        1760
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 670,
    "boilingTemperature": 1400,
    "fusionEnthalpy": 5.9,
    "vaporisationEnthalpy": 138,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": None,
    "density": 13.5,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Livermorium = Element(**{
    "name": "Livermorium",
    "symbol": "Lv",
    "atomicNumber": 116,
    "periodicNumber": None,
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
    "valence": None,
    "valenceElectrons": 6,
    "electronAffinity": 0.776,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        663.9,
        1330
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 700,
    "boilingTemperature": 1100,
    "fusionEnthalpy": 7.61,
    "vaporisationEnthalpy": 42,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": None,
    "density": 12.9,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Tennessine = Element(**{
    "name": "Tennessine",
    "symbol": "Ts",
    "atomicNumber": 117,
    "periodicNumber": None,
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
    "valence": None,
    "valenceElectrons": 7,
    "electronAffinity": 1.719,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        736.9,
        1435.4
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 700,
    "boilingTemperature": 883,
    "fusionEnthalpy": None,
    "vaporisationEnthalpy": None,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": None,
    "density": 7.2,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
})

Oganesson = Element(**{
    "name": "Oganesson",
    "symbol": "Og",
    "atomicNumber": 118,
    "periodicNumber": None,
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
    "valence": None,
    "valenceElectrons": 8,
    "electronAffinity": 0.056,
    "wignerSeitzElectronDensity": None,
    "chemicalScale": None,
    "mendeleev_universalSequence": None,
    "mendeleev_pettifor": None,
    "mendeleev_modified": None,
    "workFunction": None,
    "electronegativity_pauling": None,
    "electronegativity_allen": None,
    "ionisationEnergies": [
        860.1,
        1560
    ],
    "chemicalHardness": None,
    "chemicalPotential": None,
    "meltingTemperature": 325,
    "boilingTemperature": 450,
    "fusionEnthalpy": 23.5,
    "vaporisationEnthalpy": 19.4,
    "molarHeatCapacity": None,
    "phase": "solid",
    "thermalConductivity": None,
    "thermalExpansion": None,
    "crystalStructure": "A1",
    "density": 5,
    "cohesiveEnergy": None,
    "debyeTemperature": None,
    "price": None
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
