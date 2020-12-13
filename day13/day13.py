from functools import reduce
from math import prod

with open("./input.txt", "r") as f:
  lines = f.read().splitlines()
  ts_0 = int(lines[0])
  bus_ids = [int(x) for x in lines[1].split(",") if x != "x"]
  print(prod(reduce(lambda x, y: x if x[0] < y[0] else y, [((ts_0//x + 1)*x-ts_0, x) for x in bus_ids])))