from collections import defaultdict
from itertools import product


def solve(quiz_input, dim=3, cycles=6):
  dirs = set(product(*(range(-1, 2) for _ in range(dim))))
  dirs.discard((0,) * dim)
  ons = set()
  for x, line in enumerate(quiz_input.splitlines()):
    for y, cube in enumerate(line):
      if cube == "#":
        ons.add((x, y) + (0,) * (dim - 2))
  for x in range(cycles):
    res = set()
    counter = defaultdict(lambda: 0)
    for o in ons:
      for d in dirs:
        counter[tuple(x1 + y1 for x1, y1 in zip(o, d))] += 1
    for o in ons:
      # toggle rule 1
      if 2 <= counter[o] <= 3:
        res.add(o)
    for o in set(counter.keys()) - ons:
      # toggle rule 2
      if counter[o] == 3:
        res.add(o)
    ons = res
  return len(ons)


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve(quiz_input, dim=3, cycles=6))
    print("Part 2:", solve(quiz_input, dim=4, cycles=6))
