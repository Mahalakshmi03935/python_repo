import unittest
from python_repo.src.text_alignment.util import generate_hackerrank_logo

class TestGenerateHackerRankLogo(unittest.TestCase):

    def test_generate_logo_odd_thickness(self):
        # Test with odd thickness
        expected_logo = (
            "----H----\n"
            "--HHHHHH--\n"
            "HHHHHHHHHHH\n"
            "HHHHHHHHHHH\n"
            "HHHHHHHHHHH\n"
            "HHHHHHHHHHH\n"
            "--HHHHHH--\n"
            "----H----\n"
        )
        logo = generate_hackerrank_logo(5)
        self.maxDiff = None
        self.assertMultiLineEqual(logo, expected_logo)

if __name__ == '__main__':
    unittest.main()
