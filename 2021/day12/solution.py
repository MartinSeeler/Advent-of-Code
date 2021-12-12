from collections import Counter, defaultdict
import time


def parse_mapping(text: str):
    paths = defaultdict(set)
    for line in text.splitlines():
        [f, t] = line.split("-")
        paths[f].add(t)
        paths[t].add(f)
    return paths


def find_all_paths(
    mappings: defaultdict, x: str, current_path: set, double_allowed: bool
) -> int:
    if x == "end":
        return 1
    paths = 0
    for b in mappings[x]:
        if b not in current_path:
            tmp = {b} if b == b.lower() else set()
            paths += find_all_paths(mappings, b, current_path | tmp, double_allowed)
        elif double_allowed and b != "start":
            paths += find_all_paths(mappings, b, current_path, False)
    return paths


def solve_part_1(text: str):
    mapping = parse_mapping(text)
    return find_all_paths(mapping, "start", {"start"}, False)


def solve_part_2(text: str):
    mapping = parse_mapping(text)
    return find_all_paths(mapping, "start", {"start"}, True)


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
