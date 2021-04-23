import unittest
from remove_short.__init__ import remove_short

opts={"minsize":6}


class TestRemoveShort(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["He was the more ready to do this because the rights had become much less valuable.","drop his litigation with the monastry and relinguish"]
        self.expected_output_strings = ["because rights become valuable.","litigation monastry relinguish"]

    def test_remove_short(self):
        ouput_list = [remove_short(string,opts) for string in self.input_strings]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
