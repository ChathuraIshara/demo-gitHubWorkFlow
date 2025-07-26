import unittest
from app import add, subtract, multiply, divide, is_even, factorial


class TestCalculator(unittest.TestCase):
    """Test cases for the calculator functions"""

    def test_add(self):
        """Test addition function"""
        self.assertEqual(add(2, 3), 9)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -3), -8)

    def test_subtract(self):
        """Test subtraction function"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -7), 4)
        self.assertEqual(subtract(10, 10), 0)

    def test_multiply(self):
        """Test multiplication function"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-3, -4), 12)

    def test_divide(self):
        """Test division function"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-8, 4), -2)
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_is_even(self):
        """Test even number checker"""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-7))

    def test_factorial(self):
        """Test factorial function"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)

    def test_factorial_negative(self):
        """Test factorial with negative number raises error"""
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
