import time


def solve_part_1(text: str):
    word = "XMAS"
    matrix = [
        [x for x in line.strip()] for line in text.splitlines() if line.strip() != ""
    ]
    rows, cols = len(matrix), len(matrix[0])
    word_length = len(word)

    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1),  # Diagonal up-left
    ]

    def is_word_at(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or matrix[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_word_at(x, y, dx, dy):
                    count += 1

    return count


def solve_part_2(text: str):
    matrix = [
        [x for x in line.strip()] for line in text.splitlines() if line.strip() != ""
    ]
    rows, cols = len(matrix), len(matrix[0])
    count = 0

    def is_valid_combination(x, y):
        if y < 1 or y > cols - 2 or x < 1 or x >= rows - 2:
            return False

        tl = matrix[x - 1][y - 1]
        tr = matrix[x - 1][y + 1]
        bl = matrix[x + 1][y - 1]
        br = matrix[x + 1][y + 1]

        tl_br_valid = tl in {"M", "S"} and br in {"M", "S"} and tl != br
        tr_bl_valid = tr in {"M", "S"} and bl in {"M", "S"} and tr != bl

        return tl_br_valid and tr_bl_valid

    count = 0
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == "A":  # Only check around 'A'
                if is_valid_combination(x, y):
                    count += 1

    return count


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
