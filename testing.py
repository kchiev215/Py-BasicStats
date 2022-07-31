import unittest.mock
import math
import csv
import Functions


class TestingFunctions(unittest.TestCase):
    def test_zcount(self):
        expected = 5
        actual = Functions.zcount([1, 2, 3, 4, 5])
        self.assertEqual(actual, expected)

    def test_zcount1(self):
        expected = 6
        actual = Functions.zcount([1, 2, 3, 4, 5, 6])
        self.assertEqual(actual, expected)

    def test_zcount3(self):
        expected = 1
        actual = Functions.zcount([1])
        self.assertEqual(actual, expected)

    def test_zmean(self):
        expected = 2
        actual = Functions.zmean([1, 2, 3])
        self.assertEqual(actual, expected)

    def test_zmean2(self):
        expected = 1
        actual = Functions.zmean([1, 1, 1, 1])
        self.assertEqual(actual, expected)

    def test_zmean3(self):
        expected = round(4.71429, 2)
        actual = Functions.zmean([1, 2, 4, 5, 6, 7, 8])
        self.assertEqual(actual, expected)

    def test_median(self):
        expected = 5
        actual = Functions.zmedian([1, 2, 4, 5, 6, 7, 8])
        self.assertEqual(actual, expected)

    def test_median1(self):
        expected = 5
        actual = Functions.zmedian([4, 5, 4, 5, 6, 7, 8])
        self.assertEqual(actual, expected)

    def test_median2(self):
        expected = 6
        actual = Functions.zmedian([4, 5, 32, 5, 7, 8])
        self.assertEqual(actual, expected)


