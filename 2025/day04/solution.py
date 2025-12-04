import time
from pathlib import Path


def adjacent_positions(pos: complex, width: int, height: int) -> list[complex]:
  # returns all 8 adjacent positions, constraints to grid size are handled elsewhere
  return [
      pos + complex(dx, dy)
      for dx in [-1, 0, 1]
      for dy in [-1, 0, 1]
      if not (dx == 0 and dy == 0) and (0 <= pos.real + dx < width and 0 <= pos.imag + dy < height)
  ]

def solve_part_1(text: str):
  grid = [[c for c in line.strip()] for line in text.strip().splitlines()]
  res = 0
  for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
      pos = complex(x, y)
      if grid[y][x] == '@':
        adjacents = adjacent_positions(pos, len(grid[0]), len(grid))
        neighbors = sum(grid[int(adj.imag)][int(adj.real)] == '@' for adj in adjacents)
        if neighbors < 4:
          res += 1
  return res


def solve_part_2(text: str):
  grid = [[c for c in line.strip()] for line in text.strip().splitlines()]
  res = 0
  while True:
    to_be_removed = []
    for y in range(0, len(grid)):
      for x in range(0, len(grid[0])):
        pos = complex(x, y)
        if grid[y][x] == '@':
          adjacents = adjacent_positions(pos, len(grid[0]), len(grid))
          neighbors = sum(grid[int(adj.imag)][int(adj.real)] == '@' for adj in adjacents)
          if neighbors < 4:
            to_be_removed.append(pos)
    if not to_be_removed:
      break
    res += len(to_be_removed)
    for pos in to_be_removed:
      grid[int(pos.imag)][int(pos.real)] = '.'
  return res


if __name__ == '__main__':
  with open(Path(__file__).parent / "input.txt", "r") as f:
    quiz_input = f.read()
    start = time.time()
    p_1_solution = int(solve_part_1(quiz_input))
    middle = time.time()
    print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
    p_2_solution = int(solve_part_2(quiz_input))
    end = time.time()
    print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
