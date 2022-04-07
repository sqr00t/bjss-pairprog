import unittest
from unittest.mock import patch
from helpers import functions

class test_funcs(unittest.TestCase):
    
    @patch('helpers.functions.get_input', return_value=100000)
    def test_input_is_int(self, input):
        """Tests user input is int"""
        self.assertTrue(type(functions.get_input()) is int)

    def test_get_tax_amount(self):
        """Tests result of tax calculation given user input"""
        #setup
        house_price = 250000
        multiplier = 0.02
        
        expected = 5000
        
        #result
        self.assertEqual(functions.get_tax_amount(house_price, multiplier), expected)
        

if __name__ == '__main__':
    unittest.main()

