import unittest
from fix_encoding.__init__ import ftfy_fix_encoding


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["âœ” No problems","The Mona Lisa doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have eyebrows."]
        self.expected_output_strings = ["✔ No problems", "The Mona Lisa doesn’t have eyebrows."]

    def test_fix_encoding(self):
        ouput_list = [ftfy_fix_encoding(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
