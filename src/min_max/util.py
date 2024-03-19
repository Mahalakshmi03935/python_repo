import numpy as np, logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)
def min_max_operation(array):
    logger.info("Input Array:\n%s", array)
    min_value = np.min(array)
    logger.info("Min Value along axis None: %d", min_value)
    max_min_value = np.max(min_value)
    logger.debug("Max of Min Values along axis None: %d", max_min_value)
    return max_min_value


