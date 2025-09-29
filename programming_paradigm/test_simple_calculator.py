# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a new calculator for each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3, places=1)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertIsNone(self.calc.divide(0, 0))  # 0 / 0 is undefined

if __name__ == "__main__":
    unittest.main()
