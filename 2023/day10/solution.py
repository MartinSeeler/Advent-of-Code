from collections import defaultdict
import time


def parse_adjacence_tiles(text: str):
    adj_tiles = defaultdict(set)
    s = (0, 0)
    tile_mapping = {
        "-": [(-1, 0), (1, 0)],
        "|": [(0, -1), (0, 1)],
        "F": [(1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(-1, 0), (0, 1)],
        "L": [(1, 0), (0, -1)],
    }

    for y, line in enumerate(text.splitlines()):
        for x, t in enumerate(line):
            if t == "S":
                s = (x, y)
            if t == ".":
                continue
            if t in tile_mapping:
                for dx, dy in tile_mapping[t]:
                    n = (x + dx, y + dy)
                    if n == (19, 88):
                        print(f"Found {n} from {x,y} via {t}")
                    adj_tiles[n].add((x, y))

    return adj_tiles, s


def find_cycle(adj_tiles, s):
    start, end = list(adj_tiles[s])  # there are only two adjacent tiles for the start
    path = [start]
    visited = {start}
    cycle = set()
    while path:
        current_tile = path[-1]
        if current_tile == end:
            cycle.update(path)
            path.pop()
        elif current_tile in path[:-1]:
            cycle_start_index = path.index(current_tile)
            cycle.update(path[cycle_start_index:])
            path = path[: cycle_start_index + 1]
        else:
            unvisited_tiles = [
                tile for tile in adj_tiles[current_tile] if tile not in visited
            ]
            if unvisited_tiles:
                next_tile = unvisited_tiles[0]
                path.append(next_tile)
                visited.add(next_tile)
            else:
                path.pop()
    cycle.add(s)
    return cycle


def solve_part_1(text: str):
    adj_tiles, s = parse_adjacence_tiles(text)
    cycle = find_cycle(adj_tiles, s)
    return len(cycle) // 2


def solve_part_2(text: str):
    adj_tiles, s = parse_adjacence_tiles(text)
    cycle = find_cycle(adj_tiles, s)

    interior_points = 0

    y_max = len(text.splitlines())
    x_max = len(text.splitlines()[0])
    for y in range(y_max):
        for x in range(x_max):
            # Skip points that are in the cycle already
            if (x, y) in cycle:
                continue

            # Cast a ray from the point to the right
            ray = [(i, y) for i in range(x, x_max) if (i, y) in cycle]

            # Count the number of intersections with the cycle, but only consider
            # intersections with the |, J, and L tiles, since other pipes are
            # no cross-sections
            intersections = sum(
                1 for px, py in ray if text.splitlines()[py][px] in "|JL"
            )

            # If the number of intersections is odd, the point is inside the polygon
            if intersections % 2 == 1:
                interior_points += 1

    return interior_points


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
