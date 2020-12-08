il = []
with open("./input.txt", "r") as f:
    il = f.read().splitlines()

def fs(idx, acc, visited):
    if idx in visited:
        return None
    elif idx == len(il):
        return visited, acc
    else:
        if il[idx].startswith("nop"):
            return (fs(idx+1, acc, visited.union(set([idx]))) or 
                fs(idx+int(il[idx].split(" ")[1]), acc, visited.union(set([idx]))))
        elif il[idx].startswith("acc"):
            return fs(idx+1, acc+int(il[idx].split(" ")[1]), visited.union(set([idx])))
        else:
            return (fs(idx+int(il[idx].split(" ")[1]), acc, visited.union(set([idx]))) or 
                fs(idx+1, acc, visited.union(set([idx]))))

print(fs(0, 0, set())[1])