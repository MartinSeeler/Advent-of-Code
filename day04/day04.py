from operator import mul
from functools import reduce

input_list = []
with open("./input.txt", "r") as f:
    input_list = f.read().splitlines()

field_necessary = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

valids = 0
current_input = ""
for ldx, line in enumerate(input_list):
    if line == "" or ldx == len(input_list) - 1:
        keys = set([x.split(":")[0] for x in current_input.strip().split(" ")])
        valids += field_necessary.issubset(keys)
        current_input = ""
    else:
        current_input += f" {line}"
print(valids)
