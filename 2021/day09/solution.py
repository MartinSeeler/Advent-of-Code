from collections import deque
from functools import reduce
import time


def has_pos(field: list[list[int]], pos: complex) -> bool:
    return 0 <= pos.real < len(field) and 0 <= pos.imag < len(field[0])


dirs = [0 + 1j, 1 + 0j, 0 - 1j, -1 + 0j]


def adjacents(pos: complex, field: list[list[int]]) -> list[complex]:
    return [pos + d for d in dirs if has_pos(field, pos + d)]


def is_low_point(field: list[list[int]], pos: complex) -> bool:
    cur_value = field[int(pos.real)][int(pos.imag)]
    return all(
        field[int(adj.real)][int(adj.imag)] > cur_value for adj in adjacents(pos, field)
    )


def solve_part_1(text: str):
    res = 0
    field = [list(map(int, line.strip())) for line in text.splitlines()]
    for ix, row in enumerate(field):
        for jx, num in enumerate(row):
            pos = complex(ix, jx)
            if is_low_point(field, pos):
                res += num + 1
    return res


def bfs_basins(grid: list[list[int]], start: complex):
    remaining = deque()
    basin = set()
    basin.add(start)
    remaining.append(start)

    while remaining:
        cur_pos = remaining.popleft()
        cur_val = grid[int(cur_pos.real)][int(cur_pos.imag)]
        for pos in adjacents(cur_pos, grid):
            if pos not in basin:
                adj_val = grid[int(pos.real)][int(pos.imag)]
                # height 9 cannot ever be included.
                if adj_val < 9 and adj_val > cur_val:
                    basin.add(pos)
                    remaining.append(pos)
    return basin


def solve_part_2(text: str):
    basin_lens = []
    field = [list(map(int, line.strip())) for line in text.splitlines()]
    for ix, row in enumerate(field):
        for jx, _ in enumerate(row):
            pos = complex(ix, jx)
            if is_low_point(field, pos):
                basin = bfs_basins(field, pos)
                basin_lens.append(len(basin))
    return reduce(lambda x, y: x * y, sorted(basin_lens, reverse=True)[:3])


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
