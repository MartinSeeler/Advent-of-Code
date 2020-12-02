from itertools import combinations

input_list = []
with open("./day01-input.txt", "r") as f:
    lines = f.read().splitlines()
    input_list = [int(x) for x in lines]

def find_solutions(inputs, target_sum, N = 2):
    for xs in combinations(inputs, N):
        if sum(xs) == target_sum:
            yield xs

solution_part_1 = next(find_solutions(input_list, 2020, 2))
print(f"Solution Part 1: {solution_part_1} => {solution_part_1[0]*solution_part_1[1]}")

solution_part_2 = next(find_solutions(input_list, 2020, 3))
print(f"Solution Part 2: {solution_part_2} => {solution_part_2[0]*solution_part_2[1]*solution_part_2[2]}}")
