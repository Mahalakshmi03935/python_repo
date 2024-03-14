import logging
import util

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    matrix = util.parse_input()
    determinant = util.find_determinant(matrix)
    if determinant is not None:
        logger.debug(f"Determinant of the matrix: {determinant}")
