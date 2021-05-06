import unittest
from replace_currency.__init__ import replace_currency_symbols


class TestReplaceCurrencySymbols(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["10 $","100 £"]
        self.expected_output_strings = ["10 USD","100 GBP"]
        self.opts = [
            {
                "token":'USD'
            },
            {
                "token": 'GBP'
            }
        ]

    def test_replace_currency_symbols(self):
        ouput_list = [replace_currency_symbols(string,self.opts[index]) for index,string in enumerate(self.input_strings)]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
