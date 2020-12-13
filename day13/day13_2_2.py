from itertools import count
from math import lcm

with open("./input.txt", "r") as f:
  buses = [(idx, int(x)) for idx, x in enumerate(f.read().splitlines()[1].split(",")) if x != "x"]
  t, step = buses[0]
  for delta, period in buses[1:]:
    for t in count(t, step):
      if (t + delta) % period == 0:
        break
    step = lcm(step, period)
print(t)
