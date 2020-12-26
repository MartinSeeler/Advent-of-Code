import re

two_same_chars = re.compile(r"(\w)\1+")
vovel = re.compile(r"([aeiou])")


def is_nice(text: str) -> bool:
  return all([x not in text for x in ["ab", "cd", "pq", "xy"]]) and (len(re.findall(two_same_chars, text)) > 0) and (
        len(re.findall(vovel, text)) >= 3)


def solve_part_1(text: str) -> int:
  return sum(map(is_nice, text.splitlines()))


def solve_part_2(text: str):
  pass


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
