import unittest
from remove_stopwords_except.__init__ import remove_stopwords_except


class TestRemoveStopwordsExcept(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["We did it ourselves.","I do by myself."]
        self.expected_output_strings = ["We did ourselves.","I by myself."]
        self.opts = [
            {
                "wordlist":"did"
            },

            {
                "wordlist":"by"
            }
        ]

    def test_remove_stopwords_except(self):
        ouput_list = [remove_stopwords_except(string,self.opts[index]) for index,string in enumerate(self.input_strings)]
        self.assertListEqual(self.expected_output_strings, ouput_list)


if __name__ == '__main__':
    unittest.main()
