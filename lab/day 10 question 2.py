import pytest

# =========================
# APPLICATION CODE
# =========================

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b


# =========================
# FIXTURES
# =========================

@pytest.fixture(scope="function")
def sample_number():
    return 4, 2

@pytest.fixture(scope="function")
def sample_numbers():
    return 10, 5

@pytest.fixture(scope="module")
def calculator_resource():
    print("\n[SETUP] Calculator Resource Created")
    yield
    print("\n[TEARDOWN] Calculator Resource Closed")


# =========================
# xUnit STYLE METHODS
# =========================

def setup_module(module):
    print("\n[SETUP MODULE] All-in-one Test File")

def teardown_module(module):
    print("\n[TEARDOWN MODULE] All-in-one Test File")

def setup_function(function):
    print("\n[SETUP FUNCTION]")

def teardown_function(function):
    print("\n[TEARDOWN FUNCTION]")


# =========================
# TEST CASES
# =========================

def test_addition(sample_numbers, calculator_resource):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_subtraction(sample_numbers):
    a, b = sample_numbers
    assert sub(a, b) == 5

def test_multiplication(sample_numbers):
    a, b = sample_numbers
    assert mul(a, b) == 50

def test_division(sample_number):
    a, b = sample_number
    assert divide(a, b) == 2

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)






