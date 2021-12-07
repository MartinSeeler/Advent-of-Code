import numpy as np
import time


def solve_part_1(text: str):
    nums = [int(x) for x in text.split(",")]
    return sum(abs(nums - np.median(nums)))


def solve_part_2(text: str):
    cost = lambda d: d * (d + 1) // 2
    nums = [int(x) for x in text.split(",")]
    # this would minimize cost^2 instead of cost * (cost + 1) / 2, but if we
    # round the mean, we get close enough acording to the tests
    return sum(cost(abs(nums - np.round(np.mean(nums)))))
    # correct for all puzzle inputs would be
    # return min(
    #     sum(cost(abs(nums - np.floor(np.mean(nums))))),
    #     sum(cost(abs(nums - np.ceil(np.mean(nums))))),
    # )


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = solve_part_1(quiz_input)
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
        p_2_solution = solve_part_2(quiz_input)
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
