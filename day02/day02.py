import re
from functools import reduce

input_list = []
with open("./input.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        input_list.append(line.split(" "))

def is_entry_valid(range, pattern, text):
    [range_min, range_max] = [int(x) for x in range.split("-")]
    p = re.compile(pattern[:-1])
    matches = re.findall(p, text)
    return len(matches) >= range_min and len(matches) <= range_max


valid_results = reduce(lambda sum, entry: sum + 1 if is_entry_valid(*entry) else sum, input_list, 0)
print(f"Valids: {valid_results}")
