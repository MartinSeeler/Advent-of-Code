import re
from math import prod


def parse_content(text: str):
  re_field_range = r"([\w\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)"
  re_values = r"^\d+,[\d+,?]+"
  rules = {}
  all_tickets = []
  for line in text.splitlines():
    fields = re.findall(re_field_range, line)
    if len(fields) > 0:
      rules[fields[0][0]] = [int(x) for x in fields[0][1:]]
    ticket_matches = re.findall(re_values, line, re.M)
    if len(ticket_matches) > 0:
      all_tickets.append([int(x) for x in ticket_matches[0].split(",")])
  my_ticket = all_tickets[0]
  nearby_tickets = all_tickets[1:]
  return rules, my_ticket, nearby_tickets


def solve_part_1(text: str):
  rules, my_ticket, nearby_tickets = parse_content(text)
  s = 0
  for t in nearby_tickets:
    for v in t:
      invalid = all(not (rs[0] <= v <= rs[1] or rs[2] <= v <= rs[3]) for rs in rules.values())
      if invalid:
        s += v
  return s


def solve_part_2(text: str):
  rules, my_ticket, nearby_tickets = parse_content(text)
  valid_ticket = list(filter(
    lambda t: not (any([all(not (rs[0] <= v <= rs[1] or rs[2] <= v <= rs[3]) for rs in rules.values()) for v in t])),
    nearby_tickets))
  possible_mappings = {}
  for idx in range(len(my_ticket)):
    possible = []
    for k, rs in rules.items():
      if all([rs[0] <= vt[idx] <= rs[1] or rs[2] <= vt[idx] <= rs[3] for vt in valid_ticket]):
        possible.append(k)
    possible_mappings[idx] = set(possible)
  mapping = list([None for _ in range(len(my_ticket))])
  for _ in range(len(my_ticket)):
    for k, pi in possible_mappings.items():
      if len(pi) == 1:
        field = list(pi)[0]
        mapping[k] = field
        for j, pis in possible_mappings.items():
          pis.discard(field)
          possible_mappings[j] = pis
        break
  return prod([my_ticket[idx] for idx, x in enumerate(mapping) if x.startswith("departure")])


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
