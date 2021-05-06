import unittest
from replace_word_breaks.__init__ import replace_word_breaks


class TestReplaceWordBreaks(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["you are right-  <3!","A bunch of - 'new' references, including  - [moana](<URL>)."]
        self.expected_output_strings = ["you are right <3!","A bunch of 'new' references, including  [moana](<URL>)."]
        self.opts = [
            {
                "token":'url'
            },
        ]

    def test_replace_word_breaks(self):
        ouput_list = [replace_word_breaks(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
