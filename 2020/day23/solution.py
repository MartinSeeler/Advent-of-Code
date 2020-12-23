from typing import List
from itertools import dropwhile


def play(cups: List[int], games_to_play: int):
  # make linked list: (value, next_idx)
  nodes: List[(int, int)] = list(zip(cups, list(range(1, len(cups))) + [0]))
  idx = lambda node: node[1]
  val = lambda node: node[0]
  walk = lambda node, n=1: nodes[idx(node)] if n <= 1 else walk(nodes[idx(node)], n - 1)
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
    if r % 1000 == 0:
      print(f"-- move {r} --")
    # print(nodes)
    # print("cups:", f"({val(nodes[current_idx])}), {' '.join(map(str, acc(current_idx)))}")
    picked_up = list(
      map(find, [val(walk(nodes[current_idx])), val(walk(nodes[current_idx], 2)), val(walk(nodes[current_idx], 3))]))
    # print("pick up:", " ".join(map(str, picked_up)))
    nodes[current_idx] = (val(nodes[current_idx]), idx(picked_up[-1][1]))
    dest_val = (val(nodes[current_idx]) - 1) or len(nodes)
    # print("dest_val", dest_val, [val(x[1]) for x in picked_up])
    while dest_val in [val(x[1]) for x in picked_up]:
      dest_val = (dest_val - 1) or len(nodes)
    # print("dest_val", dest_val)
    dest_idx, dest_node = find(dest_val)
    # print(f"destination: {dest_node} at {dest_idx}")
    # print("search", picked_up[-1])
    nodes[picked_up[-1][0]] = (val(picked_up[-1][1]), idx(dest_node))
    nodes[dest_idx] = (val(dest_node), picked_up[0][0])
    # print("nodes:", nodes)
    # print("cups:", ' '.join(map(str, acc(current_idx))))
    current_idx = idx(nodes[current_idx])
  dest_idx, dest_node = find(1)
  return acc(dest_idx)


def parse(text: str) -> List[int]:
  return [int(x) for x in text]


def solve_part_1(text: str, rounds: int):
  return ''.join(map(str, play(parse(text), rounds)))[1:]


def solve_part_2(text: str, rounds: int):
  xs = parse(text)
  res = play(xs + list(range(len(xs) + 1, 1000001)), rounds)
  return res[1] * res[2]


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input, 100))
    print("Part 2:", solve_part_2(quiz_input, 10000000))
