il = []
with open("input.txt", "r") as f:
    il = f.read().splitlines()

parse = lambda idx: int(il[idx].split(" ")[1])

def fs(idx, acc, visited):
    if idx in visited:
        return None
    elif idx == len(il):
        return visited, acc
    else:
        if il[idx].find("nop")==0:
            return (fs(idx+1, acc, visited | set([idx])) or 
                fs(idx+parse(idx), acc, visited | set([idx])))
        elif il[idx].find("acc")==0:
            return fs(idx+1, acc+parse(idx), visited | set([idx]))
        else:
            return (fs(idx+parse(idx), acc, visited | set([idx])) or 
                fs(idx+1, acc, visited | set([idx])))

print(fs(0, 0, set())[1])