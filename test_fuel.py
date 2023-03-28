from Fuel import precentage_counter

def test_precentage():
    assert precentage_counter(3, 4) == 0.75
    assert precentage_counter(1, 100) == 0.01
    assert precentage_counter(99, 100) == 0.99
    assert precentage_counter(4, 4) == 1.00
    assert precentage_counter(1, 4) == 0.25
