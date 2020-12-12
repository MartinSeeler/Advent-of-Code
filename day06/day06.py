from functools import reduce as r
from operator import or_, and_

with open("./input.txt", "r") as f:
    xs = [x.split("\n") for x in "".join(f.read()).split("\n\n")]
    solve = lambda fn: sum(len(r(fn, map(set, x))) for x in xs)
    print("Part 1:", solve(or_))
    print("Part 2:", solve(and_))