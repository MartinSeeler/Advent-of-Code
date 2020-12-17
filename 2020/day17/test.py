import pytest

from solution import solve


@pytest.mark.parametrize("quiz_input,cycles,expected_actives", [
  (""".#.
..#
###""", 0, 5),
  (""".#.
..#
###""", 1, 11),
  (""".#.
..#
###""", 2, 21),
  (""".#.
..#
###""", 3, 38),
  (""".#.
..#
###""", 6, 112)
])
def test_part_1_solution(quiz_input, cycles, expected_actives):
  assert solve(quiz_input, 3, cycles) == expected_actives


@pytest.mark.parametrize("quiz_input,cycles,expected_actives", [
  (""".#.
..#
###""", 0, 5),
  (""".#.
..#
###""", 1, 29),
  (""".#.
..#
###""", 6, 848)
])
def test_part_2_solution(quiz_input, cycles, expected_actives):
  assert solve(quiz_input, 4, cycles) == expected_actives
