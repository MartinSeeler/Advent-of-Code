import unittest

from solution import solve_part_1, solve_part_2


class TestSolutions(unittest.TestCase):

  def test_part_1_1(self):
    quiz_input = """\
                  1721
                  979
                  366
                  299
                  675
                  1456"""
    self.assertEqual(solve_part_1(quiz_input), 514579)

  def test_part_2_1(self):
    quiz_input = """\
                  1721
                  979
                  366
                  299
                  675
                  1456"""
    self.assertEqual(solve_part_2(quiz_input), 241861950)


if __name__ == '__main__':
  unittest.main()
