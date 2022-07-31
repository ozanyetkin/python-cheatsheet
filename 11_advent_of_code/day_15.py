import numpy as np
import pandas as pd
import sys

sys.setrecursionlimit(50000)
from collections import defaultdict


df = pd.read_table("11_advent_of_code/day_15.txt", header=None, dtype=str)

danger_map = []
for row in df[0]:
    danger_map.append([int(s) for s in row])

danger_map = np.array(danger_map)
map_size = danger_map.shape[0]

def def_value():
    return 100000

unvisited_nodes = set()
visit_costs = defaultdict(def_value)

visit_costs[(0, 0)] = 0

for i in range(map_size):
    for j in range(map_size):
        unvisited_nodes.add((i, j))

def find_neighbor(coord, size=map_size):
    neighbor_list = {
        (coord[0] + 1, coord[1]),
        (coord[0], coord[1] + 1),
        (coord[0], coord[1] - 1),
        (coord[0] - 1, coord[1])
    }
    neighbors = set()
    for n in neighbor_list:
        if size - 1 >= n[0] >= 0 and size - 1 >= n[1] >= 0:
            neighbors.add(n)
    return neighbors

visit_map = np.zeros((map_size, map_size), dtype=int)

def walker(position=(0, 0)):
    visit_map[position] = 1
    print(visit_map)
    print(visit_costs)
    neighbors = find_neighbor(position)
    unvisited_nodes.remove(position)
    if len(unvisited_nodes) == 0:
        return visit_costs
    for neighbor in neighbors:
        if neighbor in unvisited_nodes:
            if visit_costs[neighbor] > (danger_map[neighbor] + visit_costs[position]):
                visit_costs[neighbor] = (danger_map[neighbor] + visit_costs[position])
    min_cost = 100000
    selected = "Not Found"
    for neighbor in neighbors:
        if visit_costs[neighbor] < min_cost and neighbor in unvisited_nodes:
            min_cost = visit_costs[neighbor]
            selected = neighbor
    if selected != "Not Found":
        return walker(selected)
    min_cost = 100000
    for node in unvisited_nodes:
        if visit_costs[node] < min_cost:
            min_cost = visit_costs[node]
            selected = node
    return walker(selected)
        
walker()
print(visit_costs[(map_size - 1, map_size - 1)])
"""
position = (0, 0)
while len(unvisited_nodes) > 0:
    if position in unvisited_nodes:
        unvisited_nodes.remove(position)
        current_cost = danger_map[position]
        neighbors = find_neighbor(position)
        for n in neighbors:
            cost = danger_map[n]
            if cost == None:
                visit_costs[n] = cost
            else:
                if cost < visit_costs[n]:
                    visit_costs[n] = cost
"""