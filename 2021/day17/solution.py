import re
import time


def solve_part_1(text: str):
    x1, x2, y1, y2 = list(map(int, re.findall("[-]?[0-9]+", text)))
    max_ys = []
    for y in range(y1, y2 + 1):
        for x in range(1, x2):
            pos = 0 + 0j
            velocity = complex(x, -y)
            max_y = 0
            has_hit = False
            while (pos.real < x2) and (pos.imag > y1):
                pos += velocity
                if x1 <= pos.real <= x2 and y1 <= pos.imag <= y2:
                    has_hit = True
                max_y = max(max_y, pos.imag)
                new_velo_x = max(velocity.real - 1, 0)
                new_velo_y = velocity.imag - 1
                velocity = complex(new_velo_x, new_velo_y)
            if has_hit:
                max_ys.append(max_y)
    return max(max_ys)


def solve_part_2(text: str):
    x1, x2, y1, y2 = list(map(int, re.findall("[-]?[0-9]+", text)))
    miny = min(y1, y2)
    velocs = set()
    for y in range(miny, -miny + 1):
        for x in range(1, x2 + 1):
            pos = 0 + 0j
            velocity = complex(x, -y)
            while (pos.real < x2) and (pos.imag > y1):
                pos += velocity
                if x1 <= pos.real <= x2 and y1 <= pos.imag <= y2:
                    velocs.add(complex(x, -y))
                new_velo_x = max(velocity.real - 1, 0)
                new_velo_y = velocity.imag - 1
                velocity = complex(new_velo_x, new_velo_y)
    return len(velocs)


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
