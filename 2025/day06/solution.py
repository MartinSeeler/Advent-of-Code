import time
from pathlib import Path
from math import prod


def solve_part_1(text: str):
  lines = text.strip().splitlines()
  nums = [int(num) for line in lines[:-1] for num in line.split() if num.isdigit()]
  ops = [c for c in lines[-1] if c in '+*']
  cols = len(ops)
  res = 0
  for i in range(cols):
    res += sum(nums[i::cols]) if ops[i] == '+' else prod(nums[i::cols])
  return res


def solve_part_2(text: str):
  lines = text.strip().splitlines()
  numbers = lines[:-1]
  number_lines_count = len(lines) - 1
  ops = [c for c in lines[-1] if c in '+*']
  res = 0
  op_idx = len(ops) - 1
  col_idx = len(numbers[0]) - 1
  nums = []
  while col_idx >= -1 and op_idx >= 0:
    # if all nums in this column are spaces, skip and decrement op_idx
    if all(line[col_idx] == ' ' for line in numbers) or col_idx == -1:
      res += sum(nums) if ops[op_idx] == '+' else prod(nums)
      nums = []
      op_idx -= 1
    else:
      # number, aprse from top to bottom
      num = ""
      for row_idx in range(number_lines_count):
        c = numbers[row_idx][col_idx]
        if c.isdigit():
          num += c
      if num:
        nums.append(int(num))
    col_idx -= 1

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
