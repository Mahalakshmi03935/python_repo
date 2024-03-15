import unittest
import logging
from python_repo.src.iterators_problem.util import calculate_probability

class TestProbability(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(filename='test_probability.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger()

    def test_probability_1(self):
        n = 4
        letters = ['a', 'a', 'c', 'd']
        k = 2
        expected_probability = 0.8333
        probability = calculate_probability(n, letters, k)
        self.assertAlmostEqual(probability, expected_probability, places=4)
        self.logger.info(f"Test 1 - Probability: {probability}, Expected: {expected_probability}")

    def test_probability_2(self):
        n = 5
        letters = ['a', 'b', 'c', 'd', 'e']
        k = 3
        expected_probability = 0.8571
        probability = calculate_probability(n, letters, k)
        self.assertAlmostEqual(probability, expected_probability, places=4)
        self.logger.info(f"Test 2 - Probability: {probability}, Expected: {expected_probability}")

    def test_probability_3(self):
        n = 3
        letters = ['a', 'a', 'a']
        k = 1
        expected_probability = 0.6667
        probability = calculate_probability(n, letters, k)
        self.assertAlmostEqual(probability, expected_probability, places=4)
        self.logger.info(f"Test 3 - Probability: {probability}, Expected: {expected_probability}")

if __name__ == "__main__":
    unittest.main()
