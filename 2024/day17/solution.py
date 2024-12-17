import time
import re


def solve_part_1(text: str):
    nums = re.findall(r"\d+", text)
    A, B, C = map(int, nums[:3])
    instructions = list(map(int, nums[3:]))
    print(A, B, C)
    print(instructions)

    def combo_operand(x: int) -> int:
        match x:
            case 0 | 1 | 2 | 3:
                return x
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case _:
                raise ValueError(f"Invalid operand {x}")

    outs = []
    instruction_pointer = 0
    while instruction_pointer < len(instructions):
        opcode = instructions[instruction_pointer]
        operand = instructions[instruction_pointer + 1]
        print(opcode, operand, instruction_pointer, A, B, C, outs)

        if opcode == 0:  # adv
            numerator = A
            denominator = 2 ** combo_operand(operand)
            A = numerator // denominator
            instruction_pointer += 2
        elif opcode == 1:  # bxl
            B ^= operand
            instruction_pointer += 2
        elif opcode == 2:  # bst
            B = combo_operand(operand) % 8
            instruction_pointer += 2
        elif opcode == 3:  # jnz
            if A != 0:
                instruction_pointer = operand
            else:
                instruction_pointer += 2
        elif opcode == 4:  # bxc
            B ^= C
            instruction_pointer += 2
        elif opcode == 5:  # out
            outs.append(combo_operand(operand) % 8)
            instruction_pointer += 2
        elif opcode == 6:  # bdv
            numerator = A
            denominator = 2 ** combo_operand(operand)
            B = numerator // denominator
            instruction_pointer += 2
        elif opcode == 7:  # cdv
            numerator = A
            denominator = 2 ** combo_operand(operand)
            C = numerator // denominator
            instruction_pointer += 2
        else:
            raise ValueError(f"Invalid opcode {opcode}")

    return ",".join(map(str, outs))


def solve_part_2(text: str):
    pass


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = solve_part_1(quiz_input)
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
        p_2_solution = solve_part_2(quiz_input)
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
