import numpy as np
import logging
from util import floor_ceil_rint

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    input_str = input("Enter the space-separated elements of the array: ")
    arr = np.array(list(map(float, input_str.split())))

    floor_arr, ceil_arr, rint_arr = floor_ceil_rint(arr)

    logger.info(f"Floor of array: {floor_arr}")
    logger.info(f"Ceil of array: {ceil_arr}")
    logger.info(f"Rint of array: {rint_arr}")

