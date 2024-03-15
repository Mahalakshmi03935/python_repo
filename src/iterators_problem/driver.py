import logging
from util import calculate_probability

def main():
    logging.basicConfig(filename='probability.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    logger = logging.getLogger()

    try:
        n = int(input("Enter the length of the list: "))
        letters = input("Enter the lowercase English letters separated by space: ").split()
        k = int(input("Enter the number of indices to be selected: "))

        probability = calculate_probability(n, letters, k)
        logger.info(f"Probability: {probability}")
        print(f"Probability: {probability}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


