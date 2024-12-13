import re
import time


def find_min_cost_for_machine(machine: list[int], add: int = 0):
    A_x, A_y, B_x, B_y, X, Y = machine
    X += add
    Y += add

    # Compute the determinant
    Δ = A_x * B_y - A_y * B_x
    if Δ == 0:
        return 0  # No unique solution

    # Apply Cramer's rule
    # A = (X*B_y - Y*B_x) / Δ
    # B = (A_x*Y - A_y*X) / Δ
    numerator_A = X * B_y - Y * B_x
    numerator_B = A_x * Y - A_y * X

    # Check if A and B are integers
    if numerator_A % Δ != 0 or numerator_B % Δ != 0:
        return 0

    A = numerator_A // Δ
    B = numerator_B // Δ

    # Check non-negativity
    if A >= 0 and B >= 0:
        return 3 * A + B

    return 0


def parse(text: str) -> list[int]:
    numbers = list(map(int, re.findall(r"\d+", text)))
    # Every "machine" is a collection of 6 numbers, so we split our list into chunks of 6
    return [numbers[i : i + 6] for i in range(0, len(numbers), 6)]


def solve_part_1(text: str):
    return sum(find_min_cost_for_machine(machine) for machine in parse(text))


def solve_part_2(text: str):
    return sum(
        find_min_cost_for_machine(machine, 10000000000000) for machine in parse(text)
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
