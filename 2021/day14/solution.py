from collections import Counter, defaultdict
import time


def play(text: str, rounds: int):
    template, _, *subs = text.split("\n")
    subs = dict(s.split(" -> ") for s in subs)

    combis = Counter()
    combis.update([x + y for x, y in zip(template, template[1:])])
    for _ in range(rounds):
        combis_in_this_round = combis.copy().items()
        for (a, b), c in combis_in_this_round:
            combis[a + b] -= c
            combis[a + subs[a + b]] += c
            combis[subs[a + b] + b] += c
    chars = Counter()
    chars[template[0]] = 1
    for (_, r), count in combis.items():
        chars[r] += count
    char_values = chars.values()
    return max(char_values) - min(char_values)


def solve_part_1(text: str):
    return play(text, 10)


def solve_part_2(text: str):
    return play(text, 40)


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
