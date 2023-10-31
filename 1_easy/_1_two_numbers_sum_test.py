import unittest
import time
from random import randint

from _1_two_numbers_sum import two_numbers_sum_a
from _1_two_numbers_sum import two_numbers_sum_b
from _1_two_numbers_sum import two_numbers_sum_c


class TwoNumbersSumA_TestCase(unittest.TestCase):
    def setUp(self):
        self.current_setup()

    def current_setup(self):
        self.tested_method = two_numbers_sum_a

    def test_full_list_negative_positive_true(self):
        self.assertEqual([11, -1], self.tested_method([3, 5, -4, 8, 11, 1, -1, 6], 10))

    def test_full_list_negative_positive_false(self):
        self.assertEqual(None, self.tested_method([3, 5, -4, 8, 11, 1, -1, 6], 50))

    def test_full_list_all_positive_true(self):
        self.assertEqual([8, 11], self.tested_method([3, 5, 4, 8, 11, 1, 1, 6], 19))

    def test_full_list_all_positive_false(self):
        self.assertEqual(None, self.tested_method([3, 5, 4, 8, 11, 1, 1, 6], 50))

    def test_full_list_all_negative_true(self):
        self.assertEqual([-8, -11], self.tested_method([-3, -5, -4, -8, -11, -1, -1, -6], -19))

    def test_full_list_all_negative_false(self):
        self.assertEqual(None, self.tested_method([-3, -5, -4, -8, -11, -1, -1, -6], 50))

    def test_one_pair_true(self):
        self.assertEqual([-3, 3], self.tested_method([-3, 3], 0))

    def test_one_pair_false(self):
        self.assertEqual(None, self.tested_method([-3, -5], 0))

    def test_empty_false(self):
        self.assertEqual(None, self.tested_method([], 0))

    def test_one_item_false(self):
        self.assertEqual(None, self.tested_method([0], 0))


class TwoNumbersSumB_TestCase(TwoNumbersSumA_TestCase):
    def current_setup(self):
        self.tested_method = two_numbers_sum_b


class TwoNumbersSumC_TestCase(TwoNumbersSumA_TestCase):
    def current_setup(self):
        self.tested_method = two_numbers_sum_c


def time_it(method, *args, **kwargs):
    start_time = time.time()
    method(*args, **kwargs)
    end_time = time.time()
    print("execution of {}: {}[s]".format(method.__name__, end_time-start_time))


class TimeMeasurement_TestCase(unittest.TestCase):
    def test_measure_time(self):
        array = [randint(-20, 20) for _ in range((10**4) * 1)]

        time_it(two_numbers_sum_a, array, 50)
        time_it(two_numbers_sum_b, array, 50)
        time_it(two_numbers_sum_c, array, 50)


if __name__ == '__main__':
    unittest.main()
