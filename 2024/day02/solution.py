import time


def parse_reports(text: str) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in text.split("\n") if line.strip()]


def is_safe(xs: list[int]) -> bool:
    diffs = [(xs[i + 1] - xs[i]) for i in range(len(xs) - 1)]
    increasing = all(d >= 1 and d <= 3 for d in diffs)
    decreasing = all(d <= -1 and d >= -3 for d in diffs)
    return increasing or decreasing


def solve_part_1(text: str):
    reports = parse_reports(text)
    safe_reports = [report for report in reports if is_safe(report)]
    return len(safe_reports)


def solve_part_2(text: str):
    reports = parse_reports(text)
    safe_count = 0
    for report in reports:
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1 :]
            if is_safe(new_report):
                safe_count += 1

    return safe_count


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
