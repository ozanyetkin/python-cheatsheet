import sys
from collections import Counter

sys.setrecursionlimit(1200)

with open('11_advent_of_code/day_7.txt') as f:
    line = f.readline()

positions = [int(l) for l in line.split(",")]
positions.sort()
"""
def align(lst, left_pos, right_pos, fuel_used=0):
    if lst[0] == lst[-1]:
        return fuel_used

    if left_pos <= -(right_pos + 1):
        step = lst[left_pos] - lst[0]
        lst = move_crabs(lst, left_pos, step, 1)
        fuel_used += step * (left_pos)
        left_count = count_same(lst, left_pos, 1)
        left_pos += left_count
    else:
        step = lst[-1] - lst[right_pos]
        lst = move_crabs(lst, -(right_pos + 1), step, -1)
        fuel_used += step * -(right_pos + 1)
        right_count = count_same(lst, right_pos, -1)
        right_pos -= right_count
    return align(lst, left_pos, right_pos, fuel_used)

def count_same(lst, start_i, dir=1, count=1):
    try:
        if lst[start_i + dir] != lst[start_i]:
            return count
    except IndexError:
        return count
    count += 1
    start_i += dir
    return count_same(lst, start_i, dir, count)

def move_crabs(lst, count, step, dir=1):
    if dir == 1:
        for i in range(count):
            lst[i] += step
    if dir == -1:
        for i in range(-1, -(count + 1), -1):
            lst[i] -= step
    return lst
"""
# print(count_same(positions, start_i=-1, dir=-1))
# print(move_crabs(positions, 1, 31, -1))
# test = [16,1,2,0,4,2,7,1,2,14]
# test.sort()
# print(align(positions, count_same(positions, 0, 1), -(count_same(positions, -1, -1) + 1)))

pos_counts = dict(Counter(positions))
pos_counts[min(pos_counts.keys())]

def align(p_counts):
    p_counts[min(p_counts.keys())]