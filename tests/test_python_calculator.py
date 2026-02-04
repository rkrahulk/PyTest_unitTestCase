import pytest
from Python_Script.python_calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add_positive(calc):
    assert calc.add(2, 3) == 5

def test_add_negative(calc):
    assert calc.add(-2, -3) == -5

def test_add_zero(calc):
    assert calc.add(0, 0) == 0

def test_subtract_positive(calc):
    assert calc.subtract(5, 3) == 2

def test_subtract_negative(calc):
    assert calc.subtract(-5, -3) == -2

def test_subtract_zero(calc):
    assert calc.subtract(0, 0) == 0

def test_multiply_positive(calc):
    assert calc.multiply(4, 3) == 12

def test_multiply_negative(calc):
    assert calc.multiply(-4, 3) == -12

def test_multiply_zero(calc):
    assert calc.multiply(0, 100) == 0

def test_divide_positive(calc):
    assert calc.divide(10, 2) == 5.0

def test_divide_negative(calc):
    assert calc.divide(-10, 2) == -5.0

def test_divide_float(calc):
    assert calc.divide(7, 2) == 3.5

def test_divide_by_zero_raises(calc):
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calc.divide(10, 0)
