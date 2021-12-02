def solve_part_1(input: str):
    numbers = list(map(int, input.splitlines()))
    return sum(x < y for x, y in zip(numbers, numbers[1:]))


def solve_part_2(input: str):
    numbers = list(map(int, input.splitlines()))
    sum_of_triples = list(map(sum, zip(numbers, numbers[1:], numbers[2:])))
    return sum(x < y for x, y in zip(sum_of_triples, sum_of_triples[1:]))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve_part_1(quiz_input))
        print("Part 2:", solve_part_2(quiz_input))
