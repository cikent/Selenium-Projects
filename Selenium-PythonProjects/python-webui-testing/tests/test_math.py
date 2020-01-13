# import modules
import pytest

# simple test for addition
def test_addition():
    assert 1 + 1 == 2

# simple test for subtraction
def test_subtraction():
    diff = 1 - 1
    assert diff == 0

# parametrized pytest test
@pytest.mark.parametrize(
    "a, b, expected",
    [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)])
# simple test for multiplication
def test_multiplication(a, b, expected):
    assert a * b == expected

# simple test for division
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
