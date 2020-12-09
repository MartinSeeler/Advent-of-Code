from itertools import combinations as cs

pa_length = 25
with open("./input.txt", "r") as f:
    nums = list([int(x) for x in f.read().splitlines()])
    for part in [nums[i:i+pa_length+1] for i in range(0,len(nums), 1)]:
        xmas = part[:pa_length]
        target = part[-1]
        combis = set()
        for i in cs(xmas, 2):
            if sum(i) == target:
                combis.add(i)
        if len(combis) == 0:
            print("Part1", target)
            for n in range(2,len(nums)-1):
                for xs in [nums[i:i+n] for i in range(0,len(nums), 1)]:
                    if sum(xs) == target:
                        print("Part2", min(xs)+max(xs))
                        exit(-1)

