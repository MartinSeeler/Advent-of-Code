def solve_part_1(text: str):
    commands = text.splitlines()
    pos = 0 + 0j
    for command in commands:
        direction, steps = command.split()
        steps = int(steps)
        if direction == "forward":
            pos += steps
        elif direction == "up":
            pos -= steps * 1j
        elif direction == "down":
            pos += steps * 1j
        else:
            raise ValueError(f"Unknown direction {direction}")
    return pos.real * pos.imag


def solve_part_2(text: str):
    commands = text.splitlines()
    pos = 0 + 0j
    aim = 0
    for command in commands:
        direction, steps = command.split()
        steps = int(steps)
        if direction == "forward":
            pos += steps + (aim * steps * 1j)
        elif direction == "up":
            aim -= steps
        elif direction == "down":
            aim += steps
        else:
            raise ValueError(f"Unknown direction {direction}")
    return pos.real * pos.imag


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        print("Part 1:", solve_part_1(quiz_input))
        print("Part 2:", solve_part_2(quiz_input))
