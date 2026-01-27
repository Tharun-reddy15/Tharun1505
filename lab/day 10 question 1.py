# =========================
# PYTEST UNIT TESTING DEMO
# =========================

# ---------- Application Code ----------
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# ---------- Pytest Test Cases ----------
# File name should be: test_calculator.py
# Pytest automatically discovers files starting with test_

def test_addition():
    assert add(3, 4) == 7

def test_division():
    assert divide(10, 2) == 5

def test_division_by_zero_exception():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)


# ---------- Test Execution ----------
# Run tests using the command:
# pytest