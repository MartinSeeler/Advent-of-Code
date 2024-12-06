from collections import defaultdict
import time

dirs = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
dirs_rot = ["^", ">", "v", "<"]


def get_path_or_none(text: str):
    obstacles = set()
    current_dir = "^"
    current_pos = (0, 0)
    cols, rows = len(text.splitlines()[0]), len(text.splitlines())
    for y, line in enumerate(text.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((x, y))
            if char in dirs_rot:
                current_dir = char
                current_pos = (x, y)

    done = False
    seen = defaultdict(list[str])
    while not done:
        # check if we moved the same direction on the same spot already
        if current_dir in seen[current_pos]:
            # thats a loop, so we can stop here
            return None
        seen[current_pos].append(current_dir)

        next_pos = tuple(map(sum, zip(current_pos, dirs[current_dir])))
        if next_pos in obstacles:
            # time to rotate
            current_dir = dirs_rot[(dirs_rot.index(current_dir) + 1) % len(dirs_rot)]
            continue

        if (
            next_pos[0] < 0
            or next_pos[0] >= cols
            or next_pos[1] < 0
            or next_pos[1] >= rows
        ):
            # we are out of the map
            done = True
            break

        current_pos = next_pos

    return seen.keys()


def solve_part_1(text: str):
    return len(get_path_or_none(text))


def solve_part_2(text: str):
    # we can keep the number of positions to check low
    # by only considering the positions we move on originally
    possible_mutation_positions = list(get_path_or_none(text))[1:]  # skip start
    print(f"checking {len(possible_mutation_positions)} possible mutations")
    final_mutations = 0

    text_matrix = [list(line) for line in text.splitlines()]
    for pos in possible_mutation_positions:
        text_matrix_mutated = [list(line) for line in text_matrix]
        x, y = pos
        text_matrix_mutated[y][x] = "#"
        text_mutated = "\n".join(["".join(line) for line in text_matrix_mutated])
        if get_path_or_none(text_mutated) is None:
            final_mutations += 1
    return final_mutations


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
