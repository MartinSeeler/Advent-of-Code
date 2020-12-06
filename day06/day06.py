import string
from functools import reduce

total = 0
with open("./input.txt", "r") as f:
    for input_group in f.read().split("\n\n"):
        total += sum(map(len, reduce(
            set.intersection, 
            map(set, input_group.split("\n")), 
            set(string.ascii_lowercase)
        )))
print(total)