def sa(w: int, l: int, h: int) -> int:
  x = l * w
  y = w * h
  z = h * l
  return (2 * x + 2 * y + 2 * z) + min([x, y, z])


def ri(w: int, l: int, h: int) -> int:
  [x, y, z] = sorted([w, l, h])
  return 2 * x + 2 * y + (x * y * z)


def solve_part_1(text: str):
  return sum(map(lambda x: sa(*map(int, x.split("x"))), text.splitlines()))


def solve_part_2(text: str):
  return sum(map(lambda x: ri(*map(int, x.split("x"))), text.splitlines()))


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
