
import logging
from util import print_formatted

# Configure the logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Test cases
test_cases = [17, 5, 10]

# Get the root logger
logger = logging.getLogger()

# Driver code
if __name__ == "__main__":
    for number in test_cases:
        logger.info(f"Printing formatted values for {number}:")
        formatted_value = print_formatted(number)
        logger.info(formatted_value)


