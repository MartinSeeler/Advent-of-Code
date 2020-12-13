import unittest

from day13_2 import solve


class TestDay05Methods(unittest.TestCase):

    def test_sample_1(self):
        self.assertEqual(solve("17,x,13,19"), 3417)

    def test_sample_2(self):
        self.assertEqual(solve("67,7,59,61"), 754018)

    def test_sample_3(self):
        self.assertEqual(solve("67,x,7,59,61"), 779210)

    def test_sample_4(self):
        self.assertEqual(solve("67,7,x,59,61"), 1261476)

    def test_sample_5(self):
        self.assertEqual(solve("1789,37,47,1889"), 1202161486)

if __name__ == '__main__':
    unittest.main()
