# Import all necessary modules and libraries
import pytest

# Create a parametized Pytest decorator
@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)])

# Parametrized Test able to take multiple different arguments in the same format
def test_multiplication(a, b, expected):
    assert a * b == expected

# Create a Test that will intentionally caues a failure
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):      # Catching the desired failure == Passing Test Case
        1 / 0

# Simple Addition Test
def test_addition():
    assert 1 + 1 == 2

# Simple Subtraction Test
def test_subtraction():
    diff = 1 - 1
    assert diff == 0