from collections import Counter, defaultdict
import time


def parse_mapping(text: str):
    paths = defaultdict(list)
    for line in text.splitlines():
        [f, t] = line.split("-")
        paths[f].append(t)
        paths[t].append(f)
    return paths


def is_valid_move(x: str, current: list[str]):
    return (x.islower() and x not in current) or x.isupper()


def is_valid_move_2(x: str, current: list[str]):
    if x.isupper():
        return True
    else:
        if x not in current:
            return True
        if x in ["start", "end"]:
            return False
        c = Counter(filter(lambda x: x.islower(), current))
        if any(map(lambda x: x > 1, c.values())):
            return False
    return True


def find_all_paths(paths: defaultdict, current_path: list[str], condition) -> int:
    if len(current_path) == 0:
        return sum(
            find_all_paths(paths, ["start", x], condition) for x in paths["start"]
        )
    elif current_path[-1] == "end":
        return 1
    else:
        return sum(
            find_all_paths(paths, current_path + [x], condition)
            for x in paths[current_path[-1]]
            if condition(x, current_path)
        )


def solve_part_1(text: str):
    mapping = parse_mapping(text)
    return find_all_paths(mapping, [], is_valid_move)


def solve_part_2(text: str):
    mapping = parse_mapping(text)
    return find_all_paths(mapping, [], is_valid_move_2)


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
