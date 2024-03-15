import unittest
from unittest.mock import patch
from util import calculate_happiness, setup_logger


class TestCalculateHappiness(unittest.TestCase):

    @patch('util.logging.getLogger')
    def test_happiness_positive(self, mock_logger):
        mock_logger.return_value = logger = MagicMock()
        n = 5
        m = 3
        arr = [1, 2, 3, 4, 5]
        a = [1, 3, 5]
        b = [2, 4]

        happiness = calculate_happiness(n, m, arr, a, b)

        self.assertEqual(happiness, 3)
        logger.info.assert_called_with("Total happiness: %d", 3)

    @patch('util.logging.getLogger')
    def test_happiness_negative(self, mock_logger):
        mock_logger.return_value = logger = MagicMock()
        n = 5
        m = 3
        arr = [1, 2, 3, 4, 5]
        a = [2, 4]
        b = [1, 3, 5]

        happiness = calculate_happiness(n, m, arr, a, b)

        self.assertEqual(happiness, -3)
        logger.info.assert_called_with("Total happiness: %d", -3)

    @patch('util.logging.getLogger')
    def test_happiness_mixed(self, mock_logger):
        mock_logger.return_value = logger = MagicMock()
        n = 5
        m = 3
        arr = [1, 2, 3, 4, 5]
        a = [1, 4]
        b = [2, 5]

        happiness = calculate_happiness(n, m, arr, a, b)

        self.assertEqual(happiness, 0)
        logger.info.assert_called_with("Total happiness: %d", 0)


if __name__ == '__main__':
    unittest.main()
