import itertools
import math
from functools import reduce
import time


def add_value(x, n, left=True):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_value(x[0], n), x[1]] if left else [x[0], add_value(x[1], n, False)]


def explode(x, depth=4):
    if isinstance(x, int):
        return False, None, x, None
    if depth == 0:
        return True, x[0], 0, x[1]
    left, right = x
    did_explode, left_value, left, right_value = explode(left, depth - 1)
    if did_explode:
        return True, left_value, [left, add_value(right, right_value)], None
    did_explode, left_value, right, right_value = explode(right, depth - 1)
    if did_explode:
        return True, None, [add_value(left, left_value, False), right], right_value
    return False, None, x, None


def split(x):
    if isinstance(x, int):
        return (True, [x // 2, math.ceil(x / 2)]) if x >= 10 else (False, x)
    left, right = x
    did_change, left = split(left)
    if did_change:
        return True, [left, right]
    did_change, right = split(right)
    return did_change, [left, right]


def add(x, y):
    res = [x, y]
    while True:
        did_change, _, res, _ = explode(res)
        if did_change:
            continue
        did_change, res = split(res)
        if not did_change:
            break
    return res


def magnitude(x):
    return x if isinstance(x, int) else 3 * magnitude(x[0]) + 2 * magnitude(x[1])


def solve_part_1(text: str):
    return magnitude(reduce(add, list(map(eval, text.splitlines()))))


def solve_part_2(text: str):
    return max(
        magnitude(add(x, y))
        for x, y in itertools.permutations(list(map(eval, text.splitlines())), 2)
    )


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
