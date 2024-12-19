from memoization import cached
import time


@cached
def calc_possible_arrangements(design: str, patterns: set[str]) -> bool:
    if design == "":
        return 0
    matching_starts = [p for p in patterns if design.startswith(p)]
    completed = sum(design == ms for ms in matching_starts)
    return completed + sum(
        calc_possible_arrangements(design[len(ms) :], patterns)
        for ms in matching_starts
    )


def solve_part_1(text: str):
    lines = text.splitlines()
    patterns = set(lines[0].strip().split(", "))
    return sum(calc_possible_arrangements(design, patterns) > 0 for design in lines[2:])


def solve_part_2(text: str):
    lines = text.splitlines()
    patterns = set(lines[0].strip().split(", "))
    return sum(calc_possible_arrangements(design, patterns) for design in lines[2:])


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
