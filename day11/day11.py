FLOOR, EMPTY_SEAT, OCCUPIED_SEAT = range(3)

grid = []
with open("./input.txt", "r") as f:
  lines = f.read().splitlines()
  for line in lines:
    grid.append(list([[".", "L", "#"].index(x) for x in line]))

print(grid)

def get_adjacent(x, y, grid):
  seats = []
  if x > 0:
    seats.append(grid[y][x-1]) # left
  if x < len(grid[0])-1:
    seats.append(grid[y][x+1]) # right
  if y > 0:
    seats.append(grid[y-1][x]) # top
  if y < len(grid)-1:
    seats.append(grid[y+1][x]) # bottom
  if x > 0 and y > 0:
    seats.append(grid[y-1][x-1]) # tl
  if x < len(grid[0])-1 and y > 0:
    seats.append(grid[y-1][x+1]) # tr
  if x > 0 and y < len(grid)-1:
    seats.append(grid[y+1][x-1]) # bl
  if x < len(grid[0])-1 and y < len(grid)-1:
    seats.append(grid[y+1][x+1]) # br
  return seats


def update(x,y, grid):
  if grid[y][x] == FLOOR:
    return FLOOR
  elif grid[y][x] == EMPTY_SEAT and all([a == EMPTY_SEAT or a == FLOOR for a in get_adjacent(x, y, grid)]):
    return OCCUPIED_SEAT
  elif grid[y][x] == OCCUPIED_SEAT and sum([1 for a in get_adjacent(x, y, grid) if a == OCCUPIED_SEAT]) >= 4:
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



