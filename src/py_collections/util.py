import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from collections import namedtuple
def calculate_average():
    n = int(input())
    columns = input().split()
    Student = namedtuple('Student', columns)
    marks_index = columns.index('MARKS')
    total_marks = sum(int(input().split()[marks_index]) for _ in range(n))
    return total_marks / n
logging.debug('{:.2f}'.format(calculate_average()))


