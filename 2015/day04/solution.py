import hashlib
from itertools import count, dropwhile


def solve_part_1(text: str) -> int:
  return next(dropwhile(lambda x: not hashlib.md5(f"{text}{x}".encode("utf-8")).hexdigest().startswith("00000"), count(0)))


def solve_part_2(text: str):
  return next(dropwhile(lambda x: not hashlib.md5(f"{text}{x}".encode("utf-8")).hexdigest().startswith("000000"), count(0)))


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
