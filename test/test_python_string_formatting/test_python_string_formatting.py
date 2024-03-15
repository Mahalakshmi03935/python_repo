import unittest
from io import StringIO
import sys
from python_repo.src.python_string_formatting.util import print_formatted

class TestPrintFormatted(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_print_formatted_case_1(self):
        number = 17
        expected_output = ''' 1  1  1  1
 2  2  2 10
 3  3  3 11
 4  4  4 100
 5  5  5 101
 6  6  6 110
 7  7  7 111
 8 10  8 1000
 9 11  9 1001
10 12  A 1010
11 13  B 1011
12 14  C 1100
13 15  D 1101
14 16  E 1110
15 17  F 1111
16 20 10 10000
17 21 11 10001
'''
        print_formatted(number)
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_print_formatted_case_2(self):
        number = 5
        expected_output = '''1  1  1  1
2  2  2 10
3  3  3 11
4  4  4 100
5  5  5 101
'''
        print_formatted(number)
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_print_formatted_case_3(self):
        number = 10
        expected_output = ''' 1  1  1  1
 2  2  2 10
 3  3  3 11
 4  4  4 100
 5  5  5 101
 6  6  6 110
 7  7  7 111
 8 10  8 1000
 9 11  9 1001
10 12  A 1010
'''
        print_formatted(number)
        self.assertEqual(self.output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

