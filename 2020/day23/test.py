import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize("quiz_input,rounds,expected_result", [
  ("""389125467""", 10, "92658374"),
  ("""389125467""", 100, "67384529")
])
def test_part_1_solution(quiz_input, rounds, expected_result):
  assert solve_part_1(quiz_input, rounds) == expected_result


@pytest.mark.parametrize("quiz_input,rounds,expected_result", [
  ("""389125467""", 10000000, 149245887792)
])
def test_part_2_solution(quiz_input, rounds, expected_result):
  assert solve_part_2(quiz_input, rounds) == expected_result
