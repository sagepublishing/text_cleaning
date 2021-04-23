import unittest
from remove_punctuation.__init__ import remove_punctuation


class TestRemovePunctuation(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["AAA? BBB. CCC! DDD.EEE","AAA? BBB. CCC!"]
        self.expected_output_strings = ["AAA BBB CCC DDDEEE","AAA BBB CCC"]

    def test_remove_punctuation(self):
        ouput_list = [remove_punctuation(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
