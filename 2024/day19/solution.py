import time


def is_possible(design, patterns) -> bool:
    matching_starts = [p for p in patterns if design.startswith(p)]
    completed = any(design == ms for ms in matching_starts)
    if completed:
        return True
    else:
        return any(is_possible(design[len(ms) :], patterns) for ms in matching_starts)


def solve_part_1(text: str):
    lines = text.splitlines()
    patterns = lines[0].strip().split(", ")

    return sum(is_possible(design, patterns) for design in lines[2:])


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
