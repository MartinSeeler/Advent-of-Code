import time
from pathlib import Path


def solve_part_1(text: str):
  lines = text.strip().splitlines()
  nums = [int(num) for line in lines[:-1] for num in line.split() if num.isdigit()]
  ops = [c for c in lines[-1] if c in '+*']
  cols = len(ops)
  res = 0
  for i in range(cols):
    if ops[i] == '+':
      res += sum(nums[i::cols])
    elif ops[i] == '*':
      prod = 1
      for n in nums[i::cols]:
        prod *= n
      res += prod
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
      # empty row, skip
      # process numbers
      if ops[op_idx] == '+':
        res += sum(nums)
      elif ops[op_idx] == '*':
        prod = 1
        for n in nums:
          prod *= n
        res += prod
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

  



  nums = [int(num) for line in lines[:-1] for num in line.split() if num.isdigit()]
  ops = [c for c in lines[-1] if c in '+*']
  cols = len(ops)
  res = 0
  for i in range(cols):
    if ops[i] == '+':
      res += sum(nums[i::cols])
    elif ops[i] == '*':
      prod = 1
      for n in nums[i::cols]:
        prod *= n
      res += prod
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
