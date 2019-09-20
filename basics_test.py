import unittest
import random
import math
import get_column_stats as gcs


class TestGetColumnStats(unittest.TestCase):

    def test_list_mean_const_small(self):
        r = gcs.list_mean([1])
        self.assertEqual(r, 1)

    def test_list_mean_rand_small(self):
        L = []
        direct_sum = 0
        for i in range(5):
            rand_int = random.randint(1, 10)
            direct_sum += rand_int
            L.append(rand_int)
        direct_mean = direct_sum / 5

        r = gcs.list_mean(L)
        self.assertEqual(r, direct_mean)

    def test_list_mean_rand_large(self):
        L = []
        direct_sum = 0
        for i in range(100):
            rand_int = random.randint(1, 10)
            direct_sum += rand_int
            L.append(rand_int)
        direct_mean = direct_sum / 100

        r = gcs.list_mean(L)
        self.assertEqual(r, direct_mean)

    def test_list_mean_Errors(self):
        self.assertRaises(ZeroDivisionError, gcs.list_mean, [])
        self.assertRaises(TypeError, gcs.list_mean, None)

    def test_stdev_const_small(self):
        r = gcs.stdev([1, 1, 1])
        self.assertEqual(r, 0)

    def test_stdev_rand_small(self):
        L = [random.randint(1, 10) for i in range(5)]
        m = gcs.list_mean(L)
        direct_sum = 0
        for i in range(5):
            direct_sum += (L[i] - m) ** 2
        direct_stdev = math.sqrt(direct_sum / 5)

        r = gcs.stdev(L)
        self.assertEqual(r, direct_stdev)

    def test_stdev_rand_large(self):
        L = [random.randint(1, 10) for i in range(100)]
        m = gcs.list_mean(L)
        direct_sum = 0
        for i in range(100):
            direct_sum += (L[i] - m) ** 2
        direct_stdev = math.sqrt(direct_sum / 100)

        r = gcs.stdev(L)
        self.assertEqual(r, direct_stdev)

    def test_stdev_Errors(self):
        rand_list = [random.randint(1, 10) for x in range(10)]
        self.assertRaises(ZeroDivisionError, gcs.stdev, [])
        self.assertRaises(TypeError, gcs.stdev, None)


if __name__ == '__main__':
    unittest.main()
