import unittest
from to_sentences.__init__ import to_sentences


class TestToSentence(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance."]
        self.expected_output_strings = ['Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.'"Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance."]

    def test_to_sentences(self):
        ouput_list = [to_sentences(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)
        
if __name__ == '__main__':
    unittest.main()
    