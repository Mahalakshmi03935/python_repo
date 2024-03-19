import numpy as np
import logging

logger = logging.getLogger(__name__)

def calculate_mean(array, axis=None):
    mean = np.mean(array, axis=axis)
    logger.info("Mean along axis %s: %s", axis, mean)
    return mean

def calculate_variance(array, axis=None):
    return np.var(array, axis=axis)

def calculate_std_deviation(array, axis=None):
    return np.std(array, axis=axis)

