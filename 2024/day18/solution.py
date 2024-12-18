import time

POSSIBLE_DIRS = (1, -1, 1j, -1j)


def a_star(pos: complex, target: complex, corrupted: set[complex], size: int) -> int:
    queue: list[tuple[complex, complex]] = [(pos, 0)]
    visited: set[complex] = set()

    while queue:
        pos, dist = queue.pop(0)
        if pos == target:
            return dist

        for dir in POSSIBLE_DIRS:
            new_pos = pos + dir
            if (
                new_pos not in corrupted
                and new_pos not in visited
                and 0 <= new_pos.real <= size
                and 0 <= new_pos.imag <= size
            ):
                visited.add(new_pos)
                queue.append((new_pos, dist + 1))

    raise ValueError("No path found")


def parse_bytes(text: str) -> list[complex]:
    return [
        complex(x, y)
        for line in text.splitlines()
        for x, y in (map(int, line.split(",")),)
    ]


def solve_part_1(text: str, size=70, bytes=1024):
    target: complex = size + size * 1j
    corrupted = set(parse_bytes(text)[:bytes])
    return a_star(0 + 0j, target, corrupted, size)


def solve_part_2(text: str, size=70):
    target: complex = size + size * 1j
    corrupted_bytes = parse_bytes(text)

    left, right = 0, len(corrupted_bytes)
    while left < right:
        mid = (left + right) // 2
        try:
            a_star(0 + 0j, target, corrupted_bytes[:mid], size)
            left = mid + 1
        except ValueError:
            right = mid

    return text.splitlines()[left - 1]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = int(solve_part_1(quiz_input))
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
        p_2_solution = solve_part_2(quiz_input)
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
