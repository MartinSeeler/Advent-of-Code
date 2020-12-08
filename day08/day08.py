instruction_list = []
with open("./input.txt", "r") as f:
    instruction_list = f.read().splitlines()

idx = 0
acc = 0
visited_idx = set()

while idx not in visited_idx:
    print(idx)
    visited_idx.add(idx)
    if instruction_list[idx].startswith("nop"):
        idx += 1
    elif instruction_list[idx].startswith("acc"):
        acc += int(instruction_list[idx].split(" ")[1])
        idx += 1
    else:
        idx += int(instruction_list[idx].split(" ")[1])
    

print(acc)
