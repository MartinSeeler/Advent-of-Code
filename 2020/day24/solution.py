import re
from collections import Counter

DIRS = list(map(lambda x: re.compile(f"^{x}"), ["w", "e", "se", "sw", "ne", "nw"]))
DIR_STEPS = [(-1, 0), (1, 0), (0, -1), (-1, -1), (1, 1), (0, 1)]


def go(t1: (int, int), dir: (int, int)) -> (int, int):
  return t1[0] + dir[0], t1[1] + dir[1]


def follow(path: str, target=(0, 0)):
  if not path:
    return target
  for ix, p in enumerate(DIRS):
    if match := re.match(p, path):
      next_dir = DIR_STEPS[ix]
      return follow(path[len(match.group()):], go(target, next_dir))


def get_neighbors(tile: (int, int)) -> [(int, int)]:
  return [go(tile, dir) for dir in DIR_STEPS]


def count_black_neighbors(tile: (int, int), c: Counter):
  return sum([is_black(neighbor, c) for neighbor in get_neighbors(tile)])


def is_black(tile: (int, int), c: Counter) -> bool:
  return tile in c and c[tile] % 2 == 1


def conway(c: Counter) -> Counter:
  new_c = Counter(c)
  for tile in c.keys():
    if is_black(tile, c):
      black_neighbors = count_black_neighbors(tile, c)
      new_c[tile] = 0 if (black_neighbors == 0 or black_neighbors > 2) else 1
    else:
      black_neighbors = count_black_neighbors(tile, c)
      new_c[tile] = 1 if black_neighbors == 2 else 0
    for neighbor in get_neighbors(tile):
      if neighbor not in c:
        black_neighbors = count_black_neighbors(neighbor, c)
        new_c[neighbor] = 1 if black_neighbors == 2 else 0
  return new_c


def get_initial_map(text: str) -> Counter:
  paths = text.splitlines()
  c = Counter()
  for target in map(follow, paths):
    c[target] += 1
  return c


def solve_part_1(text: str):
  c = get_initial_map(text)
  return sum([is_black(tile, c) for tile in c.keys()])


def solve_part_2(text: str, days: int):
  c = get_initial_map(text)
  for _ in range(days):
    c = conway(c)
  return sum([is_black(tile, c) for tile in c.keys()])


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input, 100))
