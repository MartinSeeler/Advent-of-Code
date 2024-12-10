import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """0123
1234
8765
9876""",
            1,
        ),
        (
            """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9""",
            2,
        ),
        (
            """..90..9
...1.98
...2..7
6543456
765.987
876....
987....""",
            4,
        ),
        (
            """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""",
            36,
        ),
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """\
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....""",
            3,
        ),
        (
            """..90..9
...1.98
...2..7
6543456
765.987
876....
987....""",
            13,
        ),
        (
            """012345
123456
234567
345678
4.6789
56789.""",
            227,
        ),
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
