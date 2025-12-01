from pathlib import Path
import time


def solve_part_1(text: str) -> int:
    directions = {"L": -1, "R": 1}
    x = 50
    hits = 0
    for line in text.splitlines():
        line = line.strip()
        x = (x + int(line[1:]) * directions[line[0]]) % 100
        hits += x == 0
    return hits


def solve_part_2(text: str):
  directions = {"L": -1, "R": 1}
  x = 50
  hits = 0
  for line in text.splitlines():
      line = line.strip()
      d = int(line[1:]) * directions[line[0]]
      new_raw = x + d
      if d > 0:
          hits += new_raw // 100
      elif d < 0 and new_raw <= 0:
          hits += (-new_raw) // 100 + (1 if x > 0 else 0)
      x = new_raw % 100
  return hits


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
