import pytest

from solution import decode, solve_part_1, solve_part_2


@pytest.mark.parametrize("pub,subject_number,expected_result", [
  (5764801, 7, 8),
  (17807724, 7, 11),
])
def test_decode_solution(pub, subject_number, expected_result):
  assert decode(pub, subject_number) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""\
5764801
17807724""", 14897079)
])
def test_part_1_solution(quiz_input, expected_result):
  assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""\
      fill
      me
      in""", 0)
])
def test_part_2_solution(quiz_input, expected_result):
  assert solve_part_2(quiz_input) == expected_result
