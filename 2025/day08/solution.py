import time
from pathlib import Path
from math import prod


def euclidian_distance(tuple1: tuple[int, int, int], tuple2: tuple[int, int, int]) -> float:
  return ((tuple1[0] - tuple2[0]) ** 2 + (tuple1[1] - tuple2[1]) ** 2 + (tuple1[2] - tuple2[2]) ** 2) ** 0.5


def solve_part_1(text: str):
  junctions = []
  for line in text.strip().splitlines():
    x, y, z = [int(coord) for coord in line.split(',')]
    junctions.append((x, y, z))
  # calculate distance between all pairs of junctions
  distances = []
  for x in range(len(junctions)):
    for y in range(x + 1, len(junctions)):
      dist = euclidian_distance(junctions[x], junctions[y])
      distances.append((dist, x, y))

  # Sort by distance (shortest first)
  distances.sort()
  def find_parent(i: int) -> int:
    if parents[i] != i:
      parents[i] = find_parent(parents[i])  # path compression
    return parents[i]
  def union(i: int, j: int):
    root_i = find_parent(i)
    root_j = find_parent(j)
    if root_i == root_j:
      return False
    if root_i != root_j:
      # union by size
      if size[root_i] < size[root_j]:
        parents[root_i] = root_j
        size[root_j] += size[root_i]
      else:
        parents[root_j] = root_i
        size[root_i] += size[root_j]
    return True
  # union find
  parents = [i for i in range(len(junctions))] # start with each one as its own parent
  size = [1 for _ in range(len(junctions))] # each group has size 1 in the beginning
  n = len(junctions)

  # Process the first 1000 closest pairs
  for idx, (dist, i, j) in enumerate(distances):
    if idx >= 1000:
      break
    union(i, j)

  # Get the three largest circuit sizes
  circuit_sizes = []
  for i in range(n):
    if find_parent(i) == i:
      circuit_sizes.append(size[i])

  largest_sizes = sorted(circuit_sizes)[-3:]
  return prod(largest_sizes)
  #return prod(size[i] for i in range(len(size)) if parents[i] == i)

  
  



def solve_part_2(text: str):
  junctions = []
  for line in text.strip().splitlines():
    x, y, z = [int(coord) for coord in line.split(',')]
    junctions.append((x, y, z))

  # calculate distance between all pairs of junctions
  distances = []
  for x in range(len(junctions)):
    for y in range(x + 1, len(junctions)):
      dist = euclidian_distance(junctions[x], junctions[y])
      distances.append((dist, x, y))

  # Sort by distance (shortest first)
  distances.sort()

  def find_parent(i: int) -> int:
    if parents[i] != i:
      parents[i] = find_parent(parents[i])  # path compression
    return parents[i]

  def union(i: int, j: int):
    root_i = find_parent(i)
    root_j = find_parent(j)
    if root_i == root_j:
      return False
    if root_i != root_j:
      # union by size
      if size[root_i] < size[root_j]:
        parents[root_i] = root_j
        size[root_j] += size[root_i]
      else:
        parents[root_j] = root_i
        size[root_i] += size[root_j]
    return True

  # union find
  parents = [i for i in range(len(junctions))]
  size = [1 for _ in range(len(junctions))]
  n = len(junctions)

  last_connection = None

  # Keep connecting until everything is in one circuit
  for dist, i, j in distances:
    if union(i, j):  # Only count successful merges
      last_connection = (i, j)
      # Check if we have only 1 circuit left
      num_circuits = sum(1 for idx in range(n) if find_parent(idx) == idx)
      if num_circuits == 1:
        break

  # Multiply the X coordinates of the last connection
  x1 = junctions[last_connection[0]][0]
  x2 = junctions[last_connection[1]][0]

  print(f"Last connection: junctions[{last_connection[0]}] and junctions[{last_connection[1]}]")
  print(f"Coordinates: {junctions[last_connection[0]]} and {junctions[last_connection[1]]}")
  print(f"X coordinates: {x1} and {x2}")

  return x1 * x2


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
