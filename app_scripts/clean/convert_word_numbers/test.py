import unittest
from convert_word_numbers.__init__ import convert_word_digits


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["I was born in twenty ten","thirty twenty one"]
        self.expected_output_strings = ["I was born in 2010", "3021"]

    def test_convert_word_numbers(self):
        ouput_list = [convert_word_digits(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
