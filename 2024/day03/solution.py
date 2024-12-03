import time
import re


def parse_muls(text: str) -> list[tuple[int, int, int]]:
    r = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return [
        (int(match.group(1)), int(match.group(2)), match.start())
        for match in r.finditer(text)
    ]


def solve_part_1(text: str):
    return sum(x * y for x, y, _ in parse_muls(text))


def parse_instructs(text: str) -> tuple[list[int]]:
    r_do = re.compile(r"do\(\)")
    r_dont = re.compile(r"don't\(\)")
    return [match.start() for match in r_do.finditer(text)], [
        match.start() for match in r_dont.finditer(text)
    ]


def solve_part_2(text: str):
    dos, donts = parse_instructs(text)
    ranges = []
    i_dont, i_do = 0, 0
    while i_dont < len(donts) and i_do < len(dos):
        if donts[i_dont] <= dos[i_do]:
            ranges.append((donts[i_dont], dos[i_do]))
            i_dont += 1
        else:
            i_do += 1

    muls = parse_muls(text)
    for r in ranges:
        muls = [(x, y, i) for x, y, i in muls if not (r[0] <= i < r[1])]
    return sum(x * y for x, y, _ in muls)


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
