import time


def solve(text: str, days: int):
    ages = [*map(text.count, "012345678")]
    for _ in range(days):
        ages = ages[1:] + ages[:1]
        ages[6] += ages[-1]
    return sum(ages)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = solve(quiz_input, 80)
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
        p_2_solution = solve(quiz_input, 256)
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
