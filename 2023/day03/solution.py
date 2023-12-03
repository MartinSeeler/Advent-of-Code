from collections import defaultdict
import time
import re


def parse_symbols_map(text: str):
    return {
        (cidx, lidx): c
        for lidx, line in enumerate(text.splitlines())
        for cidx, c in enumerate(line)
        if not c.isdigit() and c != "."
    }


def parse_input(text: str):
    num_lines = len(text.splitlines())
    symbols_map = parse_symbols_map(text)
    symbols_coords = list(symbols_map.keys())
    numers_map = defaultdict(list)
    for lidx, line in enumerate(text.splitlines()):
        # search all numbers in line via regex and save the match
        for match in re.finditer(r"\d+", line):
            span = match.span()
            x_start = max(span[0] - 1, 0)
            x_end = min(span[1] + 1, len(line))
            y_start = max(lidx - 1, 0)
            y_end = min(lidx + 2, num_lines)

            matching_symbol_coords = [
                symbol_coord
                for symbol_coord in symbols_coords
                if x_start <= symbol_coord[0] < x_end
                and y_start <= symbol_coord[1] < y_end
            ]

            for symbol_coord in matching_symbol_coords:
                numers_map[symbol_coord].append(int(match.group()))
    return symbols_map, numers_map


def solve_part_1(text: str):
    _, numers_map = parse_input(text)
    return sum(sum(v) for v in numers_map.values())


def solve_part_2(text: str):
    symbols_map, numers_map = parse_input(text)
    gear_symbol_coords = [c for c in symbols_map.keys() if symbols_map[c] == "*"]
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
