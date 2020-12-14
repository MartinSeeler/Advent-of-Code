from collections import defaultdict
import re


def clear_bit(position, value):
  return value & ~(1 << position)


def set_bit(position, value):
  bit_mask = 1 << position
  return bit_mask | value


def solve_part_1(text: str):
  memory = defaultdict(lambda: 0)
  lines = [x.strip() for x in text.splitlines()]
  mask = []
  for line in lines:
    if line.startswith("mask"):
      mask = [(idx, int(x)) for idx, x in enumerate(reversed(line.split(" = ")[1])) if x != "X"]
    else:
      match = re.match(r"^mem\[(\d+)\] = (\d+)", line, re.I)
      if match:
        idx, value = match.groups()
        real_value = int(value)
        for p, b in mask:
          real_value = set_bit(p, real_value) if b else clear_bit(p, real_value)
        # print("value", idx, value, real_value)
        memory[int(idx)] = real_value
  # print(memory)
  return sum(memory.values())


def solve_part_2(text: str):
  return 0


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
