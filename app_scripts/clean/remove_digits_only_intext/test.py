import unittest
from remove_digits_only_intext.__init__ import remove_digits_only_intext


class TestRemoveDigitsOnlyIntext(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["First wicket in one hour 20minutes.","The train will arrive in three hour 40minutes."]
        self.expected_output_strings = ["First wicket in one hour minutes.","The train will arrive in three hour minutes."]

    def test_remove_digits_only_intext(self):
        ouput_list = [remove_digits_only_intext(string) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
