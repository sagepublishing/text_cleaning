import unittest
from replace_digits.__init__ import replace_digits


class TestReplaceDigits(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["Age: 3","9 cars"]
        self.expected_output_strings = ["Age: three","Nine cars"]
        self.opts = [
            {
                "token":'three'
            },
            {
                "token": 'Nine'
            }
        ]

    def test_replace_digits(self):
        ouput_list = [replace_digits(string,self.opts[index]) for index,string in enumerate(self.input_strings)]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
