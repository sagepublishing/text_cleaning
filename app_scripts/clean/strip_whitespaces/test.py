import unittest
from strip_whitespaces.__init__ import strip_whitespaces


class TestStripWhiteSpaces(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["This is   a Text \n and so on \t     Text text.","This is  a string   with    spaces, tabs present"]
        self.expected_output_strings = ["This is a Text and so on Text text.","This is a string with spaces, tabs present"]

    def test_strip_whitespaces(self):
        ouput_list = [strip_whitespaces(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
