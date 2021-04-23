import unittest
from remove_footers.__init__ import remove_footers


class TestRemoveFooters(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["'I was born in 2000. I am years old.''second line'"]
        self.expected_output_strings = [""]
        self.opts = [
            {
                "footer_lines":1
            }
        ]

    def test_remove_footers(self):
        ouput_list = [remove_footers(string,self.opts[index]) for index,string in enumerate(self.input_strings)]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
