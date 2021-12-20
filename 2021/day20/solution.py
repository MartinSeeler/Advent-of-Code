from itertools import product
import time

all_sides = list(product((-1, 0, 1), (-1, 0, 1)))


def step(image, enhance, input_on):
    visited = set()
    new_image = set()

    for (x, y) in image:
        for (dx, dy) in all_sides:
            if (x + dx, y + dy) in visited:
                continue
            visited.add((x + dx, y + dy))
            bin_num = ""
            for (ddy, ddy) in all_sides:
                bin_num += (
                    "1" if ((x + dx + ddy, y + dy + ddy) in image) == input_on else "0"
                )
            if (enhance[int(bin_num, 2)] == "#") is not input_on:
                new_image.add((x + dx, y + dy))

    return new_image


def parse(text: str):
    enhance, img_data = text.split("\n\n")
    image = set()
    for x, row in enumerate(img_data.splitlines()):
        for y, v in enumerate(row):
            if v == "#":
                image.add((x, y))
    return enhance, image


def solve_part_1(text: str):
    enhance, image = parse(text)
    for _ in range(1):
        image = step(step(image, enhance, True), enhance, False)
    return len(image)


def solve_part_2(text: str):
    enhance, image = parse(text)
    for _ in range(25):
        image = step(step(image, enhance, True), enhance, False)
    return len(image)


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
