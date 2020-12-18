import pytest

from solution import strange_eval_1, strange_eval_2


@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""1 + 2 * 3 + 4 * 5 + 6""", 71),
  ("""1 + (2 * 3) + (4 * (5 + 6))""", 51),
  ("""2 * 3 + (4 * 5)""", 26),
  ("""5 + (8 * 3 + 9 + 3 * 4 * 3)""", 437),
  ("""5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))""", 12240),
  ("""((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2""", 13632),

])
def test_eval(quiz_input, expected_result):
  assert strange_eval_1(quiz_input) == expected_result

@pytest.mark.parametrize("quiz_input,expected_result", [
  ("""1 + 2 * 3 + 4 * 5 + 6""", 231),
  ("""1 + (2 * 3) + (4 * (5 + 6))""", 51),
  ("""2 * 3 + (4 * 5)""", 46),
  ("""5 + (8 * 3 + 9 + 3 * 4 * 3)""", 1445),
  ("""5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))""", 669060),
  ("""((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2""", 23340),

])
def test_eval2(quiz_input, expected_result):
  assert strange_eval_2(quiz_input) == expected_result
