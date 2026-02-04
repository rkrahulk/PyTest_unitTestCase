import pytest
from class_Calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, -2) == -3
    assert calculator.add(0, 0) == 0

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(-5, -3) == -2
    assert calculator.subtract(0, 0) == 0

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, -3) == 6
    assert calculator.multiply(0, 5) == 0

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2.0
    assert calculator.divide(-6, -3) == 2.0
    assert calculator.divide(0, 1) == 0.0

    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calculator.divide(1, 0)