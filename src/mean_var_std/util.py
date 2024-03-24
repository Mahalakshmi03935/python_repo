import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_mean_var_std():
    X, Y = map(int, input().split())
    arr = []
    for _ in range(X):
        arr.append(list(map(int, input().split())))

    mean = np.mean(arr, axis=1)
    var = np.var(arr, axis=1)
    std = np.std(arr, axis=1)

    logging.debug(mean)
    logging.debug(var)
    logging.debug(std)

    return mean, var, std

