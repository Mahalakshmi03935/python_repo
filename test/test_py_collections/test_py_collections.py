import unittest
from util import calculate_average_marks

class TestAverageMarks(unittest.TestCase):
    def test_average_marks(self):
        test_case_1 = (5, "ID", "MARKS", "NAME", "CLASS")
        test_case_2 = (5, "MARKS", "CLASS", "NAME", "ID")
        test_case_3 = (5, "CLASS", "MARKS", "ID", "NAME")

        self.assertAlmostEqual(calculate_average_marks(*test_case_1), 78.00)
        self.assertAlmostEqual(calculate_average_marks(*test_case_2), 81.00)
        self.assertAlmostEqual(calculate_average_marks(*test_case_3), 77.00)

if __name__ == '__main__':
    unittest.main()

