import pytest
from class_Calculator.class_Calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-1, -2) == -3
    assert calc.add(0, 0) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-5, -3) == -2

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2.0
    assert calc.divide(-6, 3) == -2.0
    assert calc.divide(0, 1) == 0.0
    with pytest.raises(ValueError):
        calc.divide(1, 0)