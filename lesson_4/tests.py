import unittest
from module import multiply_numbers, join_strings, age_in_years
from solution import multiply_numbers, join_strings, age_in_years #Uncomment this line for solution

class TestStringMethods(unittest.TestCase):

    def test_multiply_numbers(self):
        print
        print "Testing multiply_numbers"
        print multiply_numbers(3,4)
        self.assertEqual(multiply_numbers(3,4),12)

    def test_join_strings(self):
        print
        print "Testing join_strings"
        print join_strings("hello ","how are you?")
        self.assertEqual(join_strings("hello ","how are you?"),"hello how are you?")

    def test_age_in_years(self):
        print
        print "Testing age_in_years"
        print age_in_years(13,4,1989)
        self.assertEqual(age_in_years(13,4,1989), 29)

if __name__ == '__main__':
    unittest.main()
