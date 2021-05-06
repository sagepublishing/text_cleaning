import unittest
from remove_custom_stopwords.__init__ import remove_custom_stopwords


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["We did it ourselves.","The Mona Lisa doesn't have eyebrows."]
        self.expected_output_strings = ["We it ourselves.", "The Lisa doesn't have eyebrows."]
        self.opts = [
            {
                "wordlist": "did"
            },
            {
                "wordlist": "Mona"
            }
        ]

    def test_remove_custome_stopwords(self):
        ouput_list = [remove_custom_stopwords(string,self.opts[index]) for index,string in enumerate(self.input_strings)]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
