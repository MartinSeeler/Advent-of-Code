from collections import defaultdict
import time
import re


def decode(line: str) -> str:
    res = ''
    (signals, values) = line.split('|')
    lens_dict = {len(x): set(x) for x in signals.split()}
    for parts in map(set, values.split()):
        match [len(parts&lens_dict[singles]) for singles in [7,2,4]]:
            case 2,_,_: res += '1'
            case 3,_,_: res += '7'
            case 4,_,_: res += '4'
            case 7,_,_: res += '8'
            case 5,1,2: res += '2'
            case 5,1,3: res += '5'
            case 5,2,3: res += '3'
            case 6,1,3: res += '6'
            case 6,2,3: res += '0'
            case 6,2,4: res += '9'
    return res


def solve_part_1(text: str):
    return len(list(filter(lambda x: x in ["1", "4", "7", "8"], "".join(map(decode, text.splitlines())))))


def solve_part_2(text: str):
    return sum(map(int, map(decode, text.splitlines())))


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
