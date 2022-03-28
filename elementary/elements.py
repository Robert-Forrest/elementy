from elementary.element import Element

Hydrogen = Element(**{
    "name": "Hydrogen",
    "symbol": "H",
    "atomicNumber": 1,
    "periodicNumber": 89,
    "radius_empirical": 0.25,
    "radius_calculated": 0.53,
    "radius_vanDerWaals": 1.2,
    "radius_covalent": 0.31,
    "radius_USE": 0.727,
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


ELEMENTS = [
    Hydrogen
]


def get_elements():
    return ELEMENTS
