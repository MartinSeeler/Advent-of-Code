import re

rules_list = []
with open("./input.txt", "r") as f:
    rules_list = f.read().splitlines()

paths = dict()
all_colors = []

for rule in rules_list:
    [head, tail] = rule.split(" contain ")
    match_head = re.match(r"^(\w+\s\w+)\sbag[s]?.*", head, re.I)
    c = match_head.groups()[0]
    all_colors.append(c)
    if match_head:
        match_tail = re.findall(r"(\d)\s(\w+\s\w+)\sbag[s]?", tail, re.I)
        if match_tail:
            paths[c] = match_tail
print(paths)
target_color = "shiny gold"

def path_exists(current_color, target_color):
    if current_color in paths:
        res = False
        for xs in paths[current_color]:
            if xs[1] == target_color:
                return True
            print("checking", xs, "for", current_color)
            res = res or path_exists(xs[1], target_color)
        return res
    else:
        return False

# solution part 1
#final = 0
#for c in all_colors:
#    if c != target_color:
#        final += path_exists(c, target_color)

def calc(current_color):
    if current_color in paths:
        return sum(map(lambda x: int(x[0]) + (int(x[0]) * calc(x[1])), paths[current_color]))
    else:
        return 0

final = calc(target_color)
print(final)