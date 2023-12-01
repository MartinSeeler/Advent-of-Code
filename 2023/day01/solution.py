import re


def solve_part_1(input: str):
    total = 0
    for line in input.splitlines():
        first = None
        last = None
        for c in line:
            if c.isdigit():
                if first is None:
                    first = int(c)
                last = int(c)

        val = first * 10 + last
        total += val
    return total


number_strings = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def solve_part_2(input: str):
    total = 0
    for line in input.splitlines():
        first = None
        last = None
        for line_idx, c in enumerate(line):
            if c.isdigit():
                if first is None:
                    first = int(c)
                last = int(c)
            else:
                for idx, number_string in enumerate(number_strings):
                    if line[line_idx:].startswith(number_string):
                        if first is None:
                            first = idx + 1
                        last = idx + 1
                        break
        val = first * 10 + last
        total += val
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve_part_1(quiz_input))
        print("Part 2:", solve_part_2(quiz_input))
