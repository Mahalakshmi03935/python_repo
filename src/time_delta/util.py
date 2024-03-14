from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_time_difference_in_seconds(time1, time2):
    dt_format = '%a %d %b %Y %H:%M:%S %z'
    timestamp1 = datetime.strptime(time1, dt_format)
    timestamp2 = datetime.strptime(time2, dt_format)
    difference = abs(timestamp1 - timestamp2).total_seconds()
    return int(difference)

