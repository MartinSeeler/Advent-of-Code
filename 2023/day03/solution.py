from collections import defaultdict
import time
import re


def parse_symbols_map(text: str):
    symbols_map = {}
    for lidx, line in enumerate(text.splitlines()):
        for cidx, c in enumerate(line):
            if not c.isdigit() and c != ".":
                symbols_map[(cidx, lidx)] = c
    return symbols_map


def solve_part_1(text: str):
    res = 0
    # transform text to 2D array of characters
    m = []
    for line in text.splitlines():
        m.append(list(line))
    for lidx, line in enumerate(text.splitlines()):
        # search all numbers in line via regex and save the match
        for match in re.finditer(r"\d+", line):
            span = match.span()
            print("found", match.group(), "at", span)
            # get range around span
            x_start = span[0] - 1
            x_end = span[1]
            y_start = lidx - 1
            y_end = lidx + 1
            # normalize range to not exceed matrix
            x_start = max(0, x_start)
            x_end = min(len(line), x_end + 1)
            y_start = max(0, y_start)
            y_end = min(len(m), y_end + 1)
            print("checking range", x_start, x_end, y_start, y_end)
            for x in range(x_start, x_end):
                for y in range(y_start, y_end):
                    # check if current position is not a number and not a dot
                    if not m[y][x].isdigit() and m[y][x] != ".":
                        # parse number
                        num = int(match.group())
                        print("adding", num, "at", x, y)
                        res += num
    return res


def solve_part_2(text: str):
    num_lines = len(text.splitlines())
    symbols_map = parse_symbols_map(text)
    print(symbols_map)
    symbols_coords = list(symbols_map.keys())
    numers_map = defaultdict(list)
    for lidx, line in enumerate(text.splitlines()):
        # search all numbers in line via regex and save the match
        for match in re.finditer(r"\d+", line):
            span = match.span()
            # get range around span
            x_start = span[0] - 1
            x_end = span[1]
            y_start = lidx - 1
            y_end = lidx + 1
            # normalize range to not exceed matrix
            x_start = max(0, x_start)
            x_end = min(len(line), x_end + 1)
            y_start = max(0, y_start)
            y_end = min(num_lines, y_end + 1)
            #
            x_range = range(x_start, x_end)
            y_range = range(y_start, y_end)
            matching_symbol_coords = filter(
                lambda c: c[0] in x_range and c[1] in y_range,
                symbols_coords,
            )
            for symbol_coord in matching_symbol_coords:
                numers_map[symbol_coord].append(int(match.group()))
    gear_symbol_coords = list(filter(lambda c: symbols_map[c] == "*", symbols_coords))
    res = 0
    for gsc in gear_symbol_coords:
        if len(numers_map[gsc]) == 2:
            res += numers_map[gsc][0] * numers_map[gsc][1]
    return res


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
