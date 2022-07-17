import sys
sys.setrecursionlimit(20000)

with open("11_advent_of_code/day_12.txt") as f:
    lines = f.readlines()

path_pieces = [set(l.replace("\n", "").split("-")) for l in lines]
unique_nodes = set([node for sublist in path_pieces for node in sublist])

path_dict = {}
for node in unique_nodes:
    val = set()
    for piece in path_pieces:
        if node in piece:
            val = val.union(piece.difference(set([node])))
    path_dict[node] = val

def walker(path: dict, path_l=[], current_path=["start"], finished_path=[], current="start"):
    if current == "end":
        finished_path.append(current_path)
        if len(path_l) > 0:
            current_path = path_l.pop()
            return walker(path, path_l, current_path, finished_path, current_path[-1])
        else:
            return finished_path
    
    valid_options = []
    not_valid = list(filter(lambda x: x.islower(), current_path))

    for option in path[current]:
        if option not in not_valid:
            valid_options.append(option)

    if len(valid_options) > 0:
        current = valid_options.pop()
        for v_option in valid_options:
            potential_path = current_path + [v_option]
            path_l.append(potential_path)
        current_path.append(current)
        return walker(path, path_l, current_path, finished_path, current)
    else:
        if len(path_l) > 0:
            current_path = path_l.pop()
            return walker(path, path_l, current_path, finished_path, current_path[-1])
        else:
            return finished_path

print(len(walker(path_dict)))
