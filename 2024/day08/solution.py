from collections import defaultdict
from itertools import permutations
import time


def parse(text: str):
    board = set()
    antennas = defaultdict(set)
    for y, line in enumerate(text.strip().splitlines()):
        for x, c in enumerate(line.strip()):
            p = (x, y)
            board.add(p)
            if c != ".":
                antennas[c].add(p)
    return board, antennas


def solve_part_1(text: str):
    board, antennas = parse(text)
    antinode_locs = set()

    for _, locs in antennas.items():
        for x, y in permutations(locs, 2):
            antinode = (y[0] + (y[0] - x[0]), y[1] + (y[1] - x[1]))
            antinode_locs.add(antinode)

    return len(antinode_locs & board)


def solve_part_2(text: str):
    board, antennas = parse(text)
    antinode_locs = set()
    map_w = len(text.splitlines()[0])
    for _, locs in antennas.items():
        for x, y in permutations(locs, 2):
            for i in range(map_w):
                antinode = (y[0] + (y[0] - x[0]) * i, y[1] + (y[1] - x[1]) * i)
                antinode_locs.add(antinode)
    return len(antinode_locs & board)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = int(solve_part_1(quiz_input))
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
        p_2_solution = int(solve_part_2(quiz_input))
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
