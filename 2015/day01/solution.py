from itertools import accumulate
import operator


def solve_part_1(text: str) -> int:
  return sum(1 if x == "(" else -1 for x in text)


def solve_part_2(text: str) -> object:
  return list(accumulate([1 if x == "(" else -1 for x in text], func=operator.add, initial=0)).index(-1)


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
