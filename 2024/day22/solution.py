import time

N = 2000


def next_secret(s):
    """3-step pseudorandom transformation for a 24-bit integer."""
    s = (s ^ ((s << 6) & 0xFFFFFF)) & 0xFFFFFF
    s = (s ^ (s >> 5)) & 0xFFFFFF
    s = (s ^ ((s << 11) & 0xFFFFFF)) & 0xFFFFFF
    return s


def pack_diffs_into_key(d0, d1, d2, d3):
    """
    Each diff is offset by +9 to fit into [0..18] (5 bits each).
    Combine them into a single 20-bit integer.
    """
    return (d0 << 15) | (d1 << 10) | (d2 << 5) | d3


def solve_part_1(text: str):
    buyers = map(int, text.splitlines())
    total = 0
    for secret in buyers:
        for _ in range(N):
            secret = next_secret(secret)
        total += secret
    return total


def solve_part_2(text: str):
    buyers = list(map(int, text.splitlines()))
    size = 1 << 20  # total possible 4-diff combinations
    seen = [0] * size
    results = [0] * size
    buyer_id = 1

    secrets_arr = [0] * (N + 1)
    prices_arr = [0] * (N + 1)
    deltas_arr = [0] * (N + 1)

    for secret_number in buyers:
        # Fill arrays with generated secrets, prices, and deltas
        secrets_arr[0] = secret_number
        prices_arr[0] = secrets_arr[0] % 10
        for i in range(1, N + 1):
            secrets_arr[i] = next_secret(secrets_arr[i - 1])
            prices_arr[i] = secrets_arr[i] % 10
            deltas_arr[i] = prices_arr[i] - prices_arr[i - 1]

        # From index 4 onward, we have a valid window of 4 consecutive deltas
        for i in range(4, N + 1):
            # We gather the 4 consecutive deltas leading to prices_arr[i].
            d0 = deltas_arr[i - 3] + 9
            d1 = deltas_arr[i - 2] + 9
            d2 = deltas_arr[i - 1] + 9
            d3 = deltas_arr[i] + 9
            key = pack_diffs_into_key(d0, d1, d2, d3)

            # Only record the first time this buyer sees this pattern
            if seen[key] != buyer_id:
                seen[key] = buyer_id
                results[key] += prices_arr[i]

        buyer_id += 1

    return max(results)


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
