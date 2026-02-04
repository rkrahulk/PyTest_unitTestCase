import pytest
from Python_Script.python_calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add_positive_numbers(calculator):
    assert calculator.add(2, 3) == 5

def test_add_negative_numbers(calculator):
    assert calculator.add(-2, -3) == -5

def test_add_zero(calculator):
    assert calculator.add(0, 5) == 5
    assert calculator.add(5, 0) == 5

def test_subtract_positive_numbers(calculator):
    assert calculator.subtract(5, 3) == 2

def test_subtract_negative_numbers(calculator):
    assert calculator.subtract(-5, -3) == -2

def test_subtract_resulting_zero(calculator):
    assert calculator.subtract(3, 3) == 0

def test_multiply_positive_numbers(calculator):
    assert calculator.multiply(2, 3) == 6

def test_multiply_negative_numbers(calculator):
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(2, -3) == -6
    assert calculator.multiply(-2, -3) == 6

def test_multiply_by_zero(calculator):
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(5, 0) == 0

def test_divide_positive_numbers(calculator):
    assert calculator.divide(6, 3) == 2.0

def test_divide_negative_numbers(calculator):
    assert calculator.divide(-6, 3) == -2.0
    assert calculator.divide(6, -3) == -2.0
    assert calculator.divide(-6, -3) == 2.0

def test_divide_resulting_float(calculator):
    assert calculator.divide(7, 2) == 3.5

def test_divide_by_zero_raises(calculator):
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calculator.divide(5, 0)
