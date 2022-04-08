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
        self.assertEqual(functions.get_tax_amount(295000), 4750)
        self.assertEqual(functions.get_tax_amount(124000), 0)
        self.assertEqual(functions.get_tax_amount(500000), 15000)    
        self.assertEqual(functions.get_tax_amount(700000), 25000)
        #self.assertEqual(functions.get_tax_amount(1000000), 43750)
        #self.assertEqual(functions.get_tax_amount(10000000), 1113750)
        self.assertEqual(functions.get_tax_amount(250000), 2500)
        self.assertEqual(functions.get_tax_amount(125000), 0)
        

if __name__ == '__main__':
    unittest.main()

