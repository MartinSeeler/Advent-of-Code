import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""\
      123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +""", 4277556)
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +""", 3263827)
])
def test_part_2_solution(quiz_input, expected_result):
  assert solve_part_2(quiz_input) == expected_result
