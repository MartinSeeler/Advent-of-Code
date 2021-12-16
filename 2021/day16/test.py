import pytest

from solution import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "quiz_input,expected_result",
    [
        ("""D2FE28""", 1),
        ("""38006F45291200""", 1),
        ("""EE00D40C823060""", 1),
        # ("""8A004A801A8002F478""", 16),
        # ("""620080001611562C8802118E34""", 12),
        # ("""C0015000016115A2E0802F182340""", 23),
        # ("""A0016C880162017C3686B18A3D4780""", 31),
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
