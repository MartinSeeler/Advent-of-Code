from itertools import combinations

nums = []
with open("./input.txt", "r") as f:
    nums = list([int(x) for x in f.read().splitlines()])

pa_length = 25
invalid_num = -1
for part in [nums[i:i+pa_length+1] for i in range(0,len(nums), 1)]:
    xmas = part[:pa_length]
    target = part[-1]
    res = set()
    for i in combinations(xmas, 2):
        if sum(i) == target:
            res.add(i)
    if len(res) == 0:
        print(target)
        invalid_num = target
        break

for n in range(2,100):
    for part in [nums[i:i+n] for i in range(0,len(nums), 1)]:
        if sum(part) == invalid_num:
            print(min(part)+max(part))
            exit(-1)