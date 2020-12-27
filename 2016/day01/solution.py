def solve_part_1(text: str) -> int:
  pos = 0 + 0j
  dirs = [0 + 1j, 1 + 0j, 0 - 1j, -1 + 0j]
  dir = dirs[0]
  for inst in text.split(", "):
    rot = inst[0]
    width = int(inst[1:])
    dir = dirs[(dirs.index(dir) + 1) % 4] if rot == "R" else dirs[(dirs.index(dir) - 1 + 4) % 4]
    pos += (width * dir)
  return int(abs(pos.real)) + int(abs(pos.imag))


def solve_part_2(text: str) -> int:
  pos = 0 + 0j
  dirs = [0 + 1j, 1 + 0j, 0 - 1j, -1 + 0j]
  dir = dirs[0]
  seen = set()
  seen.add(pos)
  for inst in text.split(", "):
    rot = inst[0]
    width = int(inst[1:])
    dir = dirs[(dirs.index(dir) + 1) % 4] if rot == "R" else dirs[(dirs.index(dir) - 1 + 4) % 4]
    for n in range(1, width + 1):
      also_seen = pos + (n * dir)
      if also_seen in seen:
        return int(abs(also_seen.real)) + int(abs(also_seen.imag))
      seen.add(also_seen)
    pos += (width * dir)
  return 0


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
