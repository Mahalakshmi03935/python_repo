import util
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_time_difference(testcases):
    results = []
    for time1, time2 in testcases:
        difference = util.get_time_difference_in_seconds(time1, time2)
        if difference is not None:
            results.append(difference)
    return results

if __name__ == "__main__":
    testcases = [
        ("Sun 10 MAY 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"),
        ("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"),
        # Add more test cases if needed
    ]


    results = calculate_time_difference(testcases)
    if results:
        for result in results:
            logger.info("Time difference in seconds: {}".format(result))

