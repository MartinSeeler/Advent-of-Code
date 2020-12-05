import unittest

from day05 import get_row, get_column, get_seat_id


class TestDay05Methods(unittest.TestCase):

    def test_get_row(self):
        self.assertEqual(get_row('FBFBBFF'), 44)
        self.assertEqual(get_row('BFFFBBF'), 70)
        self.assertEqual(get_row('FFFBBBF'), 14)
        self.assertEqual(get_row('BBFFBBF'), 102)

    def test_get_column(self):
        self.assertEqual(get_column('RLR'), 5)
        self.assertEqual(get_column('RRR'), 7)
        self.assertEqual(get_column('RLL'), 4)

    def test_get_seat_id(self):
        self.assertEqual(get_seat_id('FBFBBFFRLR'), 357)
        self.assertEqual(get_seat_id('BFFFBBFRRR'), 567)
        self.assertEqual(get_seat_id('FFFBBBFRRR'), 119)
        self.assertEqual(get_seat_id('BBFFBBFRLL'), 820)


if __name__ == '__main__':
    unittest.main()
