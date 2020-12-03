from operator import mul
from functools import reduce

input_list = []
with open("./input.txt", "r") as f:
    input_list = f.read().splitlines()


def get_trees(x_step, y_step):
    x = 0
    y = 0
    trees = 0
    while y < len(input_list):
        trees += 1 if input_list[y][x] == "#" else 0
        x = (x+x_step) % len(input_list[0])
        y += y_step
    return trees


slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
print("Final", reduce(mul, [get_trees(*params) for params in slopes]))