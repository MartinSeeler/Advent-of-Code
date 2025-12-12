import time
from pathlib import Path
from fractions import Fraction

# Source - https://stackoverflow.com/a/1482316
# Posted by Mark Rushakoff, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-10, License - CC BY-SA 4.0

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def solve_part_1(text: str):
  res = 0
  for line in text.strip().splitlines():
    # example line
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    parts = line.split(" ")
    grid_part = parts[0]
    grid = grid_part.strip("[]")
    grid_len = len(grid)
    buttons = [b.strip("()") for b in parts[1:-1]]
    # now we need a bit mask with each index from buttons a 1, the whole mask has a length of grid_len
    button_masks = []
    for b in buttons:
      bitmask = 0
      b_ints = [int(x) for x in b.split(",")]
      for bi in b_ints:
        bitmask |= (1 << (grid_len - 1 - bi))
      button_masks.append(bitmask)
      # print(f"Button {bitmask:0{grid_len}b}")
      
    # Now we need a bit mask for the grid itself, where # is 1 and . is 0
    grid_mask = 0
    for i, c in enumerate(grid):
      if c == "#":
        grid_mask |= (1 << (grid_len - 1 - i))
    # print(f"Grid {grid_mask:0{grid_len}b}")

    # now generate all subsets of button_masks
    min_size = 99999999999
    for s in powerset(button_masks):
      # XOR all masks
      xor_mask = 0
      for mask in s:
        xor_mask ^= mask
      if xor_mask == grid_mask:
        # print(f"Match found with subset: {s}")
        if len(s) < min_size:
          min_size = len(s)
    res += min_size
  return res



def solve_machine_part2(buttons, targets):
  n_buttons = len(buttons)
  n_counters = len(targets)

  # Build augmented matrix [A | b] using Fractions for exact arithmetic
  matrix = []
  for j in range(n_counters):
    row = []
    for i in range(n_buttons):
      row.append(Fraction(1) if j in buttons[i] else Fraction(0))
    row.append(Fraction(targets[j]))
    matrix.append(row)

  pivot_cols = []
  pivot_row = 0
  for col in range(n_buttons):
    # Find pivot in this column
    found = -1
    for row in range(pivot_row, n_counters):
      if matrix[row][col] != 0:
        found = row
        break
    if found == -1:
      continue

    matrix[pivot_row], matrix[found] = matrix[found], matrix[pivot_row]
    pivot_cols.append(col)

    scale = matrix[pivot_row][col]
    for c in range(n_buttons + 1):
      matrix[pivot_row][c] /= scale

    for row in range(n_counters):
      if row != pivot_row and matrix[row][col] != 0:
        factor = matrix[row][col]
        for c in range(n_buttons + 1):
          matrix[row][c] -= factor * matrix[pivot_row][c]

    pivot_row += 1

  n_pivots = pivot_row
  pivot_col_set = set(pivot_cols)
  free_cols = [i for i in range(n_buttons) if i not in pivot_col_set]

  # Check for inconsistent system
  for row in range(n_pivots, n_counters):
    if matrix[row][n_buttons] != 0:
      return float('inf')

  # Build expressions: pivot_var = const - sum(coef * free_var)
  expressions = []
  for i, col in enumerate(pivot_cols):
    const = matrix[i][n_buttons]
    coefs = [(j, matrix[i][free_cols[j]]) for j in range(len(free_cols)) if matrix[i][free_cols[j]] != 0]
    expressions.append((col, const, coefs))

  min_presses = [float('inf')]

  def search(idx, free_vals, current_sum):
    if current_sum >= min_presses[0]:
      return

    if idx == len(free_cols):
      total = current_sum
      for pivot_col, const, coefs in expressions:
        val = const
        for j, coef in coefs:
          val -= coef * free_vals[j]
        if val < 0 or val.denominator != 1:
          return
        total += int(val)
        if total >= min_presses[0]:
          return
      min_presses[0] = total
      return

    min_val = 0
    max_val = sum(targets)

    for pivot_col, const, coefs in expressions:
      remaining = const
      for j, coef in coefs:
        if j < idx:
          remaining -= coef * free_vals[j]

      coef_current = Fraction(0)
      has_later_free = False
      for j, coef in coefs:
        if j == idx:
          coef_current = coef
        elif j > idx and coef != 0:
          has_later_free = True

      if coef_current > 0 and not has_later_free:
        upper = remaining / coef_current
        if upper < 0:
          return
        max_val = min(max_val, int(upper))

    if max_val < 0:
      return

    for v in range(min_val, max_val + 1):
      search(idx + 1, free_vals + [Fraction(v)], current_sum + v)

  if not free_cols:
    total = Fraction(0)
    valid = True
    for pivot_col, const, coefs in expressions:
      if const < 0 or const.denominator != 1:
        valid = False
        break
      total += const
    if valid:
      min_presses[0] = int(total)
  else:
    search(0, [], 0)

  return min_presses[0]


def solve_part_2(text: str):
  res = 0
  for line_num, line in enumerate(text.strip().splitlines(), 1):
    # example line
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    parts = line.split(" ")

    # Parse buttons - each button is a set of counter indices it affects
    buttons = []
    for b in parts[1:-1]:
      b_str = b.strip("()")
      b_indices = set(int(x) for x in b_str.split(","))
      buttons.append(b_indices)

    # Parse targets from {3,5,4,7}
    target_part = parts[-1].strip("{}")
    targets = [int(x) for x in target_part.split(",")]

    machine_res = solve_machine_part2(buttons, targets)
    if machine_res == float('inf'):
      machine_res = 0
    res += machine_res
  return res


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
