import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def floor_ceil_rint(arr):
    floor_arr = np.floor(arr)
    ceil_arr = np.ceil(arr)
    rint_arr = np.rint(arr)
    return floor_arr, ceil_arr, rint_arr


