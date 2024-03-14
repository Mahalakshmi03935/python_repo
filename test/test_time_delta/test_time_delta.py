import unittest
from python_repo.src.time_delta.util import get_time_difference_in_seconds



class TestTimeDifference(unittest.TestCase):

    def test_time_difference(self):
        # Test case 1
        time1 = "Sun 10 May 2015 13:54:36 -0700"
        time2 = "Sun 10 May 2015 13:54:36 -0000"
        expected_result = 25200
        result = get_time_difference_in_seconds(time1, time2)
        self.assertEqual(result, expected_result)

    def test_time_difference1(self):
        # Test case 2
        time1 = "Sat 02 May 2015 19:54:36 +0530"
        time2 = "Fri 01 May 2015 13:54:36 -0000"
        expected_result = 88200
        result = get_time_difference_in_seconds(time1, time2)
        self.assertEqual(result, expected_result)





if __name__ == '__main__':
    unittest.main()

