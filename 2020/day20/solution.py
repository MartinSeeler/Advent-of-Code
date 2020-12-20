from math import prod


def solve_part_1(text: str):
  d = dict()
  for block in text.split("\n\n"):
    lines = block.splitlines()
    sides = [lines[1], lines[-1], "".join(l[0] for l in lines[1:]), "".join(l[-1] for l in lines[1:])]
    sides += [s[::-1] for s in sides]
    d[int(lines[0].split(" ")[1][:-1])] = sides
  e = dict()
  for k, sides in d.items():
    e[k] = set.union(*map(set, list([j for j in d.keys() if side in d[j] and j != k] for side in sides)))
  return prod([k for k, sides in e.items() if len(sides) == 2])


def solve_part_2(text: str):
  pass


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
