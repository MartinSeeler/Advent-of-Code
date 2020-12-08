il = []
with open("./input.txt", "r") as f:
    il = f.read().splitlines()

def find_solution(idx, acc, visited):
    if idx in visited:
        return None
    if idx == len(il):
        return visited, acc
    else:
        if il[idx].startswith("nop"):
            return find_solution(idx+1, acc, visited.union(set([idx]))) or find_solution(idx+int(il[idx].split(" ")[1]), acc, visited.union(set([idx])))
        elif il[idx].startswith("acc"):
            return find_solution(idx+1, acc+int(il[idx].split(" ")[1]), visited.union(set([idx])))
        else:
            return find_solution(idx+int(il[idx].split(" ")[1]), acc, visited.union(set([idx]))) or find_solution(idx+1, acc, visited.union(set([idx])))

print(find_solution(0, 0, set())[1])
