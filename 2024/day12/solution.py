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


def get_sides(region):
    """
    This function calculates the number of corners in a region by iterating over every grid position
    in the bounding box of the region, plus 1 to the right and down. It checks if each grid corner is part
    of the region by examining its surrounding points. The function distinguishes between regular corners
    and double-counted corners based on specific configuration indices.

    A corner is identified when the configuration index is not in {0, 3, 5, 10, 12, 15}.
    Double-counted corners are identified when the configuration index is in {6, 9}.

    The total number of sides (corners) is calculated as the size of the set of corners plus any double
    counted corners.
    """
    corners = set()
    double_corner_counter = 0
    xs = {x for _, x in region}
    ys = {y for y, _ in region}
    for y in range(min(ys), max(ys) + 2):
        for x in range(min(xs), max(xs) + 2):
            index = sum(
                ((y + dy, x + dx) in region) * sf
                for dx, dy, sf in [(-1, -1, 1), (-1, 0, 2), (0, -1, 4), (0, 0, 8)]
            )
            if index not in [0, 3, 5, 10, 12, 15]:
                corners.add((y, x))
            if index in [6, 9]:
                double_corner_counter += 1
    return len(corners) + double_corner_counter


def get_regions(text: str) -> list[list]:
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
    return regions


def solve_part_1(text: str):
    regions = get_regions(text)
    return sum(get_area(r) * get_perimeter(r) for r in regions)


def solve_part_2(text: str):
    regions = get_regions(text)
    return sum(get_area(r) * get_sides(r) for r in regions)


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
