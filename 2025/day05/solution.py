import time
from pathlib import Path

def merge_ranges(ranges_txt: str) -> list[tuple[int, int]]:
  ranges: list[tuple[int, int]] = []
  for line in ranges_txt.splitlines():
    start_str, end_str = line.split('-')
    ranges.append((int(start_str), int(end_str)))
  # sort ranges by start value
  ranges = sorted(ranges, key=lambda x: x[0])
  merged = []
  current_start, current_end = ranges[0]
  for r_start, r_end in ranges[1:]:
    if r_start <= current_end + 1:  # overlapping or contiguous
      current_end = max(current_end, r_end)
    else:
      merged.append((current_start, current_end))
      current_start, current_end = r_start, r_end
  merged.append((current_start, current_end))  # append the last range
  merged = sorted(merged, key=lambda x: x[0])
  return merged

def solve_part_1(text: str):
  ranges_txt, product_ids = text.strip().split('\n\n')
  ranges = merge_ranges(ranges_txt)
  product_ids_list = [int(line) for line in product_ids.splitlines()]
  count = 0
  for pid in product_ids_list:
    for r_start, r_end in ranges:
      if r_start <= pid <= r_end:
        count += 1
        break
  return count


def solve_part_2(text: str):
  ranges_txt = text.strip().split('\n\n')[0]
  ranges = merge_ranges(ranges_txt)
  total_covered = sum(end - start + 1 for start, end in ranges)
  return total_covered


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
