import unittest
from to_lowercase.__init__ import to_lowercase


class TestToLowerCase(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["UNRELIABLE CONNECTION SERVICE","PREFERABLE FOR TELEPHONE"]
        self.expected_output_strings = ["unreliable connection service","preferable for telephone"]

    def test_to_lowercase(self):
        ouput_list = [to_lowercase(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
