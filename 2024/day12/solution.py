import time


def get_neighbors(pos, subset=None):
    x, y = pos
    neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    result = set([pos for pos in neighbors])
    return result if subset is None else result.intersection(subset)


def get_area(region) -> int:
    return len(region)


def get_perimeter(region) -> int:
    perimeter = 0
    for pos in region:
        neighbors = get_neighbors(pos)
        perimeter += 4
        perimeter -= len(neighbors.intersection(set(region)))
    return perimeter


def solve_part_1(text: str):
    remaining = set()
    world = {}
    for y, line in enumerate(text.splitlines()):
        for x, char in enumerate(line):
            world[(x, y)] = char
            remaining.add((x, y))

    regions = []
    while len(remaining) > 0:
        start_pos = remaining.pop()
        region = {start_pos}
        current_char = world[start_pos]
        consider = get_neighbors(start_pos, remaining)

        while len(consider) > 0:
            next_consider = consider.pop()
            if world[next_consider] == current_char:
                region.add(next_consider)
                remaining.remove(next_consider)
                consider.update(get_neighbors(next_consider, remaining))

        regions.append(region)

    res = 0
    for r in regions:
        res += get_area(r) * get_perimeter(r)

    return res


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
