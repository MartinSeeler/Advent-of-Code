import time


color_indxs = ["red", "green", "blue"]


def solve_part_1(text: str):
    res = 0
    for line in text.splitlines():
        # input: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game, boxes = line.split(": ")
        game_id = int(game.split(" ")[1])
        box_iters = boxes.split("; ")
        failed = False
        for iter in box_iters:
            # iter: 1 red, 2 green, 6 blue
            observations = iter.split(", ")
            obs_counts = [0, 0, 0]
            for observation in observations:
                # observation: 1 red
                count, color = observation.split(" ")
                count = int(count)
                color_idx = color_indxs.index(color)
                obs_counts[color_idx] += count
            if obs_counts[0] > 12 or obs_counts[1] > 13 or obs_counts[2] > 14:
                failed = True
        if not failed:
            res += game_id
    return res


def solve_part_2(text: str):
    res = 0
    for line in text.splitlines():
        # input: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game, boxes = line.split(": ")
        game_id = int(game.split(" ")[1])
        box_iters = boxes.split("; ")
        all_obs = []
        for iter in box_iters:
            # iter: 1 red, 2 green, 6 blue
            observations = iter.split(", ")
            obs_counts = [0, 0, 0]
            for observation in observations:
                # observation: 1 red
                count, color = observation.split(" ")
                count = int(count)
                color_idx = color_indxs.index(color)
                obs_counts[color_idx] += count
            all_obs.append(obs_counts)
        zip_obs = zip(*all_obs)
        # find max for each color
        maxes = [max(obs) for obs in zip_obs]
        power = maxes[0] * maxes[1] * maxes[2]
        res += power
    return res


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
