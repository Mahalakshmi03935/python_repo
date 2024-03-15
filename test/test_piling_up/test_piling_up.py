

import unittest
import util
from python_repo.src.piling_up.util.import can_stack_cubes

class TestStackCubes(unittest.TestCase):
    def test_can_stack_cubes(self):
        test_cases = [
            [4, 3, 2, 1, 3, 4],
            [1, 3, 2],
            [5, 4, 3, 2, 1]
        ]
        expected_results = ["Yes", "No", "Yes"]

        results = util.can_stack_cubes(test_cases)

        self.assertEqual(results, expected_results)

if __name__ == "__main__":
    unittest.main()
