import unittest
from unittest.mock import patch
from python_repo.src.calendar_module.util import find_day

class TestFindDay(unittest.TestCase):
    def test_regular_date(self):
        # Test with a regular date (June 1, 2022)
        expected_day = "WEDNESDAY"
        actual_day = find_day(6, 1, 2022)
        self.assertEqual(actual_day, expected_day)

    def test_2(self):
        # Test with a regular date(March 3, 2002)
        expected_day = "SUNDAY"
        actual_day = find_day(3, 3, 2002)
        self.assertEqual(actual_day, expected_day)

    def test_invalid_date(self):
        # Test with an invalid date (February 30, 2022)
        with self.assertRaises(ValueError):
            find_day(2, 30, 2022)

if __name__ == '__main__':
    unittest.main()
