import unittest
from lemmatize_sentences_spacy.__init__ import lemmatize_sentence_spacy


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["loving","Python is the greatest language in the world"]
        self.expected_output_strings = ["love", "Python be the great language in the world"]

    def test_lemmatize_sentences_spacy(self):
        ouput_list = [lemmatize_sentence_spacy(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
