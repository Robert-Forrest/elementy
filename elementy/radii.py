import numpy as np


def calculate_radius(element):

    if 'radius_USE' in element.__dict__:
        return element.__dict__['radius_USE']
    elif('radius_empirical' in element.__dict__):
        return element.__dict__['radius_empirical']
    elif('radius_metallic' in element.__dict__):
        return element.__dict__['radius_metallic']
    elif('radius_covalent' in element.__dict__):
        return element.__dict__['radius_covalent']


def calculate_atomic_volume(element):
    if element.radius is not None:
        return (4. / 3.) * np.pi * element.radius**3
