def decode(public_key: int, subject_number: int) -> int:
  v = 1
  x = 0
  while v != public_key:
    v = (v * subject_number) % 20201227
    x += 1
  return x


def transform(public_key: int, loop_size: int) -> int:
  v = 1
  for _ in range(loop_size):
    v = (v * public_key) % 20201227
  return v


def solve_part_1(text: str):
  [card, door] = [int(x) for x in text.splitlines()]
  c = decode(card, 7)
  d = decode(door, 7)
  return transform(card, d)


def solve_part_2(text: str):
  pass


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
