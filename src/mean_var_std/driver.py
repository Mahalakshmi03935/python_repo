import sys
import utils
import numpy as np
from util import calculate_mean,calculate_variance,calculate_std_deviation
import logging

# Configure loggerr
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Reading input
    first_line = sys.stdin.readline().strip()
    n, m = map(int, first_line.split())
    array = []
    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().strip().split())))
    array = np.array(array)

    # Calculating mean, variance, and std deviation
    mean = utils.calculate_mean(array, axis=1)
    variance = utils.calculate_variance(array, axis=1)
    std_deviation = utils.calculate_std_deviation(array, axis=1)

    # Logging results
    logger.info("Mean along axis 1: %s", mean)
    logger.info("Variance along axis 1: %s", variance)
    logger.info("Standard deviation along axis 1: %s", std_deviation)

if __name__ == "__main__":
    main()
