import time
from collections import defaultdict


def parse_map(text: str):
    map, instructions = text.split("\n\n")
    map = defaultdict(str) | {
        (y + x * 1j): c
        for y, line in enumerate(map.splitlines())
        for x, c in enumerate(line)
    }
    instructions = [
        {"^": -1, ">": 1j, "v": 1, "<": -1j}[instruction]
        for instruction in instructions.replace("\n", "")
    ]
    return map, instructions


def simulate(map, instructions):
    pos = next(k for k, v in map.items() if v == "@")
    for inst in instructions:
        to_move = []
        path = [pos]
        while path:
            pos = path.pop()
            if map[pos] in ["#", ""]:
                break
            elif map[pos] != ".":
                to_move.append(pos)
                np = pos + inst
                path.append(np)
                if not inst.imag and map[np] == "[":
                    path.append(np + 1j)
                if not inst.imag and map[np] == "]":
                    path.append(np - 1j)
        else:
            seen = set()
            for pos in reversed(to_move):
                if pos not in seen:
                    seen.add(pos)
                    map[pos], map[pos + inst] = map[pos + inst], map[pos]
            pos += inst


def solve_part_1(text: str):
    map, instructions = parse_map(text)
    simulate(map, instructions)
    return sum(n.real * 100 + n.imag for n in map if map[n] == "O")


def solve_part_2(text: str):
    map, instructions = parse_map(
        text.replace("O", "[]").replace(".", "..").replace("#", "##").replace("@", "@.")
    )
    simulate(map, instructions)
    return sum(n.real * 100 + n.imag for n in map if map[n] == "[")


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
