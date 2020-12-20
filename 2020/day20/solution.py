from math import prod, sqrt

transpose = lambda tile: list(''.join(line) for line in zip(*tile))
invert = lambda tile: [''.join(reversed(line)) for line in tile]
rotate = lambda tile: invert(transpose(tile))


def parse(text: str):
  tiles = dict()
  tile_sides = dict()
  for block in text.split("\n\n"):
    lines = block.splitlines()
    sides = [lines[1], lines[-1], "".join(l[0] for l in lines[1:]), "".join(l[-1] for l in lines[1:])]
    sides += [s[::-1] for s in sides]
    id = int(lines[0].split(" ")[1][:-1])
    tile_sides[id] = sides
    tiles[id] = lines[1:]
  adjacents = dict()
  for k, sides in tile_sides.items():
    adjacents[k] = set.union(
      *map(set, list([j for j in tile_sides.keys() if side in tile_sides[j] and j != k] for side in sides)))
  return tiles, adjacents


def solve_part_1(text: str):
  _, adjacents = parse(text)
  return prod([k for k, sides in adjacents.items() if len(sides) == 2])


def solve_part_2(text: str):
  tiles, adjacents = parse(text)
  N = int(sqrt(len(tiles)))
  board = [[None] * N for _ in range(N)]
  print(rotate(tiles[3079]))


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
