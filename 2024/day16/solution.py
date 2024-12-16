import time
from collections import deque

POSSIBLE_DIRS = (1, -1, 1j, -1j)


def calculate_min_scores(
    start: complex, walls: set[complex]
) -> dict[complex, dict[complex, int]]:
    scores = {1: {start: 0}, -1: {}, 1j: {}, -1j: {}}
    points = deque([(start, 1)])
    while points:
        p, d = points.popleft()
        score = scores[d][p]
        for move, dir, cost in [(p + d, d, 1), (p, d * -1j, 1000), (p, d * 1j, 1000)]:
            if move in walls:
                continue
            if move in scores[dir] and scores[dir][move] <= score + cost:
                continue
            scores[dir][move] = score + cost
            points.append((move, dir))
    return scores


def solve_part_1(text: str):
    walls: set[complex] = set()
    start: complex = 0j
    end: complex = 0j
    for y, row in enumerate(text.splitlines()):
        for x, c in enumerate(row):
            match c:
                case "#":
                    walls.add(complex(x, y))
                case "S":
                    start = complex(x, y)
                case "E":
                    end = complex(x, y)
                case _:
                    pass
    scores = calculate_min_scores(start, walls)
    return min(scores[dir][end] for dir in POSSIBLE_DIRS if end in scores[dir])


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
