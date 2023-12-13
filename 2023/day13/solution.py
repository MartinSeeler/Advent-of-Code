import time


def find_reflecting_rows(block: str, target_offset=0):
    lines = block.splitlines()
    tl = len(lines)
    idx = 0
    while idx < tl:
        idx += 1
        rhs = lines[tl - idx :]
        lhs = lines[: tl - idx]
        min_len = min(len(lhs), len(rhs))
        rhs = rhs[:min_len]
        lhs = lhs[::-1][:min_len]
        rhs_str = "\n".join(rhs)
        lhs_str = "\n".join(lhs)
        matching_chars = [
            1 if rhs_str[i] == lhs_str[i] else 0 for i in range(len(rhs_str))
        ]
        if sum(matching_chars) == (len(rhs_str) - target_offset):
            return tl - idx
    return 0


def rotate_str(block: str):
    return "\n".join(["".join(row) for row in zip(*block.splitlines()[::-1])])


def solve_part_1(text: str):
    return sum(
        (find_reflecting_rows(block) * 100) + find_reflecting_rows(rotate_str(block))
        for block in text.split("\n\n")
    )


def solve_part_2(text: str):
    return sum(
        (find_reflecting_rows(block, 1) * 100)
        + find_reflecting_rows(rotate_str(block), 1)
        for block in text.split("\n\n")
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
