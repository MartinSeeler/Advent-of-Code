import time
import re


def solve_part_1(text: str):
    # parse all `mul(44,46)` text segments from text. the numbers may have 1-3 digits.
    # use regex to find all numbers in the text.
    r = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = r.findall(text)
    # multiply all numbers together
    product = 0
    for match in matches:
        product += int(match[0]) * int(match[1])
    return product


def solve_part_2(text: str):
    pass


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
