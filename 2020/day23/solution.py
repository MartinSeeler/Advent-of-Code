from typing import List
from itertools import dropwhile


def play(cups: List[int], games_to_play: int):
  nodes: List[(int, int)] = list(zip(cups, list(range(1, len(cups))) + [0]))
  idx = lambda node: node[1]
  val = lambda node: node[0]
  walk = lambda node, n=1: nodes[idx(node)] if n <= 1 else walk(nodes[idx(node)], n - 1)
  # this breaks part 2...
  find = lambda v: next(dropwhile(lambda x: val(x[1]) != v, enumerate(nodes)))

  def acc(from_idx):
    res = [val(nodes[from_idx])]
    current_idx = idx(nodes[from_idx])
    while current_idx != from_idx and len(res) <= len(nodes):
      res.append(val(nodes[current_idx]))
      current_idx = idx(nodes[current_idx])
    return res

  current_idx = 0
  for r in range(games_to_play):
    picked_up = list(
      map(find, [val(walk(nodes[current_idx])), val(walk(nodes[current_idx], 2)), val(walk(nodes[current_idx], 3))]))
    nodes[current_idx] = (val(nodes[current_idx]), idx(picked_up[-1][1]))
    dest_val = (val(nodes[current_idx]) - 1) or len(nodes)
    while dest_val in [val(x[1]) for x in picked_up]:
      dest_val = (dest_val - 1) or len(nodes)
    dest_idx, dest_node = find(dest_val)
    nodes[picked_up[-1][0]] = (val(picked_up[-1][1]), idx(dest_node))
    nodes[dest_idx] = (val(dest_node), picked_up[0][0])
    current_idx = idx(nodes[current_idx])
  dest_idx, dest_node = find(1)
  return acc(dest_idx)


class Node:
  def __init__(self, value, right=None):
    self.value = value
    self.right = right


def play_linked_list(cups: List[int], games_to_play: int):
  nm = {}
  prev = None
  for c in cups:
    node = Node(c)
    nm[c] = node
    if prev:
      prev.right = node
    prev = node
  prev.right = nm[cups[0]]
  n = None
  for i in range(games_to_play):
    n = n.right if n else nm[cups[0]]
    picked_up = [n.right, n.right.right, n.right.right.right]
    n.right = picked_up[-1].right
    d_value = n.value - 1 or len(cups)
    while nm[d_value] in picked_up:
      d_value = d_value - 1 or len(cups)
    destination = nm[d_value]
    picked_up[-1].right = destination.right
    destination.right = picked_up[0]
  return nm


def parse(text: str) -> List[int]:
  return [int(x) for x in text]


def solve_part_1(text: str, rounds: int):
  return ''.join(map(str, play(parse(text), rounds)))[1:]


def solve_part_2(text: str, rounds: int):
  cups = parse(text)
  cups = cups + [i for i in range(len(cups) + 1, 1000001)]
  node_map = play_linked_list(cups, rounds)
  return node_map[1].right.value * node_map[1].right.right.value


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input, 100))
    print("Part 2:", solve_part_2(quiz_input, 10000000))
