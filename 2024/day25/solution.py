import time


def parse(lines) -> set[tuple[int, int]]:
    return {
        (x, y)
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
        if char == "#"
    }


def solve_part_1(text: str):
    blocks = text.split("\n\n")
    locks = []
    keys = []
    for b in blocks:
        lines = b.splitlines()
        schema = parse(lines[1:-1])
        locks.append(schema) if lines[0] == "#####" else keys.append(schema)

    r = 0
    for lock in locks:
        for key in keys:
            r += len(lock & key) == 0
    return r


def solve_part_2(text: str):
    return 0


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
