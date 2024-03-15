import unittest
from io import StringIO
import sys
import os

# Add the directory containing util.py and driver.py to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)

# Import the function to be tested
from util import count_word_occurrences


class TestWordCounter(unittest.TestCase):
    def test_count_word_occurrences(self):
        # Test case 1: No words provided
        words = []
        distinct_words, occurrences = count_word_occurrences(0, words)
        self.assertEqual(distinct_words, [])
        self.assertEqual(occurrences, [])

        # Test case 2: Single word provided multiple times
        words = ['apple', 'apple', 'apple']
        distinct_words, occurrences = count_word_occurrences(3, words)
        self.assertEqual(distinct_words, ['apple'])
        self.assertEqual(occurrences, [3])

        # Test case 3: Multiple unique words provided
        words = ['apple', 'banana', 'apple', 'orange', 'banana']
        distinct_words, occurrences = count_word_occurrences(5, words)
        self.assertEqual(distinct_words, ['apple', 'banana', 'orange'])
        self.assertEqual(occurrences, [2, 2, 1])


class TestDriver(unittest.TestCase):
    def test_main(self):
        # Redirect stdout to StringIO to capture log output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run main function
        from driver import main
        main()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check if logs contain expected messages
        log_contents = captured_output.getvalue()
        self.assertIn("Input words", log_contents)
        self.assertIn("Distinct words", log_contents)
        self.assertIn("Occurrences", log_contents)
        self.assertIn("Number of distinct words", log_contents)
        self.assertIn("Occurrences of distinct words", log_contents)


if __name__ == '__main__':
    unittest.main()
