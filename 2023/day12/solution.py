from functools import cache
import time


def test_conditions_2(conditions: str, counts: list[int]):
    @cache
    def dp(p, n, r=0):
        if p >= len(conditions):
            return n == len(counts)

        if conditions[p] in ".?":
            r += dp(p + 1, n)

        if (
            conditions[p] in "#?"
            and n < len(counts)
            and (
                p + counts[n] <= len(conditions)
                and "." not in conditions[p : p + counts[n]]
            )
            and (
                p + counts[n] == len(conditions) or "#" not in conditions[p + counts[n]]
            )
        ):
            r += dp(p + counts[n] + 1, n + 1)

        return r

    return dp(0, 0)


def solve_part_1(text: str):
    res = 0
    for row in text.splitlines():
        conditions, counts = row.split(" ")
        counts = [int(c) for c in counts.split(",")]
        # print("new", conditions, counts)
        res += test_conditions_2(conditions, counts)
    return res


def solve_part_2(text: str):
    res = 0
    for row in text.splitlines():
        conditions, counts = row.split(" ")
        counts = [int(c) for c in counts.split(",")] * 5
        res += test_conditions_2("?".join([conditions] * 5), counts)
    return res


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
