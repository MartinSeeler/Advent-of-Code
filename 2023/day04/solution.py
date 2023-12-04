from collections import Counter, deque
import time


def get_matches(text: str):
    result = []
    for line in text.splitlines():
        _, numbers = line.split(": ")
        card_numbers, my_numbers = [
            [int(x) for x in xs.strip().split(" ") if x != ""]
            for xs in numbers.strip().split("|")
        ]
        matches_count = 0
        for mn in my_numbers:
            if mn in card_numbers:
                matches_count += 1
        result.append(matches_count)
    return result


def solve_part_1(text: str):
    return sum(2 ** (m - 1) for m in get_matches(text) if m > 0)


def solve_part_2(text: str):
    card_matches_table = get_matches(text)
    cards_counter = Counter()
    cards_queue = deque(range(1, len(card_matches_table) + 1))

    while cards_queue:
        card_idx = cards_queue.popleft()
        cards_counter[card_idx] += 1
        matches = card_matches_table[card_idx - 1]

        for idx2 in range(card_idx + 1, card_idx + matches + 1):
            if idx2 <= len(card_matches_table):
                cards_queue.append(idx2)

    return sum(cards_counter.values())


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
