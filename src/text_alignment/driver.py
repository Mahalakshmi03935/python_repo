import logging
from util import generate_hackerrank_logo

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    thickness = int(input("Enter the thickness for the logo: "))
    logo = generate_hackerrank_logo(thickness)
    logger.debug("\n%s", logo)

