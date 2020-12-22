import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""", 306)
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""", 0)
])
def test_part_2_solution(quiz_input, expected_result):
  assert solve_part_2(quiz_input) == expected_result
