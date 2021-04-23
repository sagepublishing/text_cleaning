import unittest
from stem_words.__init__ import stem_words


class TestStemWords(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["learning","Cats and ponies have meeting"]
        self.expected_output_strings = ["learn","cat and poni have meet"]

    def test_stem_words(self):
        ouput_list = [stem_words(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
