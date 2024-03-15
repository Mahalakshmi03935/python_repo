import unittest

from python_repo.src.precentage_problem.util import calculate_average


class TestAverageMarks(unittest.TestCase):
    def test_1(self):
        # Test case 1
        student_marks = {'Krishna': [67, 68, 69], 'Arjun': [70, 98, 63], 'Malika': [52, 56, 60]}
        query_name = 'Malika'
        self.assertEqual(calculate_average(student_marks[query_name]), 56.00)

    def test_2(self):
        # Test case 2
        student_marks = {'Harsh': [25, 26.5, 28], 'Anurag': [26, 28, 30]}
        query_name = 'Harsh'
        self.assertEqual(calculate_average(student_marks[query_name]), 26.50)

    def test_3(self):
        # Test case 3
        student_marks = {'Maha': [67, 68, 69], 'Lakshmi': [70, 98, 63],'Ammu':[52,56,60]}
        query_name = 'Ammu'
        self.assertEqual(calculate_average(student_marks[query_name]), 56.00)

if __name__ == '__main__':
    unittest.main()
