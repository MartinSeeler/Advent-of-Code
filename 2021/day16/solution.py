from functools import reduce
from operator import mul
import time

OPS = [
    sum,
    lambda x: reduce(mul, x),
    min,
    max,
    None,
    lambda x: int(x[0] > x[1]),
    lambda x: int(x[0] < x[1]),
    lambda x: int(x[0] == x[1]),
]


def parse_packets(input: str):
    data = bin(int("1" + input.strip(), 16))[3:]
    pos = 0
    versions = 0

    def read(n):
        nonlocal pos
        pos += n
        return int(data[pos - n : pos], 2)

    def readpacket():
        nonlocal versions
        versions += read(3)
        tid = read(3)
        if tid == 4:
            v = 0
            while True:
                flag = read(1)
                v = (v << 4) + read(4)
                if flag == 0:
                    return v
        vals = []
        if read(1) == 0:
            n = read(15)
            limit = pos + n
            while pos < limit:
                vals.append(readpacket())
        else:
            vals = [readpacket() for i in range(read(11))]
        return OPS[tid](vals)

    eval_res = readpacket()
    return eval_res, versions


def solve_part_1(text: str):
    _, versions = parse_packets(text)
    return versions


def solve_part_2(text: str):
    res, _ = parse_packets(text)
    return res


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
