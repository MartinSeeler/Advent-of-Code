import time

dirs = ["^", "v", "<", ">"]
dirs_offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def move(pos: tuple[int, int], map: dict[tuple[int, int], str], direction: str):
    if pos not in map:
        return pos, map
    dir_offset = dirs_offset[dirs.index(direction)]
    new_pos = (pos[0] + dir_offset[0], pos[1] + dir_offset[1])
    if new_pos in map and map[new_pos] == "#":
        return pos, map
    if new_pos in map and map[new_pos] != "#":
        nnew_pos, map = move(new_pos, map, direction)
        if nnew_pos == new_pos:
            return pos, map
    map[new_pos] = map[pos]
    del map[pos]
    return new_pos, map


def print_map(map: dict[tuple[int, int], str]):
    min_x = min([pos[0] for pos in map.keys()])
    max_x = max([pos[0] for pos in map.keys()])
    min_y = min([pos[1] for pos in map.keys()])
    max_y = max([pos[1] for pos in map.keys()])

    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in map:
                line += map[(x, y)]
            else:
                line += "."
        print(line)
    print()


def solve_part_1(text: str):
    map_view, instructions = text.split("\n\n")
    instructions = instructions.replace("\n", "")

    robot = (0, 0)
    map = dict()
    for y, line in enumerate(map_view.split("\n")):
        for x, char in enumerate(line):
            if char == "@":
                robot = (x, y)
            if char != ".":
                map[(x, y)] = char

    for i in instructions:
        robot, map = move(robot, map, i)
    print_map(map)
    # find all boxes coordinates ('0''s)
    boxes = [(x, y) for (x, y) in map.keys() if map[(x, y)] == "O"]

    return sum([100 * y + x for x, y in boxes])


def solve_part_2(text: str):
    pass


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
