import time
from pathlib import Path

def square_space(x1, y1, x2, y2):
  return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def solve_part_1(text: str):
  coords = []
  for line in text.strip().splitlines():
    x, y = map(int, line.split(","))
    coords.append((x, y))
  # calculate the square space distance from each coordinate to every other coordinate
  space = {}
  for i, (x1, y1) in enumerate(coords):
    for j, (x2, y2) in enumerate(coords):
      if i != j:
        dist = square_space(x1, y1, x2, y2)
        # print(f"Distance from ({x1},{y1}) to ({x2},{y2}) is {dist}")
        space[(i, j)] = dist
  # largest 
  largest = max(space.values())
  return largest


def is_point_in_polygon(x, y, polygon):
  """Check if point (x, y) is inside polygon using ray casting algorithm."""
  n = len(polygon)
  inside = False

  p1x, p1y = polygon[0]
  for i in range(1, n + 1):
    p2x, p2y = polygon[i % n]
    if y > min(p1y, p2y):
      if y <= max(p1y, p2y):
        if x <= max(p1x, p2x):
          if p1y != p2y:
            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
          if p1x == p2x or x <= xinters:
            inside = not inside
    p1x, p1y = p2x, p2y

  return inside


def is_on_polygon_edge(x, y, polygon):
  """Check if point (x, y) is on any edge of the polygon."""
  n = len(polygon)
  for i in range(n):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i + 1) % n]

    # Check if point is on the line segment between (x1, y1) and (x2, y2)
    if x1 == x2:  # Vertical line
      if x == x1 and min(y1, y2) <= y <= max(y1, y2):
        return True
    elif y1 == y2:  # Horizontal line
      if y == y1 and min(x1, x2) <= x <= max(x1, x2):
        return True

  return False


def is_valid_point(x, y, polygon, red_tiles, cache):
  """Check if point is red, on polygon edge, or inside polygon."""
  if (x, y) in red_tiles:
    return True
  if (x, y) in cache:
    return cache[(x, y)]
  result = is_on_polygon_edge(x, y, polygon) or is_point_in_polygon(x, y, polygon)
  cache[(x, y)] = result
  return result


def rectangle_fully_inside_polygon(rect_min_x, rect_min_y, rect_max_x, rect_max_y, polygon, red_tiles, cache):
  """
  Check if the rectangle is fully inside the polygon using crossing-based validation.
  For each rectangle edge, find polygon edge crossings and check midpoints between them.
  """
  # Check all 4 corners first (quick fail for many cases)
  corners = [
    (rect_min_x, rect_min_y),
    (rect_min_x, rect_max_y),
    (rect_max_x, rect_min_y),
    (rect_max_x, rect_max_y),
  ]
  for cx, cy in corners:
    if not is_valid_point(cx, cy, polygon, red_tiles, cache):
      return False

  n = len(polygon)

  # Top edge (y = rect_max_y): find x-coords where vertical polygon edges cross
  crossings = [rect_min_x, rect_max_x]
  for i in range(n):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i + 1) % n]
    if x1 == x2:  # Vertical polygon edge
      if min(y1, y2) <= rect_max_y <= max(y1, y2):
        if rect_min_x < x1 < rect_max_x:
          crossings.append(x1)
  crossings = sorted(set(crossings))
  for i in range(len(crossings) - 1):
    mid_x = (crossings[i] + crossings[i + 1]) // 2
    if crossings[i] < mid_x < crossings[i + 1]:
      if not is_valid_point(mid_x, rect_max_y, polygon, red_tiles, cache):
        return False

  # Bottom edge (y = rect_min_y)
  crossings = [rect_min_x, rect_max_x]
  for i in range(n):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i + 1) % n]
    if x1 == x2:  # Vertical polygon edge
      if min(y1, y2) <= rect_min_y <= max(y1, y2):
        if rect_min_x < x1 < rect_max_x:
          crossings.append(x1)
  crossings = sorted(set(crossings))
  for i in range(len(crossings) - 1):
    mid_x = (crossings[i] + crossings[i + 1]) // 2
    if crossings[i] < mid_x < crossings[i + 1]:
      if not is_valid_point(mid_x, rect_min_y, polygon, red_tiles, cache):
        return False

  # Left edge (x = rect_min_x): find y-coords where horizontal polygon edges cross
  crossings = [rect_min_y, rect_max_y]
  for i in range(n):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i + 1) % n]
    if y1 == y2:  # Horizontal polygon edge
      if min(x1, x2) <= rect_min_x <= max(x1, x2):
        if rect_min_y < y1 < rect_max_y:
          crossings.append(y1)
  crossings = sorted(set(crossings))
  for i in range(len(crossings) - 1):
    mid_y = (crossings[i] + crossings[i + 1]) // 2
    if crossings[i] < mid_y < crossings[i + 1]:
      if not is_valid_point(rect_min_x, mid_y, polygon, red_tiles, cache):
        return False

  # Right edge (x = rect_max_x)
  crossings = [rect_min_y, rect_max_y]
  for i in range(n):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i + 1) % n]
    if y1 == y2:  # Horizontal polygon edge
      if min(x1, x2) <= rect_max_x <= max(x1, x2):
        if rect_min_y < y1 < rect_max_y:
          crossings.append(y1)
  crossings = sorted(set(crossings))
  for i in range(len(crossings) - 1):
    mid_y = (crossings[i] + crossings[i + 1]) // 2
    if crossings[i] < mid_y < crossings[i + 1]:
      if not is_valid_point(rect_max_x, mid_y, polygon, red_tiles, cache):
        return False

  return True


def solve_part_2(text: str):
  coords = []
  for line in text.strip().splitlines():
    x, y = map(int, line.split(","))
    coords.append((x, y))

  red_tiles = set(coords)
  cache = {}

  # Find the largest rectangle with red corners and only red/green tiles
  max_area = 0

  # Sort pairs by area descending to find the answer faster
  pairs = []
  for i, (x1, y1) in enumerate(coords):
    for j, (x2, y2) in enumerate(coords):
      if i < j:
        area = square_space(x1, y1, x2, y2)
        pairs.append((area, i, j, x1, y1, x2, y2))

  pairs.sort(reverse=True)

  for area, i, j, x1, y1, x2, y2 in pairs:
    # Skip if this area can't beat our current max
    if area <= max_area:
      break  # Since sorted, all remaining will be smaller

    # Check if the rectangle is fully inside the polygon
    rect_min_x, rect_max_x = min(x1, x2), max(x1, x2)
    rect_min_y, rect_max_y = min(y1, y2), max(y1, y2)

    if rectangle_fully_inside_polygon(rect_min_x, rect_min_y, rect_max_x, rect_max_y, coords, red_tiles, cache):
      max_area = area

  return max_area


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
