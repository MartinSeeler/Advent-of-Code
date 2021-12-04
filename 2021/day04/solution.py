def parse_input(text: str):
  lines = text.splitlines()
  nums = list(map(int, lines[0].split(",")))
  lines = lines[2:]
  boards = [
        [list(map(int, row.split())) for row in lines[6 * i : 6 * i + 5]]
        for i in range((len(lines)+1) // 6)
    ]
  return nums, boards

def is_board_complete(board_hits: dict, x: int, y: int) -> bool:
  # the board is complete, if we got all indices up and down the current (x,y) position in our hits
  return all((x, yy) in board_hits for yy in range(5)) or all((xx, y) in board_hits for xx in range(5))

def play_until(boards, nums, min_boards_complete: int):
  boards_won = set()
  hits = [{} for _ in boards]
  for num in nums:
    for board_idx, (board, board_hits) in enumerate(zip(boards, hits)):
      for y, row in enumerate(board):
        for x, board_num in enumerate(row):
          if board_num == num:
            board_hits[(x, y)] = num
            if is_board_complete(board_hits, x, y):
                board_score = (sum(sum(row) for row in board) - sum(board_hits.values())) * num
                boards_won.add(board_idx)
                if len(boards_won) >= min_boards_complete:
                    return board_score
  return 0

def solve_part_1(text: str):
  nums, boards = parse_input(text)
  return play_until(boards, nums, 1)


def solve_part_2(text: str):
  nums, boards = parse_input(text)
  return play_until(boards, nums, len(boards))


if __name__ == '__main__':
  with open("input.txt", "r") as f:
    quiz_input = f.read()
    print("Part 1:", solve_part_1(quiz_input))
    print("Part 2:", solve_part_2(quiz_input))
