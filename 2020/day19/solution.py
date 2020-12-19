def match(sample, current, rs):
  if len(current) > len(sample):
    return False
  elif len(current) == 0 or len(sample) == 0:
    # end reached
    return len(current) == 0 and len(sample) == 0

  c = current.pop()
  if isinstance(c, str):
    if sample[0] == c:
      return match(sample[1:], current.copy(), rs)
  else:
    for r in rs[c]:
      if match(sample, current + list(reversed(r)), rs):
        return True
  return False


def count_matches(rules, samples) -> int:
  return sum([1 if match(s, list(reversed(rules[0][0])), rules) else 0 for s in samples])


def parse(text: str):
  rule_lines, samples = tuple(map(lambda x: x.splitlines(), text.split('\n\n')))
  rules = {}
  for rl in rule_lines:
    k, path = rl.split(': ')
    if path[0] == '"':
      rules[int(k)] = path[1]
    else:
      rules[int(k)] = list(map(lambda x: list(map(int, x.split(' '))), path.split(' | ')))
  return rules, samples


def solve_part_1(text: str) -> int:
  return count_matches(*parse(text))


def solve_part_2(text: str):
  return count_matches(*parse(text))


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
  with open("input2.txt", "r") as f:
    quiz_input = f.read()
    print("Part 2:", solve_part_2(quiz_input))
