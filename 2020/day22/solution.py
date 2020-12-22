from collections import Counter
import sys

sys.setrecursionlimit(100500)

def parse_cards(text: str) -> ([], []):
  return list(list(xs.splitlines()[1:]) for xs in text.split("\n\n"))


def play_round(p1, p2):
  if len(p1) == 0:
    return 1, p2
  if len(p2) == 0:
    return 0, p1
  print(f"Player 1's deck: {', '.join(p1)}")
  print(f"Player 2's deck: {', '.join(p2)}")
  print(f"Player 1 plays: {p1[0]}")
  print(f"Player 2 plays: {p2[0]}")
  if int(p1[0]) > int(p2[0]):
    print("Player 1 wins the round!")
    return play_round(p1[1:] + [p1[0]] + [p2[0]], p2[1:])
  else:
    print("Player 2 wins the round!")
    return play_round(p1[1:], p2[1:] + [p2[0]] + [p1[0]])


def play_round_rec(p1, p2, c=Counter()):
  if len(p1) == 0:
    return 1, p2
  if len(p2) == 0:
    return 0, p1
  round_key = f"{', '.join(p1)}-{', '.join(p2)}"
  if c[round_key] > 0:
    print(f"Round key {round_key} was met before")
    return 0, p1
  c[round_key] += 1
  print(f"Player 1's deck: {', '.join(p1)}")
  print(f"Player 2's deck: {', '.join(p2)}")
  print(f"Player 1 plays: {p1[0]}")
  print(f"Player 2 plays: {p2[0]}")
  if (len(p1[1:]) >= int(p1[0])) and (len(p2[1:]) >= int(p2[0])):
    print("Playing sub round")
    winner_id, winner_deck = play_round_rec(p1[1:int(p1[0])+1], p2[1:int(p2[0])+1], Counter())
    print("Winner rec", winner_id)
    if winner_id:
      print("Player 2 wins the round!")
      return play_round_rec(p1[1:], p2[1:] + [p2[0]] + [p1[0]], c)
    else:
      print("Player 1 wins the round!")
      return play_round_rec(p1[1:] + [p1[0]] + [p2[0]], p2[1:], c)
  elif int(p1[0]) > int(p2[0]):
    print("Player 1 wins the round!")
    return play_round_rec(p1[1:] + [p1[0]] + [p2[0]], p2[1:], c)
  else:
    print("Player 2 wins the round!")
    return play_round_rec(p1[1:], p2[1:] + [p2[0]] + [p1[0]], c)


def calc_score(cards: [], score=0, idx=1) -> int:
  if len(cards) == 0:
    return score
  else:
    return calc_score(cards[:-1], score=score + (idx * int(cards[-1])), idx=idx + 1)


def solve_part_1(text: str):
  (p1, p2) = parse_cards(text)
  winner_id, winner_deck = play_round(p1, p2)
  return calc_score(winner_deck)


def solve_part_2(text: str):
  (p1, p2) = parse_cards(text)
  winner_id, winner_deck = play_round_rec(p1, p2)
  return calc_score(winner_deck)


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    # print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
