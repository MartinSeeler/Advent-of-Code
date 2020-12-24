import pytest

from solution import solve_part_1, solve_part_2

test_input = """\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""


def test_part_1_solution():
  assert solve_part_1(test_input) == 10


@pytest.mark.parametrize("days,expected_result", [
  (1, 15),
  (2, 12),
  (3, 25),
  (4, 14),
  (5, 23),
  (8, 37),
  (20, 132),
  (30, 259),
  (50, 566),
  (80, 1373),
  (100, 2208)
])
def test_part_2_solution(days, expected_result):
  assert solve_part_2(test_input, days) == expected_result
