def solve(text: str, days: int):
    initial_ages = list(map(int, text.split(",")))
    age_counts = [initial_ages.count(i) for i in range(9)]
    for _ in range(days):
        newborns = age_counts.pop(0)
        age_counts[6] += newborns
        age_counts.append(newborns)
    return sum(age_counts)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve(quiz_input, 80))
        print("Part 2:", solve(quiz_input, 256))
