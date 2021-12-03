from collections import defaultdict


def solve_part_1(text: str):
    gamma = ""
    numbers = text.splitlines()
    for pos in range(len(numbers[0])):
        bit_counts = defaultdict(int)
        for line in numbers:
            bit_counts[line[pos]] += 1
        gamma += "0" if bit_counts["0"] > bit_counts["1"] else "1"
    epsilon = "".join(["1" if c == "0" else "0" for c in gamma])
    return int(epsilon, 2) * int(gamma, 2)


def find_recursive(
    numbers: list[str], pos: int, keep_bit: str, drop_bit: str
) -> list[str]:
    if len(numbers) == 1:
        return numbers
    bit_lists = defaultdict(list)
    for line in numbers:
        bit_lists[line[pos]].append(line)
    if len(bit_lists["1"]) >= len(bit_lists["0"]):
        return find_recursive(bit_lists[keep_bit], pos + 1, keep_bit, drop_bit)
    else:
        return find_recursive(bit_lists[drop_bit], pos + 1, keep_bit, drop_bit)


def solve_part_2(text: str):
    numbers = text.splitlines()
    oxygen_generator_rating = find_recursive(numbers, 0, "1", "0")[0]
    co2_scrubber_rating = find_recursive(numbers, 0, "0", "1")[0]
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve_part_1(quiz_input))
        print("Part 2:", solve_part_2(quiz_input))
