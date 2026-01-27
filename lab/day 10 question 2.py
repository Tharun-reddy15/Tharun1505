
# ----------------------
# app.py
# ----------------------
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


# ----------------------
# conftest.py
# ----------------------
import pytest

@pytest.fixture(scope="function")
def numbers():
    return 10, 5

@pytest.fixture(scope="module")
def shared_resource():
    print("\n[SETUP] Shared resource")
    resource = {"env": "QA"}
    yield resource
    print("\n[TEARDOWN] Shared resource")


# ----------------------
# test_calculator_one.py
# ----------------------
from app import add, divide

def setup_module(module):
    print("\n[setup_module]")

def teardown_module(module):
    print("\n[teardown_module]")

def setup_function(function):
    print("\n[setup_function]")

def teardown_function(function):
    print("\n[teardown_function]")

def test_addition(numbers, shared_resource):
    a, b = numbers
    assert add(a, b) == 15

def test_division(numbers):
    a, b = numbers
    assert divide(a, b) == 2


# ----------------------
# test_calculator_two.py
# ----------------------
import pytest
from app import divide

def test_division_by_zero(shared_resource):
    with pytest.raises(ValueError):
        divide(10, 0)


