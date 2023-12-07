from collections import Counter
import time

hand_types = [
    "HIGH_CARD",
    "PAIR",
    "TWO_PAIRS",
    "THREE_OF_A_KIND",
    "FULL_HOUSE",
    "FOUR_OF_A_KIND",
    "FIVE_OF_A_KIND",
]

card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_values_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def get_hand_type(hand: str, joker_mode=False):
    card_dist = Counter(hand)
    j_count = card_dist.get("J", 0)
    card_dist_sorted = sorted(card_dist.values(), reverse=True)
    if card_dist_sorted == [2, 1, 1, 1]:
        if joker_mode and j_count >= 1:
            return hand_types[3]
        return hand_types[1]
    elif card_dist_sorted == [2, 2, 1]:
        if joker_mode and j_count == 1:
            return hand_types[4]
        elif joker_mode and j_count == 2:
            return hand_types[5]
        return hand_types[2]
    elif card_dist_sorted == [3, 1, 1]:
        if joker_mode and j_count >= 1:
            return hand_types[5]
        return hand_types[3]
    elif card_dist_sorted == [3, 2]:
        if joker_mode and j_count >= 2:
            return hand_types[6]
        return hand_types[4]
    elif card_dist_sorted == [4, 1]:
        if joker_mode and j_count >= 1:
            return hand_types[6]
        return hand_types[5]
    elif card_dist_sorted == [5]:
        return hand_types[6]
    else:
        if joker_mode and j_count == 1:
            return hand_types[1]
        return hand_types[0]


def solve(text: str, joker_mode=False):
    hands = [
        (hand, get_hand_type(hand, joker_mode), bid)
        for line in text.splitlines()
        for hand, bid in [line.split(" ")]
    ]
    hands.sort(
        key=lambda x: (
            hand_types.index(x[1]),
            [
                card_values_2.index(c) if joker_mode else card_values.index(c)
                for c in x[0]
            ],
        )
    )
    return sum(int(h[2]) * (idx + 1) for idx, h in enumerate(hands))


def solve_part_1(text: str):
    return solve(text, False)


def solve_part_2(text: str):
    return solve(text, True)


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
