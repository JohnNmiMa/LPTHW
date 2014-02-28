# -*- coding: utf-8 -*-
import unittest
from calculator import Calculator
 
class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        print "Instantiated a Calculator into the calc variable"
 
    def test_calculator_add_method_returns_correct_result(self):
        #calc = Calculator()
        result = self.calc.add(2,2)
        self.assertEqual(4, result)
        print "Tested calc.add(2,2)"
 
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        print "Tested calc.add('two','three')"
 
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
        print "Tested calc.add('two',3)"
 
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        print "Tested calc.add(2,'three')"
