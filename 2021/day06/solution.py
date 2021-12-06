import re
from collections import Counter


def iter_generation(ages: Counter) -> Counter:
    new_ages = Counter()
    for age in range(8, -1, -1):
        if age == 0:
            new_ages[6] += ages[0]
            new_ages[8] += ages[0]
        else:
            new_ages[(age - 1)] = ages[age]
    return new_ages


def solve(text: str, days: int):
    ages = Counter([int(x) for x in re.findall("[0-9]+", text)])
    for _ in range(1, days + 1):
        ages = iter_generation(ages)
    return sum(ages.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve(quiz_input, 80))
        print("Part 2:", solve(quiz_input, 256))
