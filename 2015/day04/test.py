import pytest

from solution import solve_part_1


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""abcdef""", 609043),
  ("""pqrstuv""", 1048970),
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result
