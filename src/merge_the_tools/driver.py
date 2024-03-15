import logging
from util import merge_the_tools

def setup_logger():
    logging.basicConfig(filename='merge_tools.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')


def main():
    setup_logger()
    s = input().strip()
    k = int(input().strip())
    merge_the_tools("mahalakshmi",5)

if __name__ == "__main__":
    main()

