import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """2333133121414131402""",
            1928,
        )
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """2333133121414131402""",
            2858,
        )
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
