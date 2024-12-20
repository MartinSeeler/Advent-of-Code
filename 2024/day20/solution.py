import time


def solve(text: str, min_saves: int = 100, cheat_length: int = 2):
    world = {
        (x, y): c
        for y, line in enumerate(text.splitlines())
        for x, c in enumerate(line.strip())
    }

    x, y = next(k for k, v in world.items() if v == "S")
    distances = {(x, y): 0}
    while world[(x, y)] != "E":
        for pos_next in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if world[pos_next] in ".E" and pos_next not in distances:
                distances[pos_next] = distances[(x, y)] + 1
                x, y = pos_next

    return sum(
        distances.get((dis_x + dx, dis_y + dy), 0) - dis - abs(dx) - abs(dy)
        >= min_saves
        for (dis_x, dis_y), dis in distances.items()
        for dy in range(-cheat_length, cheat_length + 1)
        for dx in range(-cheat_length + abs(dy), cheat_length - abs(dy) + 1)
    )


def solve_part_1(text: str, min_saves: int = 100):
    return solve(text, min_saves=min_saves, cheat_length=2)


def solve_part_2(text: str, min_saves: int = 100):
    return solve(text, min_saves=min_saves, cheat_length=20)


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
