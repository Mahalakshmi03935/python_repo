import logging


def calculate_happiness(n, m, arr, a, b):
    happiness = 0
    happy_set = set(a)
    unhappy_set = set(b)

    for num in arr:
        if num in happy_set:
            happiness += 1
        elif num in unhappy_set:
            happiness -= 1

    return happiness


def setup_logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)
