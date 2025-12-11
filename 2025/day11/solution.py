import time
from functools import cache
from pathlib import Path


def parse_routes(text: str):
  routes = {}
  for line in text.strip().splitlines():
    router_from, router_to = line.strip().split(": ")
    router_tos = router_to.split(" ")
    routes[router_from] = router_tos
  return routes


def solve_part_1(text: str):
  routes = parse_routes(text)

  @cache
  def count_paths(node):
    if node == "out":
      return 1
    return sum(count_paths(next_node) for next_node in routes.get(node, []))

  return count_paths("you")


def solve_part_2(text: str):
  routes = parse_routes(text)

  @cache
  def count_paths(node, dac=False, fft=False):
    if node == "out":
      return 1 if dac and fft else 0
    return sum(count_paths(next_node, dac or next_node == "dac", fft or next_node == "fft")
               for next_node in routes.get(node, []))

  return count_paths("svr")


if __name__ == '__main__':
  with open(Path(__file__).parent / "input.txt", "r") as f:
    quiz_input = f.read()
    start = time.time()
    p_1_solution = int(solve_part_1(quiz_input))
    middle = time.time()
    print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
    p_2_solution = int(solve_part_2(quiz_input))
    end = time.time()
    print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
