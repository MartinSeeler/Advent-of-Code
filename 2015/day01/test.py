import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""(())""", 0),
  ("""()()""", 0),
  ("""(()(()(""", 3),
  ("""))(((((""", 3),
  ("""))(""", -1),
  (""")())())""", -3),
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  (""")""", 1),
  ("""()())""", 5)
])
def test_part_2_solution(quiz_input, expected_result):
  assert solve_part_2(quiz_input) == expected_result
