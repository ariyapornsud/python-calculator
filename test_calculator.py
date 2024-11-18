import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)  # 1 + 2 = 3

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, 2), 1)  # -1 + 2 = 1

    # Test cases for subtract()
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1) 

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(2, -3), 5)  # -3 - 2 = 5

    # Test cases for multiply()
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)  # 2 * 3 = 6

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)  # 0 * 5 = 0

    # Test cases for divide()
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  # 10 // 2 = 5

    def test_divide_edge_case(self):
        self.assertEqual(self.calc.divide(0, 5), 0)  # 0 // 5 = 0

    # Test cases for modulo()
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  # 10 % 3 = 1

    def test_modulo_zero_case(self):
        self.assertEqual(self.calc.modulo(5, 5), 0)  # 5 % 5 = 0

if __name__ == '__main__':
    unittest.main()
