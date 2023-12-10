import time


def predict_next(line: str, backwards=False):
    all_nums = [[int(n) for n in line.split(" ")]]
    while not all(x == 0 for x in all_nums[-1]):
        next_diffs = [
            all_nums[-1][i + 1] - all_nums[-1][i] for i in range(len(all_nums[-1]) - 1)
        ]
        all_nums.append(next_diffs)

    next_value = 0
    for num_list in reversed(all_nums):
        next_value = (
            num_list[0] - next_value if backwards else num_list[-1] + next_value
        )

    return next_value


def solve_part_1(text: str):
    return sum(predict_next(line) for line in text.splitlines())


def solve_part_2(text: str):
    return sum(predict_next(line, True) for line in text.splitlines())


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
