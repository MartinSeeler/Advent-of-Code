from itertools import combinations


def find_solutions(inputs, target_sum, n=2):
  for xs in combinations(inputs, n):
    if sum(xs) == target_sum:
      yield xs


def solve_part_1(text: str):
  input_list = [int(x) for x in text.splitlines()]
  res = next(find_solutions(input_list, 2020, 2))
  return res[0] * res[1]


def solve_part_2(text: str):
  input_list = [int(x) for x in text.splitlines()]
  res = next(find_solutions(input_list, 2020, 3))
  return res[0] * res[1] * res[2]


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
