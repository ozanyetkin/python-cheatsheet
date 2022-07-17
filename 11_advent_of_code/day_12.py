import sys
from collections import Counter

sys.setrecursionlimit(15000)

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
"""
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
"""
# print(len(walker(path_dict)))

def walker(map: dict, chosen: str, current_path=[]):
    optional_paths = []
    options = option_finder(map, current_path, chosen) 
    for option in options:
        if option != "end":
            optional_paths.append(current_path + [option])
    if "end" in options:
        finished_path = current_path + ["end"]
        return finished_path, optional_paths, True
    else:
        return [], optional_paths, False


def option_finder(map: dict, current_path: list, chosen: str):
    counts = Counter(current_path)
    forbidden = set(filter(lambda x: x.islower(), current_path))

    if counts[chosen] < 2 and chosen in forbidden:
        forbidden.remove(chosen)
    return map[current_path[-1]].difference(forbidden)

def collector(map: dict, chosen: str, unfinished_paths=[["start"]], finished_paths=[]):
    if len(unfinished_paths) > 0:
        finished_path, optional_paths, is_finished = walker(map, chosen, unfinished_paths.pop())
        if is_finished:
            finished_paths.append(finished_path)
        unfinished_paths += optional_paths
        return collector(map, chosen, unfinished_paths, finished_paths)
    else:
        return finished_paths

chosen_set = set(filter(lambda x: x.islower() and x not in ["start", "end"], path_dict.keys()))
all_paths = []
for chosen in chosen_set:
    all_paths += collector(path_dict, chosen)

print(len(all_paths))