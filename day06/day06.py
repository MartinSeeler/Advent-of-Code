import string
from functools import reduce

total = 0
with open("./input.txt", "r") as f:
    print(sum([sum(map(len, reduce(
            set.intersection, 
            map(set, xs.split("\n")), 
            set(string.ascii_lowercase)
        ))) for xs in f.read().split("\n\n")]))