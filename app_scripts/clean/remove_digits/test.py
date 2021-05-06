import unittest
from remove_digits.__init__ import remove_digits


class TestRemoveDigits(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["I was born in 2000.","Your age must be below 18."]
        self.expected_output_strings = ["I was born in .","Your age must be below ."]

    def test_remove_digits(self):
        ouput_list = [remove_digits(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
