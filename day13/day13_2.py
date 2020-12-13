from functools import reduce
from math import lcm

deps = "17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,739,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,971,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19"
bus_deps = [(int(x), idx) for idx, x in enumerate(deps.split(",")) if x != "x"]

t0 = bus_deps[0][0]
needle = lcm(*[x[0] for x in bus_deps])
print(needle)
bus_deps = bus_deps[1:]
ts = -1
while ts == -1:
	needle -= t0
	if all([(needle//bd[0]+1)*bd[0] == needle+bd[1] for bd in bus_deps]):
		ts = needle
		break
print(ts)