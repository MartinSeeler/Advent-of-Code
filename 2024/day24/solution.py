from collections import defaultdict
import functools
from operator import itemgetter
import re
import time


def solve_part_1(text: str):
    values_text, connections_text = text.split("\n\n")
    connections = {}
    for c in connections_text.split("\n"):
        source_left, op, source_right, _, target = c.split(" ")
        connections[target] = (source_left, op, source_right)

    all_gates = set()
    for k, v in connections.items():
        all_gates.add(k)
        source_left, _, source_right = v
        all_gates.add(source_left)
        all_gates.add(source_right)

    # Gather all z wires, sorted by their bit index
    relevant_keys = sorted(k for k in all_gates if k.startswith("z"))

    # Parse the initial (constant) values
    values = {}
    for line in values_text.split("\n"):
        wire_name, val = line.split(": ")
        values[wire_name] = val

    def get_value(key, override=None):
        """
        Evaluate the value of a wire.
        `override` is an optional dictionary for "swapped outputs":
            if override is not None and key is in override,
            we treat 'key' as if its source is actually override[key].
        """
        # If the wire is swapped to some other wire's output
        actual_key = override.get(key, key) if override else key

        # If it's a direct known value
        if actual_key in values:
            return values[actual_key]

        source_left, op, source_right = connections[actual_key]
        left_value = get_value(source_left, override=override)
        right_value = get_value(source_right, override=override)

        if op == "AND":
            return str(int(left_value) & int(right_value))
        elif op == "XOR":
            return str(int(left_value) ^ int(right_value))
        elif op == "OR":
            return str(int(left_value) | int(right_value))
        else:
            raise ValueError(f"Unknown operation {op}")

    # Build final binary number from z wires (least significant bit is z00, etc.)
    binary_number = "".join(get_value(k) for k in relevant_keys[::-1])
    return int(binary_number, 2)


def solve_part_2(text: str) -> str:
    """
    Inserted solution from the notebook. We detect wires that do not match
    the expected pattern for this specific puzzle's addition logic. Those
    'errors' are the swapped wires. Finally, we return them as a comma-
    separated list (sorted).
    """
    # -- Parse the puzzle input into two blocks: part A (values) and part B (ops)
    blocks = text.strip().split("\n\n")
    partA = blocks[0].splitlines() if len(blocks) > 0 else []
    partB = blocks[1].splitlines() if len(blocks) > 1 else []

    # Convert part A into a dictionary of wire->integer-value
    values = {}
    for line in partA:
        line = line.strip()
        if not line:
            continue
        name, val_str = line.split(": ")
        values[name] = int(val_str)

    # Convert part B into a list of operations: (inp1, inp2, gate, out)
    ops = []
    for line in partB:
        line = line.strip()
        if not line:
            continue
        left_part, out_wire = line.split("->")
        out_wire = out_wire.strip()
        inp1, gate, inp2 = left_part.strip().split(" ")
        ops.append((inp1, inp2, gate, out_wire))

    # -- Define a function that tries to apply gates repeatedly until no changes
    def work() -> int:
        nonlocal values
        missing = 0
        for inp1, inp2, gate, out in ops:
            # If we've already computed 'out', skip
            if out in values:
                continue
            # If we don't have values for inputs yet, skip
            if inp1 not in values or inp2 not in values:
                missing += 1
                continue

            # We do have values: apply the gate
            assert gate in ["AND", "OR", "XOR"], f"undefined gate {gate}"
            match gate:
                case "OR":
                    values[out] = values[inp1] | values[inp2]
                case "AND":
                    values[out] = values[inp1] & values[inp2]
                case "XOR":
                    values[out] = values[inp1] ^ values[inp2]
        return missing

    # Keep iterating until no missing references
    while work():
        pass

    # Now compute 'output' from all z-wires (bitwise).
    # This is used only to find the "highest bit" wire name (like 'z45').
    output = 0
    for k, v in values.items():
        if k.startswith("z"):
            # shift v into the correct bit position
            idx = int(k[1:])  # e.g. z12 => 12
            output |= v << idx

    # Find the highest bit actually used in 'output'
    def highest_bit(n: int) -> int | None:
        if n == 0:
            return None
        bit = 0
        while n:
            n >>= 1
            bit += 1
        return bit - 1

    hb = highest_bit(output)
    if hb is None:
        # If there's no z-wire usage or the sum is zero, fallback
        last_output = "z00"
    else:
        last_output = f"z{hb}"

    # -- Next, build usage stats for each wire
    usage = defaultdict(set)
    for inp1, inp2, gate, _ in ops:
        usage[inp1].add(gate)
        usage[inp2].add(gate)

    # We'll collect wires that do NOT match the puzzle's expected half-adder pattern => 'errors'
    errors = []

    # Check each gate against puzzle's pattern
    for inp1, inp2, gate, out in ops:
        if out == last_output:
            # special case for highest bit => must be 'int OR int = zXX'
            if inp1[0] in ("x", "y") or inp2[0] in ("x", "y") or gate != "OR":
                errors.append(out)
            continue

        if out == "z00":
            # special case for lowest bit => 'x00 XOR y00 -> z00'
            if sorted([inp1, inp2]) != ["x00", "y00"]:
                errors.append(out)
            if gate != "XOR":
                errors.append(out)
            continue

        # If one input is x00 or y00, then gate must be XOR or AND
        if "00" in inp1 or "00" in inp2:
            if (inp1.startswith("x") and inp2.startswith("y")) or (
                inp1.startswith("y") and inp2.startswith("x")
            ):
                if gate not in ("XOR", "AND"):
                    errors.append(out)
            continue

        # If gate == XOR
        if gate == "XOR":
            if inp1[0] in ("x", "y"):
                if inp2[0] not in ("x", "y"):
                    errors.append(out)
                if out.startswith("z"):
                    errors.append(out)
                # also expect AND+XOR usage on out
                if "AND" not in usage[out] or "XOR" not in usage[out]:
                    errors.append(out)
            elif not out.startswith("z"):
                errors.append(out)

        # If gate == OR
        elif gate == "OR":
            if inp1[0] in ("x", "y") or inp2[0] in ("x", "y") or out.startswith("z"):
                errors.append(out)
            # expect AND+XOR usage on out
            if "AND" not in usage[out] or "XOR" not in usage[out]:
                errors.append(out)

        # If gate == AND
        elif gate == "AND":
            if inp1[0] in ("x", "y"):
                if inp2[0] not in ("x", "y"):
                    errors.append(out)
            # expect OR usage on out
            if "OR" not in usage[out]:
                errors.append(out)

    # The puzzle states there are exactly 8 wires that are "errors" (i.e., swapped outputs).
    # We return them as a comma-separated list. If you *know* the puzzle has 8, we can assert that:
    errors = sorted(set(errors))
    # If your puzzle indeed always has 8, keep the assertion:
    # assert len(errors) == 8, f"Expected 8 swaps but found {len(errors)}"

    return ",".join(errors)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = int(solve_part_1(quiz_input))
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
        p_2_solution = solve_part_2(quiz_input)
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
