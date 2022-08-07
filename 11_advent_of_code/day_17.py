from math import ceil, floor
import numpy as np
import matplotlib.pyplot as plt
from itertools import zip_longest

x_min, x_max = 20, 30
y_min, y_max = -10, -5

"""
poly = [1, 1, -x_max * 2]
roots = np.roots(poly)
x_velo_max = int(max(roots))

poly = [1, 1, -x_min * 2]
roots = np.roots(poly)
x_velo_min = int(max(roots))

possible_x = [i for i in range(ceil(x_velo_min), floor(x_velo_max) + 1)]

y_velo_cmax = abs(y_min) - 1
y_velo_min = abs(y_max) - 1
max_height = (y_velo_cmax * (y_velo_cmax + 1)) // 2

certains = len(possible_x) * (y_velo_cmax - y_velo_min)
print(max_height)
"""

"""
x_axis = [i * (i + 1) / 2 for i in range(x_velo + 1)][::-1]
x_axis = [int(max(x_axis) - x) for x in x_axis]
y_up = [int(i * (i + 1) / 2) for i in range(y_velo + 1)][::-1]
y_up = [int(max(y_up) - y) for y in y_up]
y_down = y_up[::-1]
y_speed = [i for i in range(-(y_velo + 1), -20, -1)]
y_hell = [sum(y_speed[0:n]) for n in range(1, 2)]

y_axis = y_up + y_down + y_hell

for x, y in zip_longest(x_axis, y_axis, fillvalue=max(x_axis)):
    plt.scatter(x, y)
plt.show()
"""
poly = [1, 1, -x_min * 2]
roots = np.roots(poly)
x_velo_min = int(max(roots))

y_velo_max = abs(y_min) - 1
y_velo_min = y_min

x_velo_min = ceil(x_velo_min)
x_velo_max = x_max

y_range = [y for y in range(y_velo_min, y_velo_max + 1)]
x_range = [x for x in range(x_velo_min, x_velo_max + 1)]

velo_range = [(x, y) for x in x_range for y in y_range]


def tracker(x_velo, y_velo, trajectory=[]):
    t = 0
    r = (
        -(t**2) / 2 + x_velo * t if t <= x_velo else (x_velo**2) / 2,
        -(t**2) / 2 + y_velo * t,
    )
    trajectory.append(r)

    while r[0] < x_max and r[1] > y_min:
        r = (
            -(t**2) / 2 + x_velo * t if t <= x_velo else (x_velo**2) / 2,
            -(t**2) / 2 + y_velo * t,
        )
        trajectory.append(r)

        if x_min <= r[0] <= x_max and y_min <= r[1] <= y_max:
            return trajectory
        t += 1
    return False

hit_count = 0
for x, y in velo_range:
    if tracker(x, y):
        hit_count += 1

print(hit_count)

"""
print(velo_range)
for x, y in velo_range[24:28]:
    a = tracker(x, y)
    if a:
        for fuck in a:
            plt.scatter(fuck[0], fuck[1])

plt.show()
"""