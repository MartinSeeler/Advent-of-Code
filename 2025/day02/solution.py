import time
from pathlib import Path

def split_in_n_parts(s: str, n: int) -> list[str]:
  """
  Splits a given string `s` into `n` equal parts and returns them as a list.
  Assumes that the length of `s` is divisible by `n`.
  Examples:
      split_in_n_parts("123123", 2) -> ["123", "123"]
      split_in_n_parts("123123123", 3) -> ["123", "123", "123"]
      split_in_n_parts("1212121212", 5) -> ["12", "12", "12", "12", "12"]
  """
  part_length = len(s) // n
  if len(s) % n != 0:
    return []
  return [s[i * part_length: (i + 1) * part_length] for i in range(n)]
  

def solve_part_1(text: str):
  ids = text.strip().split(",")
  sum = 0
  for id_pair in ids:
    start_str, end_str = id_pair.split("-")
    for x in range(int(start_str), int(end_str) + 1):
      x_str = str(x)
      parts = split_in_n_parts(x_str, 2)
      if len(parts) != 2:
        continue
      left, right = parts
      if left == right and left is not None:
        sum += x
  return sum
    


def solve_part_2(text: str):
  ids = text.strip().split(",")
  sum = 0
  for id_pair in ids:
    start_str, end_str = id_pair.split("-")
    for x in range(int(start_str), int(end_str) + 1):
      x_str = str(x)
      for length in range(2, len(x_str)+1):
        parts = split_in_n_parts(x_str, length)
        if len(parts) != length:
          continue
        if all(part == parts[0] and part is not None for part in parts):
          sum += x
          break
  return sum


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
