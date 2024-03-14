import unittest
from unittest.mock import patch
import numpy as np
from python_repo.src.linear_algebra.util import parse_input,find_determinant


class TestUtil(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '1 2 3', '4 5 6', '7 8 9'])
    def test_find_determinant(self, mock_input):
        matrix = parse_input()
        determinant = find_determinant(matrix)
        self.assertEqual(determinant, 0.0)

    @patch('builtins.input', side_effect=['2', '1 2', '3 4'])
    def test_find_determinant_non_zero(self, mock_input):
        matrix = parse_input()
        determinant = find_determinant(matrix)
        self.assertEqual(determinant, -2.0)

    @patch('builtins.input', side_effect=['2', '1 a', '3 4'])
    def test_parse_input_invalid(self, mock_input):
        with self.assertRaises(ValueError):
            parse_input()



if __name__ == '__main__':
    unittest.main()
