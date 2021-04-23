import unittest
from replace_urls.__init__ import replace_urls


class TestReplaceUrls(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["Python website: https://www.python.org/","Google: https://www.python.org/."]
        self.expected_output_strings = ["Python website: url","Google: url"]
        self.opts = [
            {
                "token":'url'
            },
        ]

    def test_replace_urls(self):
        ouput_list = [replace_urls(string,self.opts[0]) for index,string in enumerate(self.input_strings)]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
