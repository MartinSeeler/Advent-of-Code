FLOOR, EMPTY_SEAT, OCCUPIED_SEAT = range(3)

grid = []
with open("input.txt", "r") as f:
  lines = f.read().splitlines()
  for line in lines:
    grid.append(list([[".", "L", "#"].index(x) for x in line]))

print(grid)

def get_adj_step(x, y, x_mod, y_mod, grid):
  if x + x_mod >= 0 and x + x_mod <= len(grid[0])-1 and y+y_mod >= 0 and y+y_mod <= len(grid)-1:
    if grid[y+y_mod][x+x_mod] == FLOOR:
      return get_adj_step(x+x_mod, y+y_mod, x_mod, y_mod, grid)
    else:
      return grid[y+y_mod][x+x_mod]
  else:
    return FLOOR


def get_adjacent(x, y, grid):
  seats = []
  seats.append(get_adj_step(x, y, -1, 0, grid)) # left
  seats.append(get_adj_step(x, y, +1, 0, grid)) # right
  seats.append(get_adj_step(x, y, 0, -1, grid)) # top
  seats.append(get_adj_step(x, y, 0, 1, grid)) # bottom
  seats.append(get_adj_step(x, y, -1, -1, grid)) # tl
  seats.append(get_adj_step(x, y, 1, -1, grid)) # tr
  seats.append(get_adj_step(x, y, -1, 1, grid)) # bl
  seats.append(get_adj_step(x, y, 1, 1, grid)) # br
  return seats


def update(x,y, grid):
  if grid[y][x] == FLOOR:
    return FLOOR
  elif grid[y][x] == EMPTY_SEAT and all([a == EMPTY_SEAT or a == FLOOR for a in get_adjacent(x, y, grid)]):
    return OCCUPIED_SEAT
  elif grid[y][x] == OCCUPIED_SEAT and sum([1 for a in get_adjacent(x, y, grid) if a == OCCUPIED_SEAT]) >= 5:
    return EMPTY_SEAT
  else:
    return grid[y][x]

def process_grid(grid):
  next_grid = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
  for x in range(len(grid[0])):
    for y in range(len(grid)):
      next_grid[y][x] = update(x, y, grid)
  return next_grid

def concat(grid):
  return "\n".join(["".join([[".", "L", "#"][x] for x in xs]) for xs in grid])
  

while True:
  #print(f"Next for\n{concat(grid)}\n\n")
  next_grid = process_grid(grid)
  if next_grid == grid:
    print(next_grid)
    print(sum([sum([1 for x in xs if x == OCCUPIED_SEAT]) for xs in next_grid]))
    exit()
  grid = next_grid



