def solve_part_1(text: str):
  nums = [int(x) for x in text.strip().split(",")]
  turn = len(nums) + 1
  memory = {x: [n+1] for n, x in enumerate(nums)}
  last = nums[-1]
  while turn <= 2020:
    if turn < 10:
      print(turn, last, memory)
    if last in memory and len(memory[last]) == 1:
      last = 0
      memory[last] = [turn] if last not in memory else memory[last] + [turn]
    elif last in memory and len(memory[last]) > 1:
      last = memory[last][-1] - memory[last][-2]
      memory[last] = [turn] if last not in memory else memory[last] + [turn]
    turn += 1
  return last


def solve_part_2(text: str):
  nums = [int(x) for x in text.strip().split(",")]
  turn = len(nums) + 1
  memory = {x: [n + 1] for n, x in enumerate(nums)}
  last = nums[-1]
  while turn <= 30000000:
    if turn % 10000 == 0:
      print(turn, last)
    if last in memory and len(memory[last]) == 1:
      last = 0
      memory[last] = [turn] if last not in memory else [memory[last][-1]] + [turn]
    elif last in memory and len(memory[last]) > 1:
      last = memory[last][-1] - memory[last][-2]
      memory[last] = [turn] if last not in memory else [memory[last][-1]] + [turn]
    else:
      memory[last] = [turn]
    turn += 1
  return last


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
