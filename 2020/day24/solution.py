import re
from collections import Counter

DIRS = list(map(lambda x: re.compile(f"^{x}"), ["w", "e", "se", "sw", "ne", "nw"]))
DIR_STEPS = [(-1, 0), (1, 0), (0, -1), (-1, -1), (1, 1), (0, 1)]


def follow(path: str, target=(0, 0)):
  if not path:
    return target
  for ix, p in enumerate(DIRS):
    if match := re.match(p, path):
      next_dir = DIR_STEPS[ix]
      return follow(path[len(match.group()):], (target[0] + next_dir[0], target[1] + next_dir[1]))


def solve_part_1(text: str):
  paths = text.splitlines()
  c = Counter()
  for path in paths:
    c[follow(path)] += 1
  return sum([1 for k, v in c.items() if v % 2 == 1])


def solve_part_2(text: str):
  pass


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
