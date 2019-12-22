import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_results(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(7, 3), 21)
        self.assertEqual(self.calculator.result, 21)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(9, 0), "Dividend cannot be zero.")
        self.assertEqual(self.calculator.result, "Dividend cannot be zero.")


if __name__ == '__main__':
    unittest.main()
