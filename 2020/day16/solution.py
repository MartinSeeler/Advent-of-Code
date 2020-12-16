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


in_range = lambda v, rs: rs[0] <= v <= rs[1] or rs[2] <= v <= rs[3]


def solve_part_1(text: str):
  rules, my_ticket, nearby_tickets = parse_content(text)
  return sum([v for t in nearby_tickets for v in t
              if all(not in_range(v, rs) for rs in rules.values())])


def solve_part_2(text: str):
  rules, my_ticket, nearby_tickets = parse_content(text)
  valid_ticket = list(filter(
    lambda t: not (any([all(not in_range(v, rs) for rs in rules.values()) for v in t])),
    nearby_tickets))
  possible_mappings = {}
  for idx in range(len(my_ticket)):
    possible_mappings[idx] = set([k for k, rs in rules.items() if
                                  all([in_range(vt[idx], rs) for vt in valid_ticket])])
  mapping = list([None for _ in range(len(my_ticket))])
  for _ in range(len(my_ticket)):
    for m_idx, possible_idxs in possible_mappings.items():
      if len(possible_idxs) == 1:
        field = list(possible_idxs)[0]
        mapping[m_idx] = field
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
