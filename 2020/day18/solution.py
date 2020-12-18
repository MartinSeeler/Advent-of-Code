import re


def strange_eval_1(text: str) -> int:
  if ms := re.search(r"(\((\d+)(\s([+*])\s(\d+))+\))", text):
    return strange_eval_1(text.replace(ms.groups()[0], str(strange_eval_1(ms.groups()[0][1:-1])), 1))
  if ms := re.match(r"(\d+)\s([+*])\s(\d+)", text):
    x, op, y = ms.groups()
    return strange_eval_1(text.replace(ms.group(), str(int(x) + int(y) if op == "+" else int(x) * int(y)), 1))
  return int(text)


def strange_eval_2(text: str) -> int:
  if ms := re.search(r"(\((\d+)(\s([+*])\s(\d+))+\))", text):
    return strange_eval_2(text.replace(ms.groups()[0], str(strange_eval_2(ms.groups()[0][1:-1])), 1))
  if ms := re.search(r"(\d+)\s\+\s(\d+)", text):
    return strange_eval_2(text.replace(ms.group(), str(int(ms.groups()[0]) + int(ms.groups()[1])), 1))
  if ms := re.match(r"(\d+)\s\*\s(\d+)", text):
    return strange_eval_2(text.replace(ms.group(), str(int(ms.groups()[0]) * int(ms.groups()[1])), 1))
  return int(text)


def solve_part_1(text: str):
  return sum([strange_eval_1(line) for line in text.splitlines()])


def solve_part_2(text: str):
  return sum([strange_eval_2(line) for line in text.splitlines()])


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
