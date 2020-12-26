import re

two_same_chars = re.compile(r"(\w)\1+")
vovel = re.compile(r"([aeiou])")
enclosed = re.compile(r"(\w).\1")
foo = re.compile(r"(\w{2}).*\1")


def is_nice(text: str) -> bool:
  return all([x not in text for x in ["ab", "cd", "pq", "xy"]]) and (len(re.findall(two_same_chars, text)) > 0) and (
      len(re.findall(vovel, text)) >= 3)


def is_nice2(text: str) -> bool:
  return len(re.findall(enclosed, text)) > 0 and len(re.findall(foo, text)) > 0


def solve_part_1(text: str) -> int:
  return sum(map(is_nice, text.splitlines()))


def solve_part_2(text: str):
  return sum(map(is_nice2, text.splitlines()))


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
