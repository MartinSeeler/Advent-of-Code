import re

INST_CODES = ["N", "S", "E", "W", "L", "R", "F"]
NORTH, SOUTH, EAST, WEST, LEFT, RIGHT, FORWARD = range(7)

def split_inst(value):
	match = re.match(r"([a-z]+)([0-9]+)", value, re.I)
	return (INST_CODES.index(match.groups()[0]), int(match.groups()[1]))

all_inst = []
with open("input.txt", "r") as f:
    all_inst = list([split_inst(x) for x in f.read().splitlines()])

def walk(instructions, w_x = -1, w_y = 10, x = 0, y = 0):
	if len(instructions) == 0:
		return (x, y)
	(d, w), *rest = instructions
	print("at", INST_CODES[d], w, w_x, w_y, x, y)
	if d == FORWARD:
		return walk(rest, w_x, w_y, x+(w*w_x), y+(w*w_y))
	if d == NORTH:
		return walk(rest, w_x-w, w_y, x, y)
	if d == SOUTH:
		return walk(rest, w_x+w, w_y, x, y)
	if d == EAST:
		return walk(rest, w_x, w_y+w, x, y)
	if d == WEST:
		return walk(rest, w_x, w_y-w, x, y)
	if d in [LEFT, RIGHT]:
		if d == LEFT:
			w *= -1
		if (w//90) % 4 == 0:
			return walk(rest, w_x, w_y, x, y)
		elif (w//90) % 2 == 0:
			return walk(rest, -w_x, -w_y, x, y)
		elif (w//90) % 4 == 1:
			return walk(rest, w_y, -w_x, x, y)
		else:
			return walk(rest, -w_y, w_x, x, y)


(ns, ew) = walk(all_inst)
print(abs(ns)+abs(ew))
