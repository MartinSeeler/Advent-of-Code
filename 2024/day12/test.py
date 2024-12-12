import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """AAAA
BBCD
BBCC
EEEC""",
            140,
        ),
        (
            """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""",
            772,
        ),
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """AAAA
BBCD
BBCC
EEEC""",
            80,
        ),
        (
            """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""",
            436,
        ),
        (
            """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""",
            236,
        ),
        (
            """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""",
            368,
        ),
        (
            """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""",
            1206,
        ),
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
