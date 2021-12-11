import time
import numpy as np


def get_inc_mask(s, x, y):
    mask = np.zeros(s, dtype=np.int8)
    mask[
        np.max([x - 1, 0]) : np.min([x + 2, mask.shape[0]]),
        np.max([y - 1, 0]) : np.min([y + 2, mask.shape[1]]),
    ] = 1
    mask[x, y] = 0
    return mask


def play_field(field):
    field += 1
    all_flashes = np.zeros(field.shape, dtype=bool)
    while np.any(flashes := (field > 9) & ~all_flashes):
        inc_mask = np.zeros(field.shape, dtype=np.int8)
        for flash in np.argwhere(flashes):
            inc_mask += get_inc_mask(field.shape, flash[0], flash[1])
        field += inc_mask
        all_flashes[flashes] = True
    field[all_flashes] = 0
    return field, np.sum(all_flashes)


def solve_part_1(text: str):
    field = np.array(
        [list(map(int, line)) for line in text.splitlines()], dtype=np.int8
    )
    total_flashes = 0
    for _ in range(0, 100):
        field, flashes = play_field(field)
        total_flashes += flashes
    return total_flashes


def solve_part_2(text: str):
    field = np.array(
        [list(map(int, line)) for line in text.splitlines()], dtype=np.int8
    )
    for r in range(1, 1000):
        field, _ = play_field(field)
        if np.all(field == 0):
            return r
    return -1


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
