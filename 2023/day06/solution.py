from math import sqrt, ceil, floor
import re
import time


def parse_input(text, merge=False):
    t, r = [
        re.findall(
            r"\d+", l.split(":")[1].replace(" ", "") if merge else l.split(":")[1]
        )
        for l in text.splitlines()
    ]
    return zip(map(int, t), map(int, r))


def solve(text, merge=False):
    res = 1
    for T, rec in parse_input(text, merge):
        sqrt_discriminant = sqrt(T**2 - 4 * rec)
        t1 = max(0, ceil((T - sqrt_discriminant) / 2))
        t1 += t1 * (T - t1) <= rec
        t2 = min(T, floor((T + sqrt_discriminant) / 2))
        t2 -= t2 * (T - t2) <= rec
        solutions = max(0, t2 + 1 - t1)
        res *= solutions
    return res


def solve_part_1(text: str):
    return solve(text, False)


def solve_part_2(text: str):
    return solve(text, True)


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
