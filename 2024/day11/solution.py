import functools
import time


@functools.lru_cache(None)
def transform_number(n: int):
    n_str = str(n)
    if n == 0:
        return [1]
    elif len(n_str) % 2 == 0:
        l, r = n_str[: len(n_str) // 2], n_str[len(n_str) // 2 :]
        return [int(l), int(r)]
    else:
        # multiply number by 2024
        return [n * 2024]


def transform_numbers(numbers: list[int]):
    for n in numbers:
        for n_transformed in transform_number(n):
            yield n_transformed


def solve_part_1(text: str):
    numbers = [int(x) for x in text.strip().split(" ")]
    for _ in range(25):
        numbers = list(transform_numbers(numbers))
    return len(numbers)


def solve_part_2(text: str):
    numbers = [int(x) for x in text.strip().split(" ")]
    for _ in range(75):
        numbers = list(transform_numbers(numbers))
    return len(numbers)


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
