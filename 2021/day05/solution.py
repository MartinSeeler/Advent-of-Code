from collections import Counter
import re


def get_line_points(x1, y1, x2, y2):
    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    if y1 == y2:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    x_range = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
    y_range = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
    return zip(x_range, y_range)


def solve_part_1(text: str):
    c = Counter()
    for line in text.splitlines():
        [x1, y1, x2, y2] = x = list(map(int, re.findall("[0-9]+", line)))
        if x1 == x2 or y1 == y2:
            for (x, y) in get_line_points(x1, y1, x2, y2):
                c[(x, y)] += 1
    return len(list(filter(lambda x: x >= 2, list(c.values()))))


def solve_part_2(text: str):
    c = Counter()
    for line in text.splitlines():
        [x1, y1, x2, y2] = x = list(map(int, re.findall("[0-9]+", line)))
        for (x, y) in get_line_points(x1, y1, x2, y2):
            c[(x, y)] += 1
    return len(list(filter(lambda x: x >= 2, list(c.values()))))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve_part_1(quiz_input))
        print("Part 2:", solve_part_2(quiz_input))
