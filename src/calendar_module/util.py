import logging
logging.basicConfig(level=logging.INFO,format="%(message)s")
import calendar
def find_day():
    mm, dd, yyyy = map(int, input().split())
    ind = calendar.weekday(yyyy, mm, dd)
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    result = days[ind]
    logging.info(result)
    return result