def match(s, rem, rs):
  lr, ls = len(rem), len(s)
  if lr > ls:
    return False
  elif lr * ls == 0:
    return (lr, ls) == (0, 0)
  if isinstance(rem[-1], str):
    return match(s[1:], rem[:-1], rs) if s[0] == rem[-1] else False
  for r in rs[rem[-1]]:
    if match(s, rem[:-1] + list(r[::-1]), rs):
      return True


def count_matches(rules, samples) -> int:
  return sum([1 if match(s, rules[0][0][::-1], rules) else 0 for s in samples])


def parse(text: str):
  rule_lines, samples = tuple(map(lambda x: x.splitlines(), text.split('\n\n')))
  rules = {}
  for rl in rule_lines:
    k, path = rl.split(': ')
    rules[int(k)] = path[1] if path[0] == '"' else list(map(lambda x: list(map(int, x.split(' '))), path.split(' | ')))
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
