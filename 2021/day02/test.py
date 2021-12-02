import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """forward 5
down 5
forward 8
up 3
down 8
forward 2""",
            150,
        )
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """forward 5
down 5
forward 8
up 3
down 8
forward 2""",
            900,
        )
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
