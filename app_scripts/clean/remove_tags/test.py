import unittest
from remove_tags.__init__ import remove_tags


class TestRemoveTags(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["<h2>Image Maps</h2>","<h1> Server side Example</h1>"]
        self.expected_output_strings = ["Image Maps"," Server side Example"]

    def test_remove_tags(self):
        ouput_list = [remove_tags(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
