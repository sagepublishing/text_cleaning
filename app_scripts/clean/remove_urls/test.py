import unittest
from remove_urls.__init__ import remove_urls_from_string


class TestRemoveUrlsFromString(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["This is a tweet with a url: http://t.co/0DlGChTBIx","Amazing save #FACup #zeebox https://stackoverflow.com/tiUya56M Ok"]
        self.expected_output_strings = ["This is a tweet with a url: ","Amazing save #FACup #zeebox  Ok"]

    def test_remove_urls_from_string(self):
        ouput_list = [remove_urls_from_string(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)
        
if __name__ == '__main__':
    unittest.main()
