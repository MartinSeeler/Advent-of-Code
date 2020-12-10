adapters = []
with open("./input.txt", "r") as f:
    adapters = sorted(list([int(x) for x in f.read().splitlines()]))

print(adapters)
highest = max(adapters)+3

def solve(target, xs, ones, twos, threes):
    if len(xs) <= 0:
        return (ones, twos, threes)
    head, *tail = xs
    print(target, head, tail, ones, twos, threes)
    if target+1 == head:
        return solve(head ,tail, ones+1, twos, threes)
    elif target+2 == head:
        return solve(head ,tail, ones, twos+1, threes)
    elif target+3 == head:
        return solve(head ,tail, ones, twos, threes+1)
    else:
        return None

(ones, twos, threes) = solve(0, [*adapters, highest], 0, 0, 0)
print(ones, twos, threes)
print(ones*threes)


