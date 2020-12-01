from itertools import combinations

input_list = []
with open("./day01-input.txt", "r") as f:
    lines = f.read().splitlines()
    input_list = [int(x) for x in lines]

def find_solutions(inputs, target_sum, N = 2):
    for xs in combinations(inputs, 2):
        if sum(xs) == target_sum:
            yield xs

solution = next(find_solutions(input_list, 2020, 2))
print(f"Solution: {solution} => {solution[0]*solution[1]}")
