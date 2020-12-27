from typing import List

keypad1: List[List[str]] = [
  ["1", "2", "3"],
  ["4", "5", "6"],
  ["7", "8", "9"]
]

keypad2: List[List[str]] = [
  [None, None, "1", None, None],
  [None, "2", "3", "4", None],
  ["5", "6", "7", "8", "9"],
  [None, "A", "B", "C", None],
  [None, None, "D", None, None]
]


def travel(text: str, start, keypad: List[List[str]]) -> str:
  [(x, y)] = [(ix, iy) for ix, row in enumerate(keypad) for iy, i in enumerate(row) if i == start]
  for i in text:
    if i in "UD":
      next_x = max(0, x - 1) if i == "U" else min(len(keypad) - 1, x + 1)
      if keypad[next_x][y] is not None:
        x = next_x
    else:
      next_y = min(len(keypad[0]) - 1, y + 1) if i == "R" else max(0, y - 1)
      if keypad[x][next_y] is not None:
        y = next_y
  return keypad[x][y]


def solve(text: str, keypad: List[List[str]]):
  from_key = "5"
  code = ""
  for line in text.splitlines():
    next_key = travel(line, from_key, keypad)
    from_key = next_key
    code += next_key
  return code


def solve_part_1(text: str):
  return solve(text, keypad1)


def solve_part_2(text: str):
  return solve(text, keypad2)


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
