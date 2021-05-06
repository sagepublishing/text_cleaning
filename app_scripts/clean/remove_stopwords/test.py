import unittest
from remove_stopwords.__init__ import remove_default_stopwords


class TestRemoveDefaultStopwords(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["Nick likes to play football, however he is not too fond of tennis.","He determined to drop his litigation with the monastry, and relinguish his claims to the wood-cuting and fishery rihgts at once."]
        self.expected_output_strings = ["Nick likes play football, fond tennis.","He determined drop litigation monastry, relinguish claims wood-cuting fishery rihgts once."]

    def test_remove_default_stopwords(self):
        ouput_list = [remove_default_stopwords(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
