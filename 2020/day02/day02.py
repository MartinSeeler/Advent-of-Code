import re
from functools import reduce

input_list = []
with open("input.txt", "r") as f:
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

def is_entry_valid_part2(range, pattern, text):
    [first_idx, second_idx] = [int(x) for x in range.split("-")]
    p = re.compile(pattern[:-1])
    matches_first_idx = matches_second_idx = False
    for m in re.finditer(p, text):
        match_idx = m.start() + 1
        if match_idx == first_idx:
            matches_first_idx = True
        elif match_idx == second_idx:
            matches_second_idx = True
    return (matches_first_idx or matches_second_idx) and not (matches_first_idx and matches_second_idx)

valid_results_2 = reduce(lambda sum, entry: sum + 1 if is_entry_valid_part2(*entry) else sum, input_list, 0)
print(f"Valids Part Two: {valid_results_2}")