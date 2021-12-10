from collections import deque
import time

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

def find_non_matching_bracket(line: str) -> str:
   rem  = deque()
   for c in line:
     if c in "([{<":
        rem.append(c)
     else:
       last = rem.pop()
       exp = pairs[last]
       if exp != c:
         return c
    
def find_incomplete_remaining(line: str) -> str:
   rem  = deque()
   for c in line:
     if c in "([{<":
        rem.append(c)
     else:
       last = rem.pop()
       exp = pairs[last]
       if exp != c:
         return ""
   ending = ""
   while len(rem) > 0:
     ending += pairs[rem.pop()]
   return ending


def solve_part_1(text: str):
  points = {")": 3, "}": 1197, "]": 57, ">": 25137}
  score = 0
  for line in text.splitlines():
    res = find_non_matching_bracket(line)
    if res:
      score += points[res]
  return score
  
def solve_part_2(text: str):
  points = {")": 1, "]": 2, "}": 3, ">": 4}
  scores = []
  for line in text.splitlines():
    score = 0
    res = find_incomplete_remaining(line)
    for c in res:
      score = (score * 5) + points[c]
    if score > 0:
      scores.append(score)
  return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    start = time.time()
    p_1_solution = int(solve_part_1(quiz_input))
    middle = time.time()
    print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
    p_2_solution = int(solve_part_2(quiz_input))
    end = time.time()
    print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
