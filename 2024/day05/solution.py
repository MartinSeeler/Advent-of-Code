import time

from functools import cmp_to_key


def build_dependency_matrix(rules):
    n = 100  # Assuming pages are numbered from 0 to 99
    rules_matrix = [[False] * n for _ in range(n)]

    for rule in rules:
        x, y = map(int, rule.split("|"))
        rules_matrix[x][y] = True

    return rules_matrix


def is_valid_update(update, rules_matrix):
    for i in range(len(update) - 1):
        if not rules_matrix[update[i]][update[i + 1]]:
            return False
    return True


def sort_update(update, rules_matrix):
    def custom_compare(x, y):
        if rules_matrix[x][y]:
            return -1
        elif rules_matrix[y][x]:
            return 1
        else:
            return 0

    update.sort(key=cmp_to_key(custom_compare))
    return update


def find_middle_page(update):
    middle_index = (len(update) - 1) // 2
    return update[middle_index]


def solve_part_1(text: str):
    rules, updates = text.split("\n\n")
    rules = rules.split("\n")
    updates = [[int(x) for x in update.split(",")] for update in updates.split("\n")]

    # Build the dependency matrix
    rules_matrix = build_dependency_matrix(rules)

    middle_pages_sum = 0

    for update in updates:
        if is_valid_update(update, rules_matrix):
            middle_pages_sum += find_middle_page(update)

    return middle_pages_sum


def solve_part_2(text: str):
    rules, updates = text.split("\n\n")
    rules = rules.split("\n")
    updates = [[int(x) for x in update.split(",")] for update in updates.split("\n")]

    # Build the dependency matrix
    rules_matrix = build_dependency_matrix(rules)

    middle_pages_sum = 0

    for update in updates:
        if not is_valid_update(update, rules_matrix):
            sorted_update = sort_update(update[:], rules_matrix)
            middle_page = find_middle_page(sorted_update)
            middle_pages_sum += middle_page

    return middle_pages_sum


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
