total = 0
with open("./input.txt", "r") as f:
    for input_group in f.read().split("\n\n"):
        total += len(set("".join(input_group.split("\n"))))
print(total)