import unittest
from remove_pattern.__init__ import remove_pattern


class TestRemovePatterns(unittest.TestCase):

    def setUp(self):
        self.input_strings = ["John is a good man.","We went to the movies, and then we went out to lunch."]
        self.expected_output_strings = ["John  good man.","We went to the movies, and then  out to lunch."]
        self.opts = [
            {
               "string": 'is a' 
            },
            {
                "string": 'we went'
            }
        ]
    def test_remove_patterns(self):
        ouput_list = [remove_pattern(string,self.opts[index]) for index,string in enumerate(self.input_strings)]
        self.assertListEqual(self.expected_output_strings, ouput_list)

if __name__ == '__main__':
    unittest.main()
