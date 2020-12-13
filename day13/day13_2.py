from functools import reduce
from math import lcm, prod

def solve(inp):
	bus_deps = [(int(x), idx) for idx, x in enumerate(inp.split(",")) if x != "x"]
	# Extended Euclidean algorithm
	# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
	invm = lambda a, b: 0 if a==0 else 1 if b%a==0 else b - invm(b%a,a)*b//a
	# chinese remainder theorems
	# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
	N = prod([bs[0] for bs in bus_deps])
	x = sum([bs[1]*(N//bs[0])*invm(N//bs[0], bs[0]) for bs in bus_deps])
	return N - x % N

with open("./input.txt", "r") as f:
	print(solve(f.read().splitlines()[1]))
