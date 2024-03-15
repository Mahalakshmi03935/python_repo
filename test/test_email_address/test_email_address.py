import unittest
import logging
from util import is_valid_email, filter_valid_emails

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestUtil(unittest.TestCase):
    def test_is_valid_email(self):
        valid_emails = ["test@example.com", "user_123@example.com", "user-123@example.com", "user123@example.com",
                        "user123@example.co.uk", "user.123@example.co"]
        invalid_emails = ["testexample.com", "test@examplecom", "test@.com", "@example.com", "test@com", "test@.com.",
                          "test@.123", "test@exam ple.com"]

        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))
                logger.info(f"{email} is a valid email.")

        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
                logger.info(f"{email} is an invalid email.")

    def test_filter_valid_emails(self):
        emails = ["test@example.com", "user_123@example.com", "user-123@example.com", "user123@example.com",
                  "user123@example.co.uk", "user.123@example.co", "invalid-email", "invalid_email@", "@invalid.com"]
        expected_result = ["test@example.com", "user-123@example.com", "user_123@example.com", "user123@example.com",
                           "user.123@example.co"]
        filtered_emails = filter_valid_emails(emails)
        self.assertEqual(filtered_emails, expected_result)
        logger.info(f"Filtered valid emails: {filtered_emails}")


if __name__ == '__main__':
    unittest.main()
