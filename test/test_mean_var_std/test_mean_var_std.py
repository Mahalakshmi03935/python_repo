import unittest
import numpy as np
import io
import sys
import logging
from python_repo.src.mean_var_std.util import calculate_mean, calculate_variance, calculate_std_deviation

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.log_capture = io.StringIO()
        self.log_handler = logging.StreamHandler(self.log_capture)
        self.logger.addHandler(self.log_handler)

    def tearDown(self):
        self.logger.removeHandler(self.log_handler)
        self.log_handler.close()

    def test_calculate_mean(self):
        array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        expected_mean = np.array([2.5, 6.5, 10.5])
        calculated_mean = calculate_mean(array, axis=1)
        self.assertTrue(np.allclose(calculated_mean, expected_mean))

        self.log_handler.flush()
        log_output = self.log_capture.getvalue().strip()
        self.assertIn(f'Mean along axis 1: {expected_mean}', log_output)

    def test_calculate_variance(self):
        array = np.array([[1, 2, 3], [4, 5, 6]])
        expected_variance = np.array([1.0, 1.0])
        calculated_variance = calculate_variance(array, axis=1)
        self.assertTrue(np.allclose(calculated_variance, expected_variance))

        self.log_handler.flush()
        log_output = self.log_capture.getvalue().strip()
        self.assertIn(f'Variance along axis 1: {expected_variance}', log_output)

    def test_calculate_std_deviation(self):
        array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        expected_std_deviation = np.array([0.5 * 2**0.5, 0.5 * 2**0.5, 0.5 * 2**0.5, 0.5 * 2**0.5])
        calculated_std_deviation = calculate_std_deviation(array, axis=1)
        self.assertTrue(np.allclose(calculated_std_deviation, expected_std_deviation))

        self.log_handler.flush()
        log_output = self.log_capture.getvalue().strip()
        self.assertIn(f'Standard deviation along axis 1: {expected_std_deviation}', log_output)

if __name__ == '__main__':
    unittest.main()

