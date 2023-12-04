from collections import Counter
import time


def get_matches(text):
    return [
        sum(1 for mn in my if mn in card)
        for _, num in (line.split(": ") for line in text.splitlines())
        for card, my in [[list(map(int, xs.split())) for xs in num.split("|")]]
    ]


def solve_part_1(text):
    return sum(2 ** (m - 1) for m in get_matches(text) if m > 0)


def solve_part_2(text):
    matches = get_matches(text)
    counter = Counter()
    for i, m in enumerate(matches, 1):
        counter[i] += 1
        for j in range(i + 1, i + m + 1):
            if j <= len(matches):
                counter[j] += counter[i]
    return sum(counter.values())


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
