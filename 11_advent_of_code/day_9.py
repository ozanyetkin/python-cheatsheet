import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_table("11_advent_of_code/day_9.txt", header=None, dtype=str)
map = []
for row in df[0]:
    map.append([int(s) for s in row])

map = np.array(map)

def find_neighbor(coord):
    neighbor_list = [
        (coord[0] + 1, coord[1]),
        (coord[0], coord[1] + 1),
        (coord[0], coord[1] - 1),
        (coord[0] - 1, coord[1])
    ]
    return neighbor_list

risk_points = []
for i in range(100):
    for j in range(100):
        coordinate = (i, j)
        neighbors = find_neighbor(coordinate)

        risk = True
        for neighbor in neighbors:
            try:
                if map[i][j] >= map[neighbor[0]][neighbor[1]]:
                    risk = False
            except:
                pass
        if risk:
            risk_points.append(coordinate)

total = 0
for risk_point in risk_points:
    total += map[risk_point[0]][risk_point[1]] + 1

print(risk_points)

fig, ax = plt.subplots()
im = ax.imshow(map)
for risk_point in risk_points:
    plt.scatter(risk_point[1], risk_point[0], c="red", s=0.5)
plt.savefig("map.png")
