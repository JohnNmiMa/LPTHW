import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
    def test_ten_percent_discount(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100,10,'percent')
        self.assertEqual(10.0, result)

    def fifteen_percent_discount_test(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100,15,'percent')
        self.assertEqual(15.0, result)

    def five_dollar_discount_test(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(250,5,'absolute')
        self.assertEqual(5, result)
    
