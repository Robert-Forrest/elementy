import elementy.elements as elements


def test_element_symbol():

    assert elements.Hydrogen.symbol == "H"
    assert elements.Iron.symbol == "Fe"
    assert elements.Uranium.symbol == "U"


def test_element_atomic_number():

    assert elements.Hydrogen.atomic_number == 1
    assert elements.Iron.atomic_number == 26
    assert elements.Uranium.atomic_number == 92
