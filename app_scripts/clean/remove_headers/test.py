import unittest
from remove_headers.__init__ import remove_headers


class TestRemoveHeaders(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["This is first line. This is second line.","Subject,cc,from,to. This is my application."]
        self.expected_output_strings = ["This is second line.","This is my application."]
    
    def test_remove_headers(self):
        ouput_list = [remove_headers(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
