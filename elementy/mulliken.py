import numpy as np


def calculate_mulliken_electronegativity(element):
    if(element.electron_affinity is not None and
       element.ionisation_energies is not None):
        return 0.5 * np.abs(element.electron_affinity +
                            (element.ionisation_energies[0] / 96.485))
    else:
        return None
