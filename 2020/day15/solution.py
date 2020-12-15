def solve(text: str, limit: int):
  nums = [int(x) for x in text.strip().split(",")]
  turn = len(nums) + 1
  memory = {x: [n + 1] for n, x in enumerate(nums)}
  last = nums[-1]
  insert = lambda l, m, t: [t] if l not in m else [m[l][-1]] + [t]
  while turn <= limit:
    if last in memory and len(memory[last]) == 1:
      last = 0
      memory[last] = insert(last, memory, turn)
    elif last in memory and len(memory[last]) > 1:
      last = memory[last][-1] - memory[last][-2]
      memory[last] = insert(last, memory, turn)
    else:
      memory[last] = [turn]
    turn += 1
  return last


def solve_part_1(text: str):
  return solve(text, 2020)


def solve_part_2(text: str):
  solve(text, 30000000)


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
