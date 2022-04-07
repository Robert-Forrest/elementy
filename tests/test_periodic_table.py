from elementy import PeriodicTable


def test_periodic_table_elements():
    pt = PeriodicTable()

    assert "H" in pt.elements

    assert len(list(pt.elements.keys())) == 118
