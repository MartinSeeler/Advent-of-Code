import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""",
            40,
        )
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""",
            315,
        )
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
