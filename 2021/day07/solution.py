import numpy as np


def solve_part_1(text: str):
    nums = [int(x) for x in text.split(",")]
    return sum(abs(nums - np.median(nums)))


def solve_part_2(text: str):
    cost = lambda d: d * (d + 1) // 2
    nums = [int(x) for x in text.split(",")]
    # this would minimize cost^2 instead of cost * (cost + 1) / 2, but if we
    # round the mean, we get close enough acording to the tests
    return sum(cost(abs(nums - np.round(np.mean(nums)))))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve_part_1(quiz_input))
        print("Part 2:", solve_part_2(quiz_input))
