from collections import Counter
import re
import time


def iterate_robot(x, y, vx, vy, steps, max_x, max_y):
    for _ in range(steps):
        x = ((x + vx) + (2 * max_x)) % max_x
        y = ((y + vy) + (2 * max_y)) % max_y
    return x, y


def solve_part_1(text: str, max_w, max_h):
    robots = [
        tuple(list(map(int, re.findall(r"-?\d+", line)))) for line in text.splitlines()
    ]
    print(robots, max_w, max_h)
    max_w_h = max_w // 2
    max_h_h = max_h // 2

    tl, tr, bl, br = 0, 0, 0, 0

    for robot in robots:
        x, y = iterate_robot(robot[0], robot[1], robot[2], robot[3], 100, max_w, max_h)
        if x < max_w_h and y < max_h_h:
            tl += 1
        elif x > max_w_h and y < max_h_h:
            tr += 1
        elif x < max_w_h and y > max_h_h:
            bl += 1
        elif x > max_w_h and y > max_h_h:
            br += 1

    print(tl, tr, bl, br)

    return tl * tr * bl * br


def solve_part_2(text: str, max_w, max_h):
    robots = [
        tuple(list(map(int, re.findall(r"-?\d+", line)))) for line in text.splitlines()
    ]
    seconds_elapsed = 0

    def iterate_all_robots():
        next_robots = []
        for robot in robots:
            x, y = iterate_robot(robot[0], robot[1], robot[2], robot[3], 1, 101, 103)
            next_robots.append((x, y, robot[2], robot[3]))
        return next_robots

    def draw_robots():
        # draw robots on a grid and print it to console
        xy_counter = Counter([(robot[0], robot[1]) for robot in robots])
        # draw the number of bots at each position and . if no bots on this coordinates
        for y in range(max_h):
            line = ""
            for x in range(max_w):
                line += str(xy_counter[(x, y)]) if (x, y) in xy_counter else "."
            print(line)

    def is_finished():
        # calculate variance of all x and y coordinates
        variance = 0
        for robot in robots:
            variance += (robot[0] - max_w // 2) ** 2 + (robot[1] - max_h // 2) ** 2

        if variance > 600000:
            # if variance is this high, we don't even have to visually check if there is a christmas tree
            return False

        draw_robots()

        return (
            input(
                f"[{seconds_elapsed:04d}, {variance:.3f}] . Press y to continue or n to stop: "
            )
            == "y"
        )

    while not is_finished():
        robots = iterate_all_robots()
        seconds_elapsed += 1

    print(seconds_elapsed)

    return seconds_elapsed


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = int(solve_part_1(quiz_input, 101, 103))
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
        p_2_solution = int(solve_part_2(quiz_input, 101, 103))
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
