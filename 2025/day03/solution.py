import time
from pathlib import Path


def foo(nums: list[int], rem: int, res = ""):
  if rem == 0:
    return res
  top = max(nums[:len(nums)-rem+1])
  return foo(nums[nums.index(top) + 1:], rem - 1, res + str(top))


def solve_part_1(text: str):
  return sum(
      int(foo(list(map(int, line.strip())), 2))
      for line in text.strip().splitlines()
  )



def solve_part_2(text: str):
  return sum(
      int(foo(list(map(int, line.strip())), 12))
      for line in text.strip().splitlines()
  )


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
