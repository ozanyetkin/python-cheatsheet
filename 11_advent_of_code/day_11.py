import pandas as pd
import numpy as np

df = pd.read_table("11_advent_of_code/day_11.txt", header=None, dtype=str)

octo = []
for row in df[0]:
    octo.append([int(s) for s in row])

octo = np.array(octo)

def find_neighbor(coord):
    neighbor_list = {
        (coord[0] + 1, coord[1]),
        (coord[0], coord[1] + 1),
        (coord[0], coord[1] - 1),
        (coord[0] - 1, coord[1]),
        (coord[0] + 1, coord[1] + 1),
        (coord[0] - 1, coord[1] - 1),
        (coord[0] - 1, coord[1] + 1),
        (coord[0] + 1, coord[1] - 1)
    }
    neighbors = set()
    for n in neighbor_list:
        if 9 >= n[0] >= 0 and 9 >= n[1] >= 0:
            neighbors.add(n)
    return neighbors

def flash_checker(array, not_flashed):
    new_not_flashed = set()
    for n in not_flashed:
        flashing_neigh = 0
        for neigh in find_neighbor(n):
            if neigh not in not_flashed:
                flashing_neigh += 1
        if array[n[0], n[1]] + flashing_neigh <= 9:
            new_not_flashed.add(n)
    if new_not_flashed == not_flashed:
        return not_flashed
    return flash_checker(array, new_not_flashed)

def play(array, step):
    flash_count = 0
    for _ in range(step):
        array += np.ones((10, 10), dtype=int)
        not_flashed = set()

        for i in range(10):
            for j in range(10):
                if array[i, j] <= 9:
                    not_flashed.add((i, j))
        not_flashed = flash_checker(array, not_flashed)
        next_array = np.zeros((10, 10), dtype=int)

        for n in not_flashed:
            flashing_neigh = 0
            for neigh in find_neighbor(n):
                if neigh not in not_flashed:
                    flashing_neigh += 1
            next_array[n[0], n[1]] = array[n[0], n[1]] + flashing_neigh

        flash_count += 100 - len(not_flashed)
        array = next_array
    return flash_count

print(play(octo, 100))