import unittest
from unittest.mock import patch
from io import StringIO
from python_repo.src.min_max.util.import min_max_operation

class TestMinMaxOperation(unittest.TestCase):

    def test_min_max_operation(self):
        input_array = [(4,5,8,9,10),(4,7,2,9,10)]
        expected_result = 9  # Expected max of min values

        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = min_max_operation(input_array)

            self.assertEqual(result, expected_result)

            # Verify logged messages
            logged_output = fake_out.getvalue().strip().split('\n')
            self.assertEqual(len(logged_output),
            self.assertIn("Input Array:", logged_output[0])
            self.assertIn("Min Value along axis None:", logged_output[1])
            self.assertIn("Max of Min Values along axis None:", logged_output[2])

    def test_min_max_operation_empty_array(self):
        input_array = []
        expected_result = None

        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = min_max_operation(input_array)

            self.assertEqual(result, expected_result)

            # Verify logged messages
            logged_output = fake_out.getvalue().strip().split('\n')
            self.assertEqual(len(logged_output), 1)
            self.assertIn("Input Array:", logged_output[0])

    def test_min_max_operation_single_element_array(self):
        input_array = [(5,)]  # Single-element array
        expected_result = 5  # Expected max of min values for a single element

        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = min_max_operation(input_array)

            self.assertEqual(result, expected_result)

            # Verify logged messages
            logged_output = fake_out.getvalue().strip().split('\n')
            self.assertEqual(len(logged_output), 3)  # Ensure correct number of log messages
            self.assertIn("Input Array:", logged_output[0])
            self.assertIn("Min Value along axis None:", logged_output[1])
            self.assertIn("Max of Min Values along axis None:", logged_output[2])

if __name__ == '__main__':
    unittest.main()

