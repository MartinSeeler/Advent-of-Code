import time
from pathlib import Path


def solve_part_1(text: str):
  lines = text.strip().splitlines()
  beams = [lines[0].index('S')]
  print(beams)
  splits = 0
  for line in lines[1:]:
    new_beams = []
    for beam in beams:
      if line[beam] == '^':
        new_beams.append(beam - 1)
        new_beams.append(beam + 1)
        splits += 1
      else:
        new_beams.append(beam)
    beams = sorted(list(set(new_beams)))
    # print(f"line: {line} beams: {beams}")
  return splits

def solve_part_2(text: str):
  lines = text.strip().splitlines()
  beams = [(lines[0].index('S'), 1)]
  print(beams)
  splits = 0
  for line in lines[1:]:
    new_beams = []
    for (beam, depth) in beams:
      if line[beam] == '^':
        new_beams.append((beam - 1, depth))
        new_beams.append((beam + 1, depth))
        splits += 1
      else:
        new_beams.append((beam, depth))
    # beams with same pos needs to sum their depths
    beams_dict = {}
    for (beam, depth) in new_beams:
      if beam in beams_dict:
        beams_dict[beam] += depth
      else:
        beams_dict[beam] = depth
    beams = sorted([(beam, depth) for beam, depth in beams_dict.items()])
    print(f"line: {line} beams: {beams}") 

  return sum(depth for (beam, depth) in beams)


if __name__ == '__main__':
  with open(Path(__file__).parent / "input.txt", "r") as f:
    quiz_input = f.read()
    start = time.time()
    p_1_solution = int(solve_part_1(quiz_input))
    middle = time.time()
    print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
    p_2_solution = int(solve_part_2(quiz_input))
    end = time.time()
    print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
