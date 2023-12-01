import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""",
            142,
        )
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""",
            281,
        )
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    pass
    # assert solve_part_2(quiz_input) == expected_result
