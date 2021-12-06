import pytest

from solution import solve


@pytest.mark.parametrize(
    "quiz_input,days,expected_result",
    [("""3,4,3,1,2""", 18, 26), ("""3,4,3,1,2""", 80, 5934)],
)
def test_part_1_solution(quiz_input, days, expected_result):
    assert solve(quiz_input, days) == expected_result


@pytest.mark.parametrize(
    "quiz_input,days,expected_result",
    [("""3,4,3,1,2""", 256, 26984457539)],
)
def test_part_2_solution(quiz_input, days, expected_result):
    assert solve(quiz_input, days) == expected_result
