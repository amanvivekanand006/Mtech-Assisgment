import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_sub():
    assert calculator.subtract(5, 2) == 3

def test_mul():
    assert calculator.multiply(3, 4) == 12

def test_div():
    assert calculator.divide(10, 2) == 5
