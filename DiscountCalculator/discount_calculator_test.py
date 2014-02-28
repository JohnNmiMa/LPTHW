import unittest
import pdb
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

    def invalid_discount_type_test(self):
        #pdb.set_trace()
        discount_calculator = DiscountCalculator()
        self.assertRaises(ValueError, discount_calculator.calculate, 250,5,'dollar')

    def float_value_for_total_and_discount_test(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(50.0,5.5,'percent')
        self.assertEqual(2.75, result)

    def excessive_discount_test(self):
        discount_calculator = DiscountCalculator()
        self.assertRaises(ValueError, discount_calculator.calculate, 50,101,'percent')
        self.assertRaises(ValueError, discount_calculator.calculate, 50,50.1,'absolute')
        assert discount_calculator.calculate(100,10,'percent') == 10
        self.assertTrue(discount_calculator.calculate(100,10,'percent') == 10)
        self.assertIn('calculate', 'discount_calculateor')
        self.assertIsInstance(discount_calculator, DiscountCalculator)
    
if __name__ == '__main__':
    dct = DiscountCalculatorTests()
    dct.invalid_discount_type_test()

