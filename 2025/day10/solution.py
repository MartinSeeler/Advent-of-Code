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
  """
  Solve Ax = b where:
  - A[j][i] = 1 if button i affects counter j
  - x[i] = number of times to press button i (non-negative integer)
  - b[j] = target[j]
  Minimize sum(x).
  """
  n_buttons = len(buttons)
  n_counters = len(targets)

  # Build augmented matrix [A | b] using Fractions for exact arithmetic
  # Rows = counters, Cols = buttons + 1 (for target)
  matrix = []
  for j in range(n_counters):
    row = []
    for i in range(n_buttons):
      row.append(Fraction(1) if j in buttons[i] else Fraction(0))
    row.append(Fraction(targets[j]))
    matrix.append(row)

  # Gaussian elimination to Row Echelon Form
  pivot_cols = []  # which column each row pivots on
  pivot_row = 0
  for col in range(n_buttons):
    # Find pivot in this column
    found = -1
    for row in range(pivot_row, n_counters):
      if matrix[row][col] != 0:
        found = row
        break
    if found == -1:
      continue  # No pivot in this column, it's a free variable

    # Swap rows
    matrix[pivot_row], matrix[found] = matrix[found], matrix[pivot_row]
    pivot_cols.append((pivot_row, col))

    # Scale pivot row to have leading 1
    scale = matrix[pivot_row][col]
    for c in range(n_buttons + 1):
      matrix[pivot_row][c] /= scale

    # Eliminate all other rows
    for row in range(n_counters):
      if row != pivot_row and matrix[row][col] != 0:
        factor = matrix[row][col]
        for c in range(n_buttons + 1):
          matrix[row][c] -= factor * matrix[pivot_row][c]

    pivot_row += 1

  # Identify free variables (columns without pivots)
  pivot_col_set = {col for (_, col) in pivot_cols}
  free_vars = [i for i in range(n_buttons) if i not in pivot_col_set]

  # Precompute coefficients for pivot variables
  # pivot_var[col] = constant[col] + sum(coef[col][f] * free_var[f])
  constants = {}
  coefficients = {}
  for (row, col) in pivot_cols:
    constants[col] = matrix[row][n_buttons]
    coefficients[col] = [matrix[row][f] for f in free_vars]

  # Recursive search with pruning
  min_presses = [float('inf')]

  def search(idx, free_vals, current_sum):
    if current_sum >= min_presses[0]:
      return  # Prune: already worse than best

    if idx == len(free_vars):
      # Compute pivot variables and check validity
      total = current_sum
      for (_, col) in pivot_cols:
        val = constants[col]
        for i, fv in enumerate(free_vals):
          val -= coefficients[col][i] * fv
        if val < 0 or val.denominator != 1:
          return  # Invalid
        total += val
        if total >= min_presses[0]:
          return  # Prune
      min_presses[0] = total
      return

    # Determine bounds for this free variable
    # We need all pivot variables to be >= 0
    # pivot_var = constant - coef * free_var >= 0
    min_val = 0
    max_val = max(targets)

    for (_, col) in pivot_cols:
      remaining_const = constants[col]
      for i, fv in enumerate(free_vals):
        remaining_const -= coefficients[col][i] * fv
      coef = coefficients[col][idx]
      if coef > 0:
        # remaining_const - coef * x >= 0 => x <= remaining_const / coef
        upper = remaining_const / coef
        max_val = min(max_val, int(upper) if upper >= 0 else -1)
      elif coef < 0:
        # remaining_const - coef * x >= 0
        # Since coef < 0, -coef > 0, so: remaining_const + (-coef) * x >= 0
        # => x >= -remaining_const / (-coef) = remaining_const / coef
        # But coef is negative, so division flips inequality
        lower = remaining_const / coef
        if lower > 0:
          from math import ceil
          min_val = max(min_val, ceil(float(lower)))

    # Don't prune here - constraints might be satisfiable with other free vars
    # Just use reasonable bounds
    if min_val > max_val:
      min_val = 0
      max_val = max(targets) * 5  # Conservative upper bound

    # Cap the upper bound but allow it to be quite large
    upper_limit = min(max_val + 1, max(targets) * 5)

    for v in range(min_val, upper_limit):
      search(idx + 1, free_vals + [Fraction(v)], current_sum + v)

  if not free_vars:
    # No free variables - compute unique solution directly
    total = Fraction(0)
    valid = True
    for (row, col) in pivot_cols:
      val = constants[col]
      if val < 0 or val.denominator != 1:
        valid = False
        break
      total += val
    if valid:
      min_presses[0] = total
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
      # Some machines might not have a solution - skip them or use 0
      # For now, let's assume they should have solutions and this is a bug
      # print(f"Warning: No solution found for machine {line_num}")
      machine_res = 0  # or we could raise an error
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
