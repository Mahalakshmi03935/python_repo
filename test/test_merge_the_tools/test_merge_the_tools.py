import unittest
from io import StringIO
from python_repo.src.merge_the_tools.util import merge_the_tools

class TestMergeTheTools(unittest.TestCase):
    def test_merge_the_tools_case1(self):
        # Test with k=3
        input_string = "AABCAAADA"
        expected_output = "AB\nCA\nAD"
        result = merge_the_tools(input_string, 3)
        self.assertEqual(result, expected_output)

    def test_merge_the_tools_case2(self):
        # Test with k=2
        input_string = "ABCDEF"
        expected_output = "AB\nCD\nEF"
        result = merge_the_tools(input_string, 2)
        self.assertEqual(result, expected_output)

    def test_merge_the_tools_case3(self):
        # Test with k=4
        input_string = "XYXYYXZZZZYX"
        expected_output = "XYX\nYZ\nXZ"
        result = merge_the_tools(input_string, 4)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
