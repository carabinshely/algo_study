import unittest

from sorting_code import quick_sort


class MyTestQuickSort(unittest.TestCase):
    def setUp(self):
        self.sort_method = self.get_sort_method()

    def get_sort_method(self):
        return quick_sort

    def test_empty(self):
        self.assertEqual([], self.sort_method([]))

    def test_one_element(self):
        self.assertEqual([1], self.sort_method([1]))

    def test_two_equal(self):
        self.assertEqual([1, 1], self.sort_method([1, 1]))

    def test_two_notequal_sorted(self):
        self.assertEqual([1, 2], self.sort_method([1, 2]))

    def test_two_not_equal_not_sorted(self):
        self.assertEqual([1, 2], self.sort_method([2, 1]))

    def test_tree_equal(self):
        self.assertEqual([0, 0, 0], self.sort_method([0, 0, 0]))

    def test_three_notequal_sorted(self):
        self.assertEqual([1, 2, 3], self.sort_method([1, 2, 3]))

    def test_three_not_equal_not_sorted(self):
        self.assertEqual([1, 2, 3], self.sort_method([2, 1, 3]))

    def test_many_with_negative(self):
        self.assertEqual([-1, 0, 1, 2, 3], self.sort_method([0, 2, 1, 3, -1]))

    def test_many_with_doubled(self):
        self.assertEqual([-5, -5, 1, 5, 5], self.sort_method([-5, 5, 1, 5, -5]))

    def test_many_sorted(self):
        self.assertEqual([-2, -1, 0, 1, 2], self.sort_method([-2, -1, 0, 1, 2]))


if __name__ == '__main__':
    unittest.main()
