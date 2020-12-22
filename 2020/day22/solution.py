from typing import Deque, List


def parse_decks(text: str) -> [List[int], List[int]]:
  return [list(int(x) for x in xs.splitlines()[1:]) for xs in text.split("\n\n")]


def play_round_1(p1: List[int], p2: List[int]) -> (int, Deque[int]):
  while p1 and p2:
    h1, h2 = p1[0], p2[0]
    p1, p2 = p1[1:], p2[1:]
    if h1 > h2:
      p1 += [h1, h2]
    else:
      p2 += [h2, h1]
  return (0, p1) if p1 else (1, p2)


def play_round_2(p1: List[int], p2: List[int]) -> (int, Deque[int]):
  used = set()
  while p1 and p2:
    key = str(p1) + "|" + str(p2)
    if key in used:
      return 1, p2
    used.add(key)

    h1, h2 = p1[0], p2[0]
    p1, p2 = p1[1:], p2[1:]

    if len(p1) < h1 or len(p2) < h2:
      if h1 > h2:
        p1 += [h1, h2]
      else:
        p2 += [h2, h1]
    else:
      winner, _ = play_round_2(p1[:h1], p2[:h2])
      if winner == 1:
        p1 += [h1, h2]
      else:
        p2 += [h2, h1]
  return (1, p1) if len(p1) > 0 else (2, p2)


def calc_score(deck: List[int]) -> int:
  return sum((i + 1) * v for i, v in enumerate(reversed(deck)))


def solve_part_1(text: str):
  (p1, p2) = parse_decks(text)
  _, winner_deck = play_round_1(p1, p2)
  return calc_score(winner_deck)


def solve_part_2(text: str):
  (p1, p2) = parse_decks(text)
  _, winner_deck = play_round_2(p1, p2)
  return calc_score(winner_deck)


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
