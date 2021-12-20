import itertools
from collections import Counter
import time

import numpy as np


def all_orientations(scanner):
    for dir_x, dir_y in itertools.permutations(range(3), 2):
        for sign_x, sign_y in itertools.product((-1, 1), (-1, 1)):
            x_vec = np.zeros((3,))
            y_vec = np.zeros((3,))
            x_vec[dir_x] = sign_x
            y_vec[dir_y] = sign_y
            z_vec = np.cross(x_vec, y_vec)
            yield np.array(
                [
                    np.array(
                        [
                            np.dot(x_vec, beacon),
                            np.dot(y_vec, beacon),
                            np.dot(z_vec, beacon),
                        ]
                    )
                    for beacon in scanner
                ]
            ).reshape(-1, 3)


def solve(text: str):
    scanner_inputs = text.split("\n\n")
    scanners = [
        np.array(
            [np.array(list(map(int, xs.split(",")))) for xs in si.splitlines()[1:]]
        )
        for si in scanner_inputs
    ]
    beacons = scanners[0]
    remaining = scanners[1:]
    scanners = set([tuple([0, 0, 0])])
    while len(remaining) > 0:
        for i, scanner in enumerate(remaining):
            # print("scanner", i, "of", len(remaining))
            for o in all_orientations(scanner):
                c = Counter()
                for p2 in o:
                    for p1 in beacons:
                        c[tuple(p1 - p2)] += 1
                msc = c.most_common()[0]
                if msc[1] >= 12:
                    v = np.array(msc[0])
                    target = o + v
                    scanners.add(tuple(v))
                    # print("found", v)
                    beacons = np.concatenate((beacons, target))
                    remaining.pop(i)
                    break
    return scanners, beacons


def solve_part_1(completed):
    return len(set([tuple(i) for i in completed.tolist()]))


def solve_part_2(scanners):
    return np.max(
        [
            np.sum(np.abs(np.array(i) - np.array(j)))
            for i in scanners
            for j in scanners
            if i != j
        ]
    )


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        scanners, beacons = solve(quiz_input)
        p_1_solution = int(solve_part_1(beacons))
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.2f}ms)")
        p_2_solution = int(solve_part_2(scanners))
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.2f}ms)")
