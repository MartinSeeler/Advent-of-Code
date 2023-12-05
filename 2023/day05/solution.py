import time


def parse_seeds(part):
    seeds = [int(x) for x in part.split(":")[1].strip().split(" ")]
    return seeds


def parse_seeds2(part):
    seeds = [int(x) for x in part.split(":")[1].strip().split(" ")]
    # make pairs of seed[0] and seed[1], seed[2] and seed[3], ...
    seeds = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]
    return seeds


def parse_mapping(part):
    mappings = []
    for line in part.splitlines()[1:]:
        numbers = [int(x) for x in line.split(" ") if x != ""]
        mappings.append(numbers)
    return mappings


def solve_part_1(text: str):
    parts = text.split("\n\n")
    seeds = parse_seeds(parts[0])
    mappings = [parse_mapping(part) for part in parts[1:]]
    min = 2**31 - 1
    for seed in seeds:
        path = [seed]
        for midx, mapping in enumerate(mappings):
            value = path[-1]
            for line in mapping:
                if value in range(line[1], line[1] + line[2]):
                    path.append(value + (line[0] - line[1]))
                    break
            if len(path) != midx + 2:
                path.append(value)
        if path[-1] < min:
            min = path[-1]
    # print(paths)
    return min


def solve_part_2(text: str):
    parts = text.split("\n\n")
    seed_ranges = parse_seeds2(parts[0])
    mappings = [parse_mapping(part) for part in parts[1:]]
    for mapping in mappings:
        next_ranges = []
        for dest, src, l in mapping:
            idx = 0
            while idx < len(seed_ranges):
                prt_src, prt_l = seed_ranges[idx]
                if src <= prt_src < src + l <= prt_src + prt_l:
                    next_ranges.append((prt_src - src + dest, src + l - prt_src))
                    seed_ranges[idx] = (src + l, prt_src + prt_l - src - l)
                elif prt_src <= src < prt_src + prt_l <= src + l:
                    next_ranges.append((dest, prt_src + prt_l - src))
                    seed_ranges[idx] = (prt_src, src - prt_src)
                elif prt_src <= src < src + l <= prt_src + prt_l:
                    next_ranges.append((dest, l))
                    seed_ranges[idx] = (prt_src, src - prt_src)
                    seed_ranges.append((src + l, prt_src + prt_l - src - l))
                if src <= prt_src < prt_src + prt_l <= src + l:
                    next_ranges.append((prt_src - src + dest, prt_l))
                    seed_ranges[idx] = seed_ranges[-1]
                    del seed_ranges[-1]
                else:
                    idx += 1
        seed_ranges += next_ranges
    return min(vbeg for vbeg, _ in seed_ranges)


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
