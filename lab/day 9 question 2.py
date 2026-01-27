import unittest

# =====================
# Calculator Functions
# =====================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# =====================
# Unit Test Cases (TDD)
# =====================

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiply(5, 3), 15)

    def test_division(self):
        self.assertEqual(divide(6, 3), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


# =====================
# Run Tests
# =====================

if __name__ == "__main__":
    unittest.main()