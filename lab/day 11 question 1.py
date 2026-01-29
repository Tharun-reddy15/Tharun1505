def add(a, b):
    return a + b

def divide(a, b):
    return a / b

[pytest]
markers =
    slow: marks tests as slow
    skip_test: marks tests to be skipped
    xfail_test: marks tests expected to fail

testpaths = tests

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against (dev/stage/prod)"
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

import pytest
from calculator import add, divide

# -------------------------------
# PARAMETERIZED TEST
# -------------------------------
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
    ]
)
def test_addition(a, b, expected):
    assert add(a, b) == expected


# -------------------------------
# SKIP TEST
# -------------------------------
@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert True


# -------------------------------
# XFAIL TEST
# -------------------------------
@pytest.mark.xfail(reason="Division by zero not handled yet")
def test_divide_by_zero():
    divide(10, 0)


# -------------------------------
# USING CUSTOM CLI OPTION
# -------------------------------
def test_environment(env):
    print(f"Running tests in {env} environment")
    assert env in ["dev", "stage", "prod"]


# -------------------------------
# CONDITIONAL SKIP
# -------------------------------
@pytest.mark.skipif(
    condition=True,
    reason="Condition met, skipping test"
)
def test_conditional_skip():
    assert add(2, 2) == 4


