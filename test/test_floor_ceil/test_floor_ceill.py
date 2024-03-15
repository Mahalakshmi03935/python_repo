import unittest
import numpy as np
from python_repo.src.floor_ceil.util import floor_ceil_rint

class TestFloorCeilRint(unittest.TestCase):
    def test_floor_ceil_rint(self):#Test case 1:All float values
        arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
        floor_arr, ceil_arr, rint_arr = floor_ceil_rint(arr)
        self.assertTrue(np.array_equal(floor_arr, np.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])))
        self.assertTrue(np.array_equal(ceil_arr, np.array([ 2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])))
        self.assertTrue(np.array_equal(rint_arr, np.array([ 1.,  2.,  3.,  4.,  6.,  7.,  8.,  9., 10.])))

    def test_floor_ceil_rint1(self):
        # Test case 2: All negative values
        arr2 = np.array([-1.1, -2.2, -3.3, -4.4, -5.5])
        floor_arr2, ceil_arr2, rint_arr2 = floor_ceil_rint(arr2)
        self.assertTrue(np.array_equal(floor_arr2, np.array([-2., -3., -4., -5., -6.])))
        self.assertTrue(np.array_equal(ceil_arr2, np.array([-1., -2., -3., -4., -5.])))
        self.assertTrue(np.array_equal(rint_arr2, np.array([-1., -2., -3., -4., -6.])))

    def test_floor_ceil_rint2(self):
        arr3 = np.array([1, 2, 3, 4, 5])
        floor_arr1, ceil_arr1, rint_arr1 = floor_ceil_rint(arr3)
        self.assertTrue(np.array_equal(floor_arr1, np.array([1., 2., 3., 4., 5.])))
        self.assertTrue(np.array_equal(ceil_arr1, np.array([1., 2., 3., 4., 5.])))
        self.assertTrue(np.array_equal(rint_arr1, np.array([1., 2., 3., 4., 5.])))


if __name__ == '__main__':
    unittest.main()

