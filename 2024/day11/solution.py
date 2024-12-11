import functools
import time


@functools.lru_cache(None)
def solve(x, t):
    if t == 0:
        return 1
    elif x == 0:
        return solve(1, t - 1)
    elif len(str(x)) % 2 == 0:
        x_str = str(x)
        l = x_str[: len(x_str) // 2]
        r = x_str[len(x_str) // 2 :]
        l, r = (int(l), int(r))
        return solve(l, t - 1) + solve(r, t - 1)
    else:
        return solve(x * 2024, t - 1)


def solve_part_1(text: str):
    return sum(solve(x, 25) for x in [int(x) for x in text.strip().split(" ")])


def solve_part_2(text: str):
    return sum(solve(x, 75) for x in [int(x) for x in text.strip().split(" ")])


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
