import logging
import calendar

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def find_day(month, day, year):
    day_of_week = calendar.day_name[calendar.weekday(year, month, day)].upper()
    logger.info(f"The day on {month}/{day}/{year} was {day_of_week}")
    return day_of_week

