import logging
from util import find_day
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

input_date = input("Enter the date in format (MM DD YYYY): ")
parts = input_date.split()
if len(parts) == 3:
    month, day, year = map(int, parts)
    day_of_week = find_day(month, day, year)
    logger.info(f"The day is: {day_of_week}")
else:
    logger.error("Invalid input. Please enter date in format (MM DD YYYY)")
