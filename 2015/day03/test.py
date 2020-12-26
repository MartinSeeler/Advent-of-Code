import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize("quiz_input,expected_result", [
  (""">""", 2),
  ("""^>v<""", 4),
  ("""^v^v^v^v^v""", 2)
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""^v""", 3),
  ("""^>v<""", 3),
  ("""^v^v^v^v^v""", 11)
])
def test_part_2_solution(quiz_input, expected_result):
  assert solve_part_2(quiz_input) == expected_result
