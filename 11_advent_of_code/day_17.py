from math import ceil, floor
import numpy as np
import matplotlib.pyplot as plt
from itertools import zip_longest
from collections import defaultdict

x_min, x_max = 192, 251
y_min, y_max = -89, -59

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
"""
print(velo_range)
for x, y in velo_range[24:28]:
    a = tracker(x, y)
    if a:
        for fuck in a:
            plt.scatter(fuck[0], fuck[1])

plt.show()
"""
y_step_dictionary = defaultdict(set)

y_step = 1
negative_velocities = [1]
while len(negative_velocities) > 0:
    # Instead of throwing with down with v we can throw up with v-1. So positives can be counted from negatives.2*(-v-1)+1+y_step total steps for positive one.
    # y_min<=y_step*y_velo-(y_step*(y_step-1))/2<=y_max what y_velos that satisfy this while len(velocities)>0:
    # y_min+(y_step*(y_step-1))/2<=y_step*y_velo<=y_max+(y_step*(y_step-1))/2
    # So integer number of velocities that hit area are integers in [(y_min+(y_step*(y_step-1))/2)/y_step,(y_max+(y_step*(y_step-1))/2)/y_step]
    # We want negative ones so:
    negative_velocities = [
        y_velo
        for y_velo in range(
            ceil((y_min + (y_step * (y_step - 1)) / 2) / y_step),
            min(0, floor((y_max + (y_step * (y_step - 1)) / 2) / y_step) + 1),
        )
    ]
    for velo in negative_velocities:
        y_step_dictionary[y_step].add(velo)
        y_step_dictionary[-2 * velo - 1 + y_step].add(-velo - 1)
    y_step += 1
y_step_dictionary = dict(sorted(y_step_dictionary.items()))

# print(y_step_dictionary)

x_step_dictionary = {}
# x_min<=x_step*x_velo-(x_step*(x_step-1))/2 if x_step<x_velo else (x_velo**2)/2+x_velo/2 <=x_max what x_velos that satisfy this
# x_min+(x_step*(x_step-1))/2<=x_step*x_velo<=x_max+(x_step*(x_step-1))/2 for velocities that did not stop before that is x_step<x_velo
# That is same as y but when we se

stops = []
for x_step in y_step_dictionary.keys():
    velocities = []
    velocities += stops
    interval = list(
        range(
            max(ceil((x_min + (x_step * (x_step - 1)) / 2) / x_step), x_step),
            floor((x_max + (x_step * (x_step - 1)) / 2) / x_step) + 1,
        )
    )
    if len(interval) > 0:
        for x_velo in interval:
            velocities.append(x_velo)
            if x_velo == x_step:
                stops.append(x_velo)
    x_step_dictionary[x_step] = velocities

# print(x_step_dictionary)

velocity_pairs = []
for step in x_step_dictionary.keys():
    velocity_pairs += [
        (x, y) for x in x_step_dictionary[step] for y in y_step_dictionary[step]
    ]
# Convert to set so we dont count twice

print(len(set(velocity_pairs)))
