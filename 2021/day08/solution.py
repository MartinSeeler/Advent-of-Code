from collections import defaultdict
import time
import re


def decode(line: str) -> str:
    seqs = [frozenset(seq) for seq in re.findall(r"\w+", line)]
    one, seven, four, *remaining, eight = sorted(set(seqs), key=len)
    (three,) = [x for x in remaining if len(x - one) == 3]
    (zero,) = [x for x in remaining if x == (eight - four) | one | (eight - three)]
    (six,) = [x for x in remaining if len(eight - x) == 1 and len(x & one) == 1]
    (five,) = [x for x in remaining if x <= six and len(six - x) == 1]
    (two,) = [x for x in remaining if len(x - five) == 2 and len(x & five) == 3]
    (nine,) = [x for x in remaining if x == eight - (six - five)]
    lookup = {
        d: str(i)
        for i, d in enumerate(
            [zero, one, two, three, four, five, six, seven, eight, nine]
        )
    }
    return "".join(lookup[x] for x in seqs[-4:])


def solve_part_1(text: str):
    return sum(
        len(list(filter(lambda y: y in ["1", "4", "7", "8"], x)))
        for x in map(decode, text.splitlines())
    )


def solve_part_2(text: str):
    return sum(int(x) for x in map(decode, text.splitlines()))


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
