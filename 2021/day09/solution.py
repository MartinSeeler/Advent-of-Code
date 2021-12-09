from collections import deque
from functools import reduce
import time


def has_pos(field: list[list[int]], pos: complex):
    """checks if the complex number is in between the bounds of the 2d field array"""
    if pos.real < 0 or pos.real >= len(field):
        return False
    if pos.imag < 0 or pos.imag >= len(field[0]):
        return False
    return True


dirs = [0 + 1j, 1 + 0j, 0 - 1j, -1 + 0j]


def is_low_point(field: list[list[int]], pos: complex):
    """checks if all values in field around the current pos are either non existing or lower than the current value at pos"""
    cur_value = field[int(pos.real)][int(pos.imag)]
    for d in dirs:
        moved = pos + d
        if not has_pos(field, moved):
            continue
        f_value = field[int(moved.real)][int(moved.imag)]
        if f_value <= cur_value:
            return False
    return True


def solve_part_1(text: str):
    res = 0
    field = [list(map(int, line.strip())) for line in text.splitlines()]
    for ix, row in enumerate(field):
        for jx, num in enumerate(row):
            pos = complex(ix, jx)
            if is_low_point(field, pos):
                res += num + 1
    return res


def rec_find_basin(field: list[list[int]], rem: set[complex], basin: set[complex]):
    """recursively finds the lowest value in the basin of the current pos"""
    if len(rem) == 0:
        return basin
    pos = rem[0]
    if not has_pos(field, pos):
        return rec_find_basin(field, rem[1:], basin)
    cur_value = field[int(pos.real)][int(pos.imag)]
    new_basin_pos = []
    for d in dirs:
        moved = pos + d
        if not has_pos(field, moved):
            continue

        f_value = field[int(moved.real)][int(moved.imag)]
        if f_value > cur_value and f_value < 9 and moved not in basin:
            new_basin_pos.append(moved)
    return rec_find_basin(field, rem[1:] + new_basin_pos, basin + new_basin_pos)


def solve_part_2(text: str):
    basins = []
    field = [list(map(int, line.strip())) for line in text.splitlines()]
    for ix, row in enumerate(field):
        for jx, num in enumerate(row):
            pos = complex(ix, jx)
            if is_low_point(field, pos):
                basin = set(rec_find_basin(field, [pos], [pos]))
                print(basin, pos, len(basin))
                basins.append(len(basin))
    # return the 3 largest values in basins
    largest = sorted(basins, reverse=True)[:3]
    # return the multply of largest
    return reduce(lambda x, y: x * y, largest)


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
