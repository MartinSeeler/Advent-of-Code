from functools import reduce as r
from operator import or_, and_

with open("input.txt", "r") as f:
    xs = [x.split("\n") for x in f.read().split("\n"*2)]
    s = lambda fn: sum(len(r(fn, map(set, x))) for x in xs)
    print("Part 1:", s(or_))
    print("Part 2:", s(and_))