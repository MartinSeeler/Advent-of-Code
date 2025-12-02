import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""", 1227775554)
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""", 4174379265)
])
def test_part_2_solution(quiz_input, expected_result):
  assert solve_part_2(quiz_input) == expected_result
