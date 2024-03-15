import logging
from util import filter_valid_emails

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    num_emails = int(input().strip())
    emails = [input().strip() for _ in range(num_emails)]

    valid_emails = filter_valid_emails(emails)

    logger.info(valid_emails)


if __name__ == "__main__":
    main()
