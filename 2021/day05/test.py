import pytest

from solution import solve_part_1, solve_part_2, get_line_points


@pytest.mark.parametrize(
    "x1,y1,x2,y2,expected_result",
    [
        (1, 1, 1, 3, [(1, 1), (1, 2), (1, 3)]),
        (1, 1, 3, 3, [(1, 1), (2, 2), (3, 3)]),
        (9, 7, 7, 9, [(9, 7), (8, 8), (7, 9)]),
        (6, 4, 2, 0, [(6, 4), (5, 3), (4, 2), (3, 1), (2, 0)]),
    ],
)
def test_get_lines_solution(x1, y1, x2, y2, expected_result):
    assert list(get_line_points(x1, y1, x2, y2)) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""",
            5,
        )
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""",
            12,
        )
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
