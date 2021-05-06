import unittest
from remove_punctuation_except.__init__ import remove_punctuation_except

opts={"wordlist":','}


class TestRemovePunctuationExcept(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["Addressing a person!: 'Yes, Sir.'","AAA? BBB. CCC!"]
        self.expected_output_strings = ["Addressing a person Yes, Sir","AAA BBB CCC"]

    def test_remove_punctuation_except(self):
        ouput_list = [remove_punctuation_except(string,opts) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
