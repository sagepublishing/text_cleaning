import unittest
from stem_words_lancaster.__init__ import stem_words_lancaster


class TestStemWordsLancaster(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["pythoners are very intelligent and work very pythonly and now they are pythoning their way to success.","the boy's cars are different colors"]
        self.expected_output_strings = ["python ar very intellig and work very python and now they ar python their way to success . ","the boy 's car ar diff col "]

    def test_stem_words_lancaster(self):
        ouput_list = [stem_words_lancaster(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
