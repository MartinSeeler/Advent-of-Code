from collections import defaultdict, deque
import re
import time

# After analyzing the input, there seems to be a pattern. After every `inp w`, we got a reset of variables.
# Analyzing it further, we can see that each w,x and y gets resetted in every block after the `inp w` command.
# Se breaking it down to these blocks, we can see a pattern when we only look at the constant values used in the operations.
#
#  0   26    1   10    0    0   25    1    0    2
#  0   26    1   14    0    0   25    1    0   13
#  0   26    1   14    0    0   25    1    0   13
#  0   26   26  -13    0    0   25    1    0    9
#  0   26    1   10    0    0   25    1    0   15
#  0   26   26  -13    0    0   25    1    0    3
#  0   26   26   -7    0    0   25    1    0    6
#  0   26    1   11    0    0   25    1    0    5
#  0   26    1   10    0    0   25    1    0   16
#  0   26    1   13    0    0   25    1    0    1
#  0   26   26   -4    0    0   25    1    0    6
#  0   26   26   -9    0    0   25    1    0    3
#  0   26   26  -13    0    0   25    1    0    7
#  0   26   26   -9    0    0   25    1    0    9
#
# Only the indices at 2,3 and 9 do actually change. Index 2 depends on the sign of index 3. If index 3 is negative,
# index 2 is 26, otherwise it is 1. Also, there are 7 positive and 7 negative values of index 3.
# Breaking the algorithm down, we read an input and check if the input is equal to z mod 26 + value at index 3.
# If index 3 is negative, divide z by 26.
# If our input is not equal,set z to z * 26 + value at index 9 + input value.
#
# All operations on z include the value 26, so we can look at it like a stack of numbers to base 26 (by multiplying, dividing, etc),
# where we increase the digit by iterating, until our conditions are met, which indicates the single input digits (since we push and pop in a loop otherwise).
# So then we can define the algorithm with our values from index 3 and 9 as follow:
#
# 10 2
# PUSH => input[0] + 2
# 14 13
# PUSH => input[1] + 13
# 14 13
# PUSH => input[2] + 13
# -13 9
# POP => input[3] == input[2] + 13 - 13 => input[3] == input[2]
# 10 15
# PUSH => input[4] + 15
# -13 3
# POP => input[5] == input[4] + 15 - 13 => input[5] == input[4] + 2
# -7 6
# POP => input[6] == input[1] + 13 - 7 => input[1] + 6
# 11 5
# PUSH => input[7] + 5
# 10 16
# PUSH => input[8] + 16
# 13 1
# PUSH => input[9] + 1
# -4 6
# POP => input[10] == input[9] + 1 - 4 => input[10] == input[9] - 3
# -9 3
# POP => input[11] == input[8] + 16 - 9 => input[11] == input[8] + 7
# -13 7
# POP => input[12] == input[7] + 5 - 13 => input[12] == input[7] - 8
# -9 9
# POP => input[13] == input[0] + 2 - 9 => input[13] == input[0] - 7
#
# So now all equations are:
#
# input[3] == input[2]
# input[5] == input[4] + 2
# input[6] == input[1] + 6
# input[10] == input[9] - 3
# input[11] == input[8] + 7
# input[12] == input[7] - 8
# input[13] == input[0] - 7
#
# which gives a full set of equations:
#
# input[0] = input[13] + 7
# input[1] = input[6] - 6
# input[2] = input[3]
# input[3] = input[2]
# input[4] = input[5] - 2
# input[5] = input[4] + 2
# input[6] = input[1] + 6
# input[7] = input[12] + 8
# input[8] = input[11] - 7
# input[9] = input[10] + 3
# input[10] = input[9] - 3
# input[11] = input[8] + 7
# input[12] = input[7] - 8
# input[13] = input[0] - 7
#
# input[0] is 9 or 8, otherwise input[13] will be 0 or less, which is not possible
# therefore, input[13] is 1 or 2
# input[7] is always 9, otherwise input[12] will be 0 or less, which is not possible
# therefore, input[12] is always 1
# input[8] is 1 or 2, otherwise input[11] will be greater than 9, which is not possible
# therefore, input[11] is 8 or 9
# input[9] is >= 4, otherwise input[10] will be 0 or less, which is not possible
# input[11] is 8 or 9, otherwise input[8] will be 0 or less, which is not possible
# input[1] is 1,2 or 3, otherwise input[6] will be greater than 9, which is not possible
# input[4] is below 8, otherwise input[5] will be greater than 9, which is not possible
#
# leaving us with the following combinations (idx 0 to 13 top to bottom)
#
# [9|8]
# [1|2|3]
# [1|2|3|4|5|6|7|8|9]
# [1|2|3|4|5|6|7|8|9]
# [1|2|3|4|5|6|7]
# [3|4|5|6|7|8|9]
# [7|8|9]
# 9
# [1|2]
# [4|5|6|7|8|9]
# [1|2|3|4|5|6]
# [9|8]
# 1
# [1,2]
#
# putting this into code we get:


def generate_all_solutions():
    solutions = []
    num = [0] * 14
    num[7] = 9
    num[12] = 1
    for x0 in [9, 8]:
        num[0] = x0
        num[13] = x0 - 7
        for x1 in [1, 2]:
            num[8] = x1
            num[11] = x1 + 7
            for x2 in [4, 5, 6, 7, 8, 9]:
                num[9] = x2
                num[10] = x2 - 3
                for x3 in [1, 2, 3]:
                    num[1] = x3
                    num[6] = x3 + 6
                    for x4 in [1, 2, 3, 4, 5, 6, 7]:
                        num[4] = x4
                        num[5] = x4 + 2
                        for x5 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            num[2] = x5
                            num[3] = x5
                            solutions.append("".join(map(str, num)))
    return solutions


def solve_part_1(text: str):
    return max(generate_all_solutions())


def solve_part_2(text: str):
    return min(generate_all_solutions())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = int(solve_part_1(quiz_input))
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.2f}ms)")
        p_2_solution = int(solve_part_2(quiz_input))
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.2f}ms)")
