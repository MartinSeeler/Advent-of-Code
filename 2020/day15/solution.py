def solve(text: str, limit: int):
  nums = [int(x) for x in text.strip().split(",")]
  memory = {x: n + 1 for n, x in enumerate(nums)}
  last = nums[-1]
  for turn in range(len(nums) + 1, limit + 1):
    num = turn - 1 - memory[last] if last in memory else 0
    memory[last] = turn - 1
    last = num
  return last


def solve_part_1(text: str):
  return solve(text, 2020)


def solve_part_2(text: str):
  return solve(text, 30000000)


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
