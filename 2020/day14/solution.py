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
        memory[int(idx)] = real_value
  return sum(memory.values())


def solve_part_2(text: str):
  memory = defaultdict(lambda: 0)
  lines = [x.strip() for x in text.splitlines()]
  mask = []
  for line in lines:
    if line.startswith("mask"):
      mask = [(idx, x) for idx, x in enumerate(reversed(line.split(" = ")[1]))]
    else:
      match = re.match(r"^mem\[(\d+)\] = (\d+)", line, re.I)
      if match:
        address, value = match.groups()
        real_address = int(address)
        for p, b in mask:
          if b == "1":
            real_address = set_bit(int(p), real_address)
        addresses = [real_address]
        for p, b in mask:
          if b == "X":
            next_addresses = []
            for a in addresses:
              next_addresses.append(set_bit(int(p), a))
              next_addresses.append(clear_bit(int(p), a))
            addresses = next_addresses
        for a in set(addresses):
          memory[a] = int(value)
  return sum(memory.values())


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
