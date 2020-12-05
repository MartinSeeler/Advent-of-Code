def split(xs, n):
    k, m = divmod(len(xs), n)
    return (xs[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

def get_path_by_pattern(pattern: str, xs: range, rhs_char: str):
    xs_rem = list(split(xs, 2))[pattern[0] == rhs_char]
    return xs_rem[0] if len(pattern) == 1 else get_path_by_pattern(pattern[1:], xs_rem, rhs_char)

def get_row(pattern: str):   
    return get_path_by_pattern(pattern, range(0, 128), 'B')

def get_column(pattern: str):
    return get_path_by_pattern(pattern, range(0, 8), 'R')

def get_seat_id(pattern: str):
    return get_row(pattern[:7]) * 8 + get_column(pattern[-3:])


input_list = []
with open("./input.txt", "r") as f:
    input_list = f.read().splitlines()

print(max(map(get_seat_id, input_list)))