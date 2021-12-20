from functools import reduce
import time
import numpy as np
from scipy.ndimage import convolve

to_1s = lambda xs: list(map(lambda p: int(p == "#"), xs))


def solve(text: str, iters: int) -> int:
    enhance_data, _, *img = text.splitlines()

    enhance_data = np.array(to_1s(enhance_data))
    img = np.pad([to_1s(r) for r in img], (50, 50))

    binary = 2 ** np.arange(9).reshape(3, 3)
    return np.sum(
        reduce(
            lambda x, _: enhance_data[convolve(x, binary)],
            range(iters),
            img,
        )
    )


def solve_part_1(text: str):
    return solve(text, 2)


def solve_part_2(text: str):
    return solve(text, 50)


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
