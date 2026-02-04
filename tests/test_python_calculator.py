import pytest
from Python_Script.python_calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add_positive_numbers(calc):
    assert calc.add(2, 3) == 5

def test_add_negative_numbers(calc):
    assert calc.add(-2, -3) == -5

def test_add_zero(calc):
    assert calc.add(0, 0) == 0
    assert calc.add(5, 0) == 5
    assert calc.add(0, 5) == 5

def test_subtract_positive_numbers(calc):
    assert calc.subtract(5, 3) == 2

def test_subtract_negative_numbers(calc):
    assert calc.subtract(-5, -3) == -2

def test_subtract_resulting_negative(calc):
    assert calc.subtract(3, 5) == -2

def test_subtract_zero(calc):
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(5, 0) == 5
    assert calc.subtract(0, 5) == -5

def test_multiply_positive_numbers(calc):
    assert calc.multiply(2, 3) == 6

def test_multiply_negative_numbers(calc):
    assert calc.multiply(-2, -3) == 6
    assert calc.multiply(-2, 3) == -6

def test_multiply_by_zero(calc):
    assert calc.multiply(0, 5) == 0
    assert calc.multiply(5, 0) == 0

def test_divide_positive_numbers(calc):
    assert calc.divide(6, 3) == 2.0

def test_divide_negative_numbers(calc):
    assert calc.divide(-6, -3) == 2.0
    assert calc.divide(-6, 3) == -2.0

def test_divide_result_float(calc):
    assert calc.divide(7, 2) == 3.5

def test_divide_by_zero_raises(calc):
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calc.divide(5, 0)
