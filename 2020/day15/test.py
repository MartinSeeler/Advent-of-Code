import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""0,3,6""", 436),
  ("""1,3,2""", 1),
  ("""2,1,3""", 10),
  ("""1,2,3""", 27),
  ("""2,3,1""", 78),
  ("""3,2,1""", 438),
  ("""3,1,2""", 1836),
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""0,3,6""", 175594),
  ("""1,3,2""", 2587),
  ("""2,1,3""", 3544142),
  ("""1,2,3""", 261214),
  ("""2,3,1""", 6895259),
  ("""3,2,1""", 18),
  ("""3,1,2""", 362),
])
def test_part_2_solution(quiz_input, expected_result):
  assert solve_part_2(quiz_input) == expected_result
