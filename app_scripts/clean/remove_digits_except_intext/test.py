import unittest
from remove_digits_except_intext.__init__ import remove_digits_except_intext


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["First 23 by one statements.","Second 5 by two statements."]
        self.expected_output_strings = ["First by one statements.","Second by two statements."]

    def test_remove_digits_except_intext(self):
        ouput_list = [remove_digits_except_intext(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
