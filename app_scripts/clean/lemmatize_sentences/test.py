import unittest
from lemmatize_sentences.__init__ import lemmatize_sentence


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["They bought them some apples","I am loving it"]
        self.expected_output_strings = ["They buy them some apple", "I be love it"]

    def test_lemmatize_sentences(self):
        ouput_list = [lemmatize_sentence(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
