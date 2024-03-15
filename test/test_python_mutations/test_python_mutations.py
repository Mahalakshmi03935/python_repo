import unittest

from python_repo.src.python_mutations.util import  mutate_string

class TestMutateString(unittest.TestCase):
    def test_cas_1(self):
        # Test mutating string at valid position
        result = mutate_string('mahalakshmi', 4, 'b')
        self.assertEqual(result, 'mahabakshmi')

    def test_case_2(self):
        # Test invalid position
        result = mutate_string('mahalakshmi', 15, 'b')
        self.assertEqual(result, 'mahalakshmi')  # Should return original string

    def test_case_3(self):
        # Test invalid character
        result = mutate_string('mahalakshmi', 3, 'l')
        self.assertEqual(result, 'mahllakshmi')  # Should return original string

if __name__ == '__main__':
    unittest.main()

