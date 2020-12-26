import operator
from itertools import accumulate
from typing import Set

DIRS = [1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j]


def travel(text: str) -> Set[complex]:
  return set(accumulate(map(lambda x: DIRS[["^", "v", "<", ">"].index(x)], text), operator.add, initial=(0 + 0j)))


def solve_part_1(text: str) -> int:
  return len(travel(text))


def solve_part_2(text: str) -> int:
  return len(travel(text[::2]) | travel(text[1::2]))


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
