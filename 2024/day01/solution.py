import time
from collections import Counter


def parse_input(text: str):
    lines = text.strip().split("\n")
    pairs = [tuple(map(int, line.split())) for line in lines]
    return zip(*pairs)


def solve_part_1(text: str) -> int:
    xs, ys = parse_input(text)
    sorted_xs, sorted_ys = sorted(xs), sorted(ys)
    return sum(abs(x - y) for x, y in zip(sorted_xs, sorted_ys))


def solve_part_2(text: str) -> int:
    xs, ys = parse_input(text)
    counter_ys = Counter(ys)
    return sum(x * counter_ys[x] for x in xs)


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
