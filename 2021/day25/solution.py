import time


def parse(text: str):
    rights = set()
    downs = set()
    W = len(text.splitlines()[0])
    H = len(text.splitlines())
    for y, line in enumerate(text.splitlines()):
        for x, c in enumerate(line):
            if c == ">":
                rights.add(complex(x, y))
            elif c == "v":
                downs.add(complex(x, y))
    return W, H, rights, downs


def iter(rights, downs, W, H):
    new_rights = set()
    new_downs = set()
    for r in rights:
        r_n = complex(r.real + 1 if r.real < W - 1 else 0, r.imag)
        new_rights.add(r_n if r_n not in rights and r_n not in downs else r)
    for d in downs:
        d_n = complex(d.real, d.imag + 1 if d.imag < H - 1 else 0)
        new_downs.add(d_n if d_n not in new_rights and d_n not in downs else d)
    return new_rights, new_downs


def solve_part_1(text: str):
    W, H, rights, downs = parse(text)
    turn = 0
    equals = False
    while not equals:
        new_rights, new_downs = iter(rights, downs, W, H)
        if new_rights == rights and new_downs == downs:
            equals = True
        else:
            rights = new_rights
            downs = new_downs
        turn += 1
    return turn


def solve_part_2(text: str):
    return 0


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
