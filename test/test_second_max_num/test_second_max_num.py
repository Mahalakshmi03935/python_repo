import unittest
from unittest.mock import patch
from python_repo.src.second_max_num.util import find_runner_up_score

class TestFindRunnerUpScore(unittest.TestCase):
    def test_empty_list(self):
        scores = []
        self.assertIsNone(find_runner_up_score(len(scores), scores))

    def test_single_score(self):
        scores = [10]
        self.assertIsNone(find_runner_up_score(len(scores), scores))

    @patch('builtins.input', side_effect=['5', '2 3 6 6 5'])
    def test_normal_case(self, mock_input):
        n = int(input("enter the number:"))
        scores = list(map(int,input("enter the input:").split()))
        self.assertEqual(find_runner_up_score(n, scores), 5)

if __name__ == '__main__':
    unittest.main()
