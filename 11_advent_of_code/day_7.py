import sys
from collections import Counter

sys.setrecursionlimit(2000)

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

def align(p_counts, left, right, left_cost=0, right_cost=0):
    if left == right:
        return left

    n_left_cost = fuel_calc(p_counts, left + 1, 1) - left_cost
    n_right_cost = fuel_calc(p_counts, right - 1, -1) - right_cost

    if n_left_cost <= n_right_cost:
        left += 1
        left_cost += n_left_cost
    else:
        right -= 1
        right_cost += n_right_cost
    return align(p_counts, left, right, left_cost, right_cost)

def fuel_calc(p_counts, final, side):
    fuel_cons = 0
    p_keys = list(p_counts.keys())
    p_keys.sort()
    if side == 1:
        for key in p_keys:
            if key > final:
                break
            fuel_cons += p_counts[key] * int((final - key) * (final - key + 1) / 2)
    else:
        p_keys.reverse()
        for key in p_keys:
            if key < final:
                break
            fuel_cons += p_counts[key] * int((key - final) * (key - final + 1) / 2)
    return fuel_cons

test = [16,1,2,0,4,2,7,1,2,14]
test = dict(Counter(test))
# print(test)
# print(fuel_calc(test, 5, -1))
p_min = min(pos_counts.keys())
p_max = max(pos_counts.keys())

best = align(pos_counts, p_min, p_max)
print(best)
print(fuel_calc(pos_counts, best, 1) + fuel_calc(pos_counts, best, -1))