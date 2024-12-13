import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""",
            480,
        )
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """\
      fill
      me
      in""",
            0,
        )
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
