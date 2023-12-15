from collections import defaultdict
import time
from functools import reduce


def hash(text: str):
    return reduce(lambda res, c: (res + ord(c)) * 17 % 256, text, 0)


def solve_part_1(text: str):
    return sum(hash(block) for block in text.split(","))


def solve_part_2(text: str):
    instructs = text.split(",")
    boxes = defaultdict(dict)
    for inst in instructs:
        if "-" in inst:
            label = inst[:-1]
            boxes[hash(label)].pop(label, None)
        else:
            label, i = inst.split("=")
            boxes[hash(label)][label] = int(i)
    return sum(
        (i + 1) * (j + 1) * l for i in boxes for j, l in enumerate(boxes[i].values())
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
