import time


def parse_universe(text: str, expansion=1):
    lines = text.splitlines()
    matrix = [list(line) for line in lines]
    galaxy_coords = set()
    cols_to_expand = {
        c
        for c in range(len(matrix[0]))
        if all(matrix[r][c] == "." for r in range(len(matrix)))
    }
    rows_to_expand = {
        r
        for r in range(len(matrix))
        if all(matrix[r][c] == "." for c in range(len(matrix[0])))
    }
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "#":
                galaxy_coords.add(
                    (
                        x + sum([expansion for ce in cols_to_expand if ce < x]),
                        y + sum([expansion for re in rows_to_expand if re < y]),
                    )
                )
    return galaxy_coords


def calculate_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_part_1(text: str):
    galaxies = parse_universe(text)
    total_distance = 0
    for a in galaxies:
        for b in galaxies:
            if a == b:
                continue
            total_distance += calculate_distance(a, b)
    return total_distance // 2


def solve_part_2(text: str):
    galaxies = parse_universe(text, expansion=1000000 - 1)
    seen = dict()
    for a in galaxies:
        for b in galaxies:
            if a == b:
                continue
            if (a, b) in seen:
                continue
            if (b, a) in seen:
                continue
            seen[(a, b)] = calculate_distance(a, b)
    return sum(seen.values())


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
