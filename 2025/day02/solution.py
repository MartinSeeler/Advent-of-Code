import time
from pathlib import Path
from typing import Iterable


def parse_ranges(text: str) -> list[tuple[int, int]]:
    """Parse 'start-end,start-end,...' into list of (start, end) tuples."""
    return [
        (int(parts[0]), int(parts[1]))
        for pair in text.strip().split(",")
        for parts in [pair.split("-")]
    ]


def repeating_multiplier(pattern_len: int, repetitions: int) -> int:
    """
    Calculate multiplier for a pattern of length L repeated k times.
    E.g., pattern "12" (len=2) repeated 3 times: 12 × 10101 = 121212
    Formula: (10^(L×k) - 1) / (10^L - 1)
    """
    base = 10 ** pattern_len
    return (base ** repetitions - 1) // (base - 1)


def arithmetic_sum(start: int, end: int) -> int:
    if start > end:
        return 0
    count = end - start + 1
    return (start + end) * count // 2


def valid_base_range(
    pattern_len: int, 
    multiplier: int, 
    range_start: int, 
    range_end: int
) -> tuple[int, int]:
    # Base must have exactly pattern_len digits
    digit_min = 10 ** (pattern_len - 1) if pattern_len > 1 else 1
    digit_max = 10 ** pattern_len - 1
    
    range_min = -(-range_start // multiplier)  # ceiling division
    range_max = range_end // multiplier
    
    return (max(digit_min, range_min), min(digit_max, range_max))


def solve_part_1(text: str) -> int:
    total = 0
    
    for start, end in parse_ranges(text):
        min_digits = len(str(start))
        max_digits = len(str(end))
        
        for total_digits in range(min_digits, max_digits + 1):
            if total_digits % 2 != 0:
                continue
            
            half = total_digits // 2
            multiplier = 10 ** half + 1  # e.g., 101 for 4-digit numbers
            
            base_min, base_max = valid_base_range(half, multiplier, start, end)
            
            # Sum: multiplier × (base_min + base_min+1 + ... + base_max)
            total += multiplier * arithmetic_sum(base_min, base_max)
    
    return total


def generate_repeating_numbers(
    start: int, 
    end: int, 
    pattern_len: int, 
    repetitions: int
) -> Iterable[int]:
    multiplier = repeating_multiplier(pattern_len, repetitions)
    base_min, base_max = valid_base_range(pattern_len, multiplier, start, end)
    
    return (base * multiplier for base in range(base_min, base_max + 1))


def solve_part_2(text: str) -> int:
    result: set[int] = set()
    
    for start, end in parse_ranges(text):
        min_digits = len(str(start))
        max_digits = len(str(end))
        
        for total_digits in range(min_digits, max_digits + 1):
            # Check all pattern lengths that divide total_digits
            for pattern_len in range(1, total_digits):
                repetitions, remainder = divmod(total_digits, pattern_len)
                
                if remainder != 0 or repetitions < 2:
                    continue
                
                result.update(
                    generate_repeating_numbers(start, end, pattern_len, repetitions)
                )
    
    return sum(result)


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
