import numpy
import logging
from util import min_max_operation
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def main():
    result = min_max_operation[(4,5,8,9,10),(4,7,2,9,10)]
    with open("output.txt", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()

