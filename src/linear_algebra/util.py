import numpy
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')

def linear_algebra():
    a=int(input())
    arr = []
    for _ in range(a):
        arr.append(list(map(float, input().split())))
    logging.info(round(numpy.linalg.determinant(arr), 2))
    return (round(numpy.linalg.determinant(arr), 2))
