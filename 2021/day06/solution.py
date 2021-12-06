def solve(text: str, days: int):
    ages = [*map(text.count, "012345678")]
    for _ in range(days):
        ages = ages[1:] + ages[:1]
        ages[6] += ages[-1]
    return sum(ages)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve(quiz_input, 80))
        print("Part 2:", solve(quiz_input, 256))
