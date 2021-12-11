import time
from typing import Tuple


def parse_map(text: str) -> list[list[int]]:
    return [list(map(int, line.strip())) for line in text.splitlines()]


def increase_all(map: list[list[int]]) -> list[list[int]]:
    for x in range(0, len(map)):
        for y in range(0, len(map[x])):
            map[x][y] += 1
    return map


def find_9s(map: list[list[int]]):
    return [
        (x, y)
        for x in range(0, len(map))
        for y in range(0, len(map[x]))
        if map[x][y] > 9
    ]


def increase_around(map: list[list[int]], x: int, y: int) -> list[list[int]]:
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (
                i >= 0
                and i < len(map)
                and j >= 0
                and j < len(map[i])
                and (i, j) != (x, y)
            ):
                map[i][j] += 1
    return map


def play_part_1(map: list[list[int]]) -> Tuple[list[list[int]], int]:
    map = increase_all(map)
    flashing = set()
    while len(not_increased_yet := set(find_9s(map)) - set(flashing)) > 0:
        for x, y in not_increased_yet:
            map = increase_around(map, x, y)
        flashing = flashing.union(not_increased_yet)
    for x, y in flashing:
        map[x][y] = 0
    return map, len(flashing)


def solve_part_1(text: str):
    map = parse_map(text)
    total = 0
    for _ in range(0, 100):
        map, flashes = play_part_1(map)
        total += flashes
    return total


def solve_part_2(text: str):
    map = parse_map(text)
    total_elements_in_map = len(map) * len(map[0])
    round = 0
    while True:
        round += 1
        map, flashes = play_part_1(map)
        if flashes == total_elements_in_map:
            return round


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
