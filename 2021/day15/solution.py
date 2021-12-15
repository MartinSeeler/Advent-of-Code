import heapq
import time


def dijkstra(matrix: list[list[int]]) -> int:
    edges: dict[(int, int), set[(int, int)]] = {}
    risks: dict[(int, int), int] = {}
    for x, row in enumerate(matrix):
        for y, weight in enumerate(row):
            pos = x, y

            risks[pos] = weight

            if pos not in edges:
                edges[pos] = set()
            for x_d, y_d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x_next, y_next = x + x_d, y + y_d
                if (
                    x_next < 0
                    or y_next < 0
                    or x_next >= len(matrix)
                    or y_next >= len(matrix[0])
                ):
                    continue
                edges[pos].add((x_next, y_next))

    start = (0, 0)
    distances = {node: 1337424242 for node in edges}
    distances[start] = 0

    priority_queue: list[(int, (int, int))] = [(0, start)]
    while priority_queue:
        distance, current = heapq.heappop(priority_queue)
        for neighbor in edges[current]:
            if (cost := distance + risks[neighbor]) < distances[neighbor]:
                distances[neighbor] = cost
                heapq.heappush(priority_queue, (cost, neighbor))

    return distances[len(matrix) - 1, len(matrix[0]) - 1]


def solve_part_1(text: str):
    world = [list(map(int, line)) for line in text.splitlines()]
    return dijkstra(world)


def solve_part_2(text: str):
    world = [list(map(int, line)) for line in text.splitlines()]
    height = len(world)
    width = len(world[0])

    for row in world:
        for chunk in range(4):
            row += [((col + 1) % 10) or 1 for col in row[width * chunk :]]

    for chunk in range(4):
        for row in world[height * chunk :]:
            world.append([((col + 1) % 10) or 1 for col in row])
    return dijkstra(world)


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
