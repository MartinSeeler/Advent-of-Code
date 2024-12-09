import time

# why not use '.'? Because we're working with chr() and ord() of indices, and since ord('.') is 46, it would fail.
# This one looks like an empty space and it's ord is high enough to be used as a placeholder.
FREE_CHAR = "🫥"


def parse_disk(text: str) -> list:
    digits = map(int, text)
    disk = []
    expect_file_segment = True
    file_id = 0
    for digit in digits:
        if expect_file_segment:
            disk.extend(chr(file_id) for _ in range(digit))
            file_id += 1
        else:
            disk.extend(FREE_CHAR for _ in range(digit))
        expect_file_segment = not expect_file_segment
    return disk


def compute_checksum(disk: list) -> int:
    """Compute checksum by summing i * ord(block_id) for non-free blocks."""
    return sum(
        i * ord(block_id_char)
        for i, block_id_char in enumerate(disk)
        if block_id_char != FREE_CHAR
    )


def compact_disk_part1(disk: list) -> None:
    """Compaction method for part 1 logic."""
    first_dot = 0
    while True:
        # Remove trailing free spaces
        while disk and disk[-1] == FREE_CHAR:
            disk.pop()
        # Attempt to find the next free space from 'first_dot'
        try:
            first_dot = disk.index(FREE_CHAR, first_dot)
        except ValueError:
            # No more internal free spaces
            break
        # Replace that free space with the last file block
        disk[first_dot] = disk[-1]
        disk.pop()
    return disk


def compact_disk_part2(disk: list) -> None:
    """Compaction method for part 2 logic."""
    # Remove trailing free spaces
    while disk and disk[-1] == FREE_CHAR:
        disk.pop()

    # Identify file segments
    if not disk:
        return
    last_char = disk[0]
    length = 1
    files = []
    for i in range(1, len(disk)):
        if disk[i] != last_char:
            if last_char != FREE_CHAR:
                files.append(("".join(disk[i - length : i]), i - length))
            length = 1
            last_char = disk[i]
        else:
            length += 1
    if last_char != FREE_CHAR:
        files.append(("".join(disk[len(disk) - length :]), len(disk) - length))

    disk_str = "".join(disk)
    while files:
        file_blocks, file_start = files.pop()
        flen = len(file_blocks)
        free_segment = FREE_CHAR * flen
        try:
            first_slot = disk_str.index(free_segment, 0, file_start)
        except ValueError:
            continue
        # Move the file
        disk_str = (
            disk_str[:first_slot]
            + file_blocks
            + disk_str[first_slot + flen : file_start]
            + free_segment
            + disk_str[file_start + flen :]
        )

    disk.clear()
    disk.extend(disk_str)
    return disk


def solve_part_1(text: str):
    return compute_checksum(compact_disk_part1(parse_disk(text)))


def solve_part_2(text: str):
    return compute_checksum(compact_disk_part2(parse_disk(text)))


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
