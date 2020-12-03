import re
from functools import reduce

input_list = []
with open("./input.txt", "r") as f:
    input_list = f.read().splitlines()
    

x = 0
y = 0
trees = 0
while y < len(input_list):
    print(x, y, trees)
    trees += 1 if input_list[y][x] == "#" else 0
    x = (x+3) % len(input_list[0])
    y += 1

print("Final", x, y, trees)