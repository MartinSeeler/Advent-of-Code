import time


def calculate_trailhead_score(x, y, map):
    visit_next = [(x, y, 1)]
    visited = set()
    nines = set()
    while visit_next:
        x, y, exp_value = visit_next.pop()
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                (nx, ny) not in visited
                and (nx, ny) in map
                and map[(nx, ny)] == exp_value
            ):
                if (exp_value) == 9:
                    nines.add((nx, ny))
                else:
                    visit_next.append((nx, ny, exp_value + 1))
    return len(nines)


def solve_part_1(text: str):
    trail_heads = set()
    map = {}
    for y, line in enumerate(text.splitlines()):
        for x, char in enumerate(line):
            if char == "0":
                trail_heads.add((x, y))
            if char.isdigit():
                map[(x, y)] = int(char)
    return sum(calculate_trailhead_score(x, y, map) for x, y in trail_heads)


def calculate_trailhead_rating(x, y, map, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Mark the current cell as visited
    visited.add((x, y))
    new_path = path + [(x, y)]

    if map[(x, y)] == 9:
        return [new_path]  # Return the current path as a valid path

    paths_to_nine = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (
            (nx, ny) not in visited
            and (nx, ny) in map
            and map[(nx, ny)] == map[(x, y)] + 1
        ):
            paths_to_nine.extend(
                calculate_trailhead_rating(nx, ny, map, visited.copy(), new_path)
            )

    return paths_to_nine


def solve_part_2(text: str):
    trail_heads = set()
    map = {}
    for y, line in enumerate(text.splitlines()):
        for x, char in enumerate(line):
            if char == "0":
                trail_heads.add((x, y))
            if char.isdigit():
                map[(x, y)] = int(char)
    return sum(len(calculate_trailhead_rating(x, y, map)) for x, y in trail_heads)


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
