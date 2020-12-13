adapters = []
with open("input.txt", "r") as f:
    adapters = sorted(list([int(x) for x in f.read().splitlines()]))

highest = max(adapters)+3

def solve1(target, xs, ones, twos, threes):
    if len(xs) <= 0:
        return (ones, twos, threes)
    head, *tail = xs
    print(target, head, tail, ones, twos, threes)
    if target+1 == head:
        return solve1(head ,tail, ones+1, twos, threes)
    elif target+2 == head:
        return solve1(head ,tail, ones, twos+1, threes)
    elif target+3 == head:
        return solve1(head ,tail, ones, twos, threes+1)
    else:
        return None

#(ones, twos, threes) = solve1(0, [*adapters, highest], 0, 0, 0)
#print(ones, twos, threes)
#print(ones*threes)

def solve2(xs):
    step_counter = {0: 1}
    for j in xs:
        step_counter[j] = 0
        step_counter[j] += step_counter[j - 1] if j - 1 in step_counter else 0
        step_counter[j] += step_counter[j - 2] if j - 2 in step_counter else 0
        step_counter[j] += step_counter[j - 3] if j - 3 in step_counter else 0
    return step_counter[xs[-1]]
        

print(solve2([*adapters, highest]))


