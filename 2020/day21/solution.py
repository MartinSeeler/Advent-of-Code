from collections import defaultdict
from functools import reduce


def parse(text: str):
  possible_mapping = {}
  counter = defaultdict(lambda: 0)
  for line in text.splitlines():
    parts = line.split(" (contains")
    ingredients, alergens = parts[0].strip().split(" "), parts[1][:-1].strip().split(", ")
    for i in ingredients:
      counter[i] += 1
    for al in alergens:
      if al in possible_mapping:
        possible_mapping[al] &= set(ingredients)
      else:
        possible_mapping[al] = set(ingredients)
  return possible_mapping, counter


def solve_part_1(text: str):
  possible_mapping, counter = parse(text)
  return sum(
    counter[k] for k in (set(counter.keys()) - reduce(lambda x, y: set.union(x, y), possible_mapping.values())))


def solve_part_2(text: str):
  possible_mapping, _ = parse(text)
  final = {}
  while len(possible_mapping) > 0:
    for k in list(possible_mapping.keys()):
      if len(possible_mapping[k]) == 1:
        final[k] = possible_mapping[k].pop()
        possible_mapping.pop(k)
        for j, vs in possible_mapping.items():
          if j in possible_mapping.keys():
            possible_mapping[j].discard(final[k])
  return ",".join([final[k] for k in sorted(final.keys())])


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
