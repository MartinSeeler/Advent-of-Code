import time

add = lambda a, b: a + b
multiply = lambda a, b: a * b
merge = lambda a, b: int(str(a) + str(b))


def can_make_target(target, numbers, ops):
    possible_results = {numbers[0]}

    for num in numbers[1:]:
        new_results = set()
        for prev_result in possible_results:
            for op in ops:
                res = op(prev_result, num)
                if res <= target:
                    new_results.add(res)

        possible_results = new_results

    return target in possible_results


def parse_input(text: str):
    for line in text.splitlines():
        exp_result = int(line.split(": ")[0])
        nums = [int(x) for x in line.split(": ")[1].split(" ")]
        yield exp_result, nums


def solve_part_1(text: str):
    return sum(
        exp_result
        for exp_result, nums in parse_input(text)
        if can_make_target(exp_result, nums, [add, multiply])
    )


def solve_part_2(text: str):
    return sum(
        exp_result
        for exp_result, nums in parse_input(text)
        if can_make_target(exp_result, nums, [add, multiply, merge])
    )


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
