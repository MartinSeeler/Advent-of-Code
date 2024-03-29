import time


def solve(top_section: str, bottom_section: str):
    dots = set()
    for line in top_section.splitlines():
        x, y = list(map(int, line.split(",")))
        dots.add(complex(x, y))
    for line in bottom_section.splitlines():
        axis, x = line.split(" ")[2].split("=")
        x = int(x)
        if axis == "y":
            belows = set(filter(lambda d: d.imag > x, dots))
            dots -= belows
            for b in belows:
                dots.add(complex(b.real, x - (b.imag - x)))
        else:
            rights = set(filter(lambda d: d.real > x, dots))
            dots -= rights
            for r in rights:
                dots.add(complex(x - (r.real - x), r.imag))
    return dots


def solve_part_1(text: str):
    top_section, bottom_section = text.split("\n\n")
    return len(solve(top_section, bottom_section.split("\n")[0]))


def solve_part_2(text: str):
    top_section, bottom_section = text.split("\n\n")
    dots = solve(top_section, bottom_section)
    for y in range(0, 6):
        print("".join(["#" if complex(x, y) in dots else " " for x in range(0, 39)]))
    return len(dots)


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
