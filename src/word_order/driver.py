import logging
import sys
import os

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Add the current directory to the Python path
sys.path.append(current_dir)
from word_counter_util import count_word_occurrences

logging.basicConfig(filename='word_counter.log', level=logging.INFO)


def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        words = [f.readline().strip() for _ in range(n)]

    logging.info("Input words: %s", words)
    distinct_words, occurrences = count_word_occurrences(n, words)

    logging.info("Distinct words: %s", distinct_words)
    logging.info("Occurrences: %s", occurrences)

    logging.info("Number of distinct words: %d", len(distinct_words))
    logging.info("Occurrences of distinct words: %s", " ".join(map(str, occurrences)))


if __name__ == "__main__":
    main()
