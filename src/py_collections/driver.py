from util import calculate_average_marks
import logging

# Setup logging
logging.basicConfig(filename='average_marks.log', level=logging.INFO)

def main():
    num_students = int(input())
    columns = input().split()
    logging.info("Columns: %s", columns)
    average_marks = calculate_average_marks(num_students, *columns)
    logging.info("Average Marks: %.2f", average_marks)

if __name__ == "__main__":
    main()
