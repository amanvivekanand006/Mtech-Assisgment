import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_sub():
    assert calculator.sub(5, 2) == 3

def test_mul():
    assert calculator.mul(3, 4) == 12

def test_div():
    assert calculator.div(10, 2) == 5
