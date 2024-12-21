import time
from memoization import cached


NUMERIC_KEYPAD = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

DIRECTIONAL_KEYPAD = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}


DIRECTIONS = {
    (0, 1): "v",
    (1, 0): ">",
    (-1, 0): "<",
    (0, -1): "^",
}


def get_neighbors(pos, world):
    x, y = pos
    neighbors = []
    for (dx, dy), move in DIRECTIONS.items():
        new_pos = (x + dx, y + dy)
        if new_pos in world.values():
            neighbors.append((new_pos, move))
    return neighbors


def a_star(start, end, world):
    start_pos = world[start]
    end_pos = world[end]

    open_set = [(0, start_pos, "")]
    costs = {start_pos: 0}
    paths = {start_pos: set([""])}

    def heuristic(pos):
        return abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1])

    while open_set:
        # Sort by priority (cost + heuristic) and pop the smallest
        open_set.sort(key=lambda x: x[0])
        _, current, path = open_set.pop(0)

        for neighbor, move in get_neighbors(current, world):
            new_cost = costs[current] + 1

            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                paths[neighbor] = set([p + move for p in paths[current]])
                priority = new_cost + heuristic(neighbor)
                open_set.append((priority, neighbor, path + move))
            elif new_cost == costs[neighbor]:
                paths[neighbor].update(p + move for p in paths[current])

    return list(paths.get(end_pos, []))


# Generate all shortest paths
def generate_all_shortest_paths(world):
    shortest_paths = {}
    for start in world.keys():
        for end in world.keys():
            if start != end:
                all_paths = a_star(start, end, world)
                shortest_paths[f"{start}{end}"] = all_paths
    return shortest_paths


def generate_numpad_paths():
    return generate_all_shortest_paths(NUMERIC_KEYPAD)


def generate_keypad_paths():
    return generate_all_shortest_paths(DIRECTIONAL_KEYPAD)


NUMPAD_PATHS = generate_numpad_paths()
KEYPAD_PATHS = generate_keypad_paths()


@cached
def find_shortest(code, depth):
    if depth == 0:
        return len(code) + 1
    code_next = f"A{code}A"
    total = 0
    for i in range(len(code_next) - 1):
        n = code_next[i] + code_next[i + 1]
        paths = KEYPAD_PATHS[n] if n in KEYPAD_PATHS else [""]
        total += min(find_shortest(p, depth - 1) for p in paths)
    return total


def solve(text, depth):
    sum = 0
    for code in text.splitlines():
        code_next = f"A{code}"
        total = 0
        for i in range(len(code_next) - 1):
            paths = NUMPAD_PATHS[code_next[i] + code_next[i + 1]]
            total += min(find_shortest(p, depth) for p in paths)
        sum += total * int(code[:3])

    return sum


def solve_part_1(text: str):
    return solve(text, 2)


def solve_part_2(text: str):
    return solve(text, 25)


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
