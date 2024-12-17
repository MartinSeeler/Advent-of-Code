import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""",
            "4,6,3,5,6,3,5,2,1,0",
        )
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""",
            117440,
        )
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
