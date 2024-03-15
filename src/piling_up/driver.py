# driver.py

import logging
import util

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    test_cases = [
        [4, 3, 2, 1, 3, 4],
        [1, 3, 2]
    ]

    results = util.can_stack_cubes(test_cases)

    for i, result in enumerate(results):
        logger.info(f"Test case {i+1}: {result}")

if __name__ == "__main__":
    main()
