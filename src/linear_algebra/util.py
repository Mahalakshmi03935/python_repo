import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)

def find_determinant(matrix):
    det = np.linalg.det(matrix)
    logger.info(f"Determinant of the matrix: {det:.2f}")
    return round(det, 2)

def parse_input():
    n = int(input("Enter the dimension of the square matrix: "))
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix
