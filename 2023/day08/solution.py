import time
from math import lcm


def parse_input(text):
    parts = text.split("\n\n")
    path = parts[0]
    rules = parts[1].split("\n")
    map = {}
    for rule in rules:
        node = rule[:3]
        f, t = rule[7:10], rule[12:15]
        map[node] = (f, t)
    return path, map


def solve_part_1(text: str):
    path, map = parse_input(text)
    current = "AAA"
    target = "ZZZ"
    steps = 0
    p_idx = 0
    while current != target:
        steps += 1
        if path[p_idx] == "R":
            current = map[current][1]
        else:
            current = map[current][0]
        p_idx += 1
        if p_idx == len(path):
            p_idx = 0
    return steps


def find_cycle_length(map, path, start_node):
    current = start_node
    steps = 0
    p_idx = 0
    while True:
        steps += 1
        direction = path[p_idx % len(path)]
        current = map[current][0] if direction == "L" else map[current][1]
        p_idx += 1
        if current[2] == "Z":
            return steps


def solve_part_2(text: str):
    path, map = parse_input(text)
    start_nodes = [k for k in map.keys() if k[2] == "A"]
    cycle_lengths = [find_cycle_length(map, path, node) for node in start_nodes]
    overall_cycle = lcm(*cycle_lengths)
    return overall_cycle


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = int(solve_part_1(quiz_input))
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.2f}ms)")
        p_2_solution = int(solve_part_2(quiz_input))
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.2f}ms)")
