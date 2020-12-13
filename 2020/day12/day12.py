import re

INST_CODES = ["N", "S", "E", "W", "L", "R", "F"]
NORTH, SOUTH, EAST, WEST, LEFT, RIGHT, FORWARD = range(7)
FACING = EAST

DIRS = [NORTH, EAST, SOUTH, WEST]

def split_inst(value):
	match = re.match(r"([a-z]+)([0-9]+)", value, re.I)
	return (INST_CODES.index(match.groups()[0]), int(match.groups()[1]))

all_inst = []
with open("input.txt", "r") as f:
    all_inst = list([split_inst(x) for x in f.read().splitlines()])

def walk(instructions, current_dir=EAST, x = 0, y = 0):
	if len(instructions) == 0:
		return (x, y)
	(d, w), *rest = instructions
	print("at", d, w, x, y)
	if d == FORWARD:
		return walk([(current_dir, w), *rest], current_dir, x, y)
	if d == NORTH:
		return walk(rest, current_dir, x-w, y)
	if d == SOUTH:
		return walk(rest, current_dir, x+w, y)
	if d == EAST:
		return walk(rest, current_dir, x, y+w)
	if d == WEST:
		return walk(rest, current_dir, x, y-w)
	if d == RIGHT:
		return walk(rest, DIRS[(DIRS.index(current_dir)+(w//90)) % len(DIRS)], x, y)
	if d == LEFT:
		return walk(rest, DIRS[(DIRS.index(current_dir)-(w//90)) % len(DIRS)], x, y)


(ns, ew) = walk(all_inst)
print(abs(ns)+abs(ew))
