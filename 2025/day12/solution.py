import time
from pathlib import Path


def parse_input(text: str):
    """Parse input into shape areas and regions."""
    chunks = text.replace(":", "").replace("x", " ").split("\n\n")
    regions_text = chunks.pop()

    # Get area (count of #) for each shape
    areas = [chunk.count("#") for chunk in chunks]

    # Parse regions
    regions = []
    for line in regions_text.strip().splitlines():
        parts = list(map(int, line.split()))
        w, h = parts[0], parts[1]
        counts = parts[2:]
        regions.append((w, h, counts))

    return areas, regions


def solve_part_1(text: str):
    areas, regions = parse_input(text)
    count = 0
    for w, h, counts in regions:
        area_needed = sum(areas[i] * c for i, c in enumerate(counts))
        if area_needed <= w * h:
            count += 1
    return count


def solve_part_2(text: str):
    pass


if __name__ == '__main__':
  with open(Path(__file__).parent / "input.txt", "r") as f:
    quiz_input = f.read()
    start = time.time()
    p_1_solution = int(solve_part_1(quiz_input))
    middle = time.time()
    print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
    p_2_solution = int(solve_part_2(quiz_input))
    end = time.time()
    print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
