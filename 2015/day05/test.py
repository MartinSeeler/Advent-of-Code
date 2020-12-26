import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""ugknbfddgicrmopn""", 1),
  ("""aaa""", 1),
  ("""jchzalrnumimnmhp""", 0),
  ("""haegwjzuvuyypxyu""", 0),
  ("""dvszwmarrgswjxmb""", 0),
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""qjhvhtzxzqqjkmpb""", 1),
  ("""xxyxx""", 1),
  ("""uurcxstgmygtbstg""", 0),
  ("""ieodomkazucvgmuy""", 0),
])
def test_part_2_solution(quiz_input, expected_result):
  assert solve_part_2(quiz_input) == expected_result
