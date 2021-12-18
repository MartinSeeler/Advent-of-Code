import pytest

from solution import solve_part_1, solve_part_2, add, explode, split, magnitude


@pytest.mark.parametrize(
    "input,expected_result",
    [
        (([[[[[9, 8], 1], 2], 3], 4], (True, 9, [[[[0, 9], 2], 3], 4], None))),
        ([7, [6, [5, [4, [3, 2]]]]], (True, None, [7, [6, [5, [7, 0]]]], 2)),
        ([[6, [5, [4, [3, 2]]]], 1], (True, None, [[6, [5, [7, 0]]], 3], None)),
        (
            [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
            (True, None, [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], None),
        ),
        (
            [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
            (True, None, [[3, [2, [8, 0]]], [9, [5, [7, 0]]]], 2),
        ),
        (
            [1, [3, 2]],
            (False, None, [1, [3, 2]], None),
        ),
    ],
)
def test_explode(input, expected_result):
    assert explode(input) == expected_result


@pytest.mark.parametrize(
    "input,expected_result",
    [
        (
            [[[[0, 7], 4], [15, [0, 13]]], [1, 1]],
            (True, [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]),
        ),
        (
            [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]],
            (True, [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]),
        ),
        (
            [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]],
            (False, [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]),
        ),
    ],
)
def test_split(input, expected_result):
    assert split(input) == expected_result


@pytest.mark.parametrize(
    "left,right,expected_result",
    [
        (
            [[[[4, 3], 4], 4], [7, [[8, 4], 9]]],
            [1, 1],
            [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]],
        )
    ],
)
def test_add(left, right, expected_result):
    assert add(left, right) == expected_result


@pytest.mark.parametrize(
    "input,expected_result",
    [
        ([1, 9], 21),
        ([9, 1], 29),
        ([[9, 1], [1, 9]], 129),
        ([[1, 2], [[3, 4], 5]], 143),
        ([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384),
        ([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 445),
        ([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 791),
        ([[[[5, 0], [7, 4]], [5, 5]], [6, 6]], 1137),
        ([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488),
    ],
)
def test_magnitude(input, expected_result):
    assert magnitude(input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""",
            4140,
        )
    ],
)
def test_part_1_solution(quiz_input, expected_result):
    assert solve_part_1(quiz_input) == expected_result


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        (
            """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""",
            3993,
        )
    ],
)
def test_part_2_solution(quiz_input, expected_result):
    assert solve_part_2(quiz_input) == expected_result
