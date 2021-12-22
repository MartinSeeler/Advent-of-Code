from collections import Counter
import re
import time
import numpy as np


def solve(text: str, only_small=False):
    cubes = []
    for line in text.splitlines():
        state, rest = line.split()
        [x_from, x_to, y_from, y_to, z_from, z_to] = list(
            map(int, re.findall("[-]?[0-9]+", rest))
        )
        # check if the coordinates are in range -50 to 50
        if only_small and (
            x_from < -50
            or x_to > 50
            or y_from < -50
            or y_to > 50
            or z_from < -50
            or z_to > 50
        ):
            continue
        for idx, [
            other_x_from,
            other_x_to,
            other_y_from,
            other_y_to,
            other_z_from,
            other_z_to,
        ] in enumerate(cubes):
            if (
                x_from > other_x_to
                or x_to < other_x_from
                or y_from > other_y_to
                or y_to < other_y_from
                or z_from > other_z_to
                or z_to < other_z_from
            ):
                continue  # skip non overlapping cubes
            cubes[idx] = None  # remove old cube and add sub-cubes
            if x_from > other_x_from:
                cubes.append(
                    (
                        other_x_from,
                        x_from - 1,
                        other_y_from,
                        other_y_to,
                        other_z_from,
                        other_z_to,
                    )
                )
            if x_to < other_x_to:
                cubes.append(
                    (
                        x_to + 1,
                        other_x_to,
                        other_y_from,
                        other_y_to,
                        other_z_from,
                        other_z_to,
                    )
                )
            if y_from > other_y_from:
                cubes.append(
                    (
                        max(other_x_from, x_from),
                        min(other_x_to, x_to),
                        other_y_from,
                        y_from - 1,
                        other_z_from,
                        other_z_to,
                    )
                )
            if y_to < other_y_to:
                cubes.append(
                    (
                        max(other_x_from, x_from),
                        min(other_x_to, x_to),
                        y_to + 1,
                        other_y_to,
                        other_z_from,
                        other_z_to,
                    )
                )
            if z_from > other_z_from:
                cubes.append(
                    (
                        max(other_x_from, x_from),
                        min(other_x_to, x_to),
                        max(other_y_from, y_from),
                        min(other_y_to, y_to),
                        other_z_from,
                        z_from - 1,
                    )
                )
            if z_to < other_z_to:
                cubes.append(
                    (
                        max(other_x_from, x_from),
                        min(other_x_to, x_to),
                        max(other_y_from, y_from),
                        min(other_y_to, y_to),
                        z_to + 1,
                        other_z_to,
                    )
                )
        if state == "on":
            cubes.append(
                (
                    min(x_from, x_to),
                    max(x_from, x_to),
                    min(y_from, y_to),
                    max(y_from, y_to),
                    min(z_from, z_to),
                    max(z_from, z_to),
                )
            )
        cubes = [cube for cube in cubes if cube is not None]
    return sum(
        map(
            lambda cube: (cube[1] - cube[0] + 1)
            * (cube[3] - cube[2] + 1)
            * (cube[5] - cube[4] + 1),
            cubes,
        )
    )


def solve_part_1(text: str):
    return solve(text, only_small=True)


def solve_part_2(text: str):
    return solve(text)


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
