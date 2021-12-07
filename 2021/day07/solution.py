def solve_part_1(text: str):
    nums = [int(x) for x in text.split(",")]
    return min([sum([abs(n - idx) for n in nums]) for idx in range(max(nums))])


def solve_part_2(text: str):
    nums = [int(x) for x in text.split(",")]
    return min(
        [
            sum([(abs(n - idx)) * (abs(n - idx) + 1) // 2 for n in nums])
            for idx in range(max(nums))
        ]
    )


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve_part_1(quiz_input))
        print("Part 2:", solve_part_2(quiz_input))
