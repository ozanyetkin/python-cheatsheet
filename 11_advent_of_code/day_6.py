import numpy as np

from time import perf_counter
from collections import Counter
from sympy import Matrix

days = 256

t1_start = perf_counter()

with open('11_advent_of_code/day_6.txt') as f:
    line = f.readline()

time_to_birth = [int(l) for l in line.split(",")]
times = {}
for i in range(9):
    times[i] = 0

for t in time_to_birth:
    times[t] += 1

for day in range(days):
    x = times[0]

    for i in range(6):
        times[i] = times[i + 1]

    times[6] = times[7] + x
    times[7] = times[8]
    times[8] = x

total = 0
for value in times.values():
    total += value

print(total)

"""
for i in range(80):
    for j in range(len(time_to_birth)):
        if time_to_birth[j] == 0:
            time_to_birth.append(8)
            time_to_birth[j] = 6
        else:
            time_to_birth[j] -= 1
"""
t1_stop = perf_counter()
print("Elapsed t during the whole program in seconds:", t1_stop-t1_start)

matrix_string = "000000101100000000010000000001000000000100000000010000000001000000000100000000010"

a = np.zeros((9, 9), dtype=int)

count = 0
for i in range(9):
    for j in range(9):
        s = int(matrix_string[count])
        a[j][i] = s
        count += 1

a = np.linalg.eig(a)

print(a)

t2_start = perf_counter()

times_vec = np.zeros((9, 1), dtype=int)

times = {}
for i in range(9):
    times[i] = 0

for t in time_to_birth:
    times[t] += 1

for key, value in times.items():
    times_vec[key] = value

result_vec = times_vec
for i in range(days):
    result_vec = np.matmul(a, result_vec)
    # result_vec = a.dot(result_vec)

# result_vec = a_t.dot(times_vec)

print(np.sum(result_vec))

t2_stop = perf_counter()
print("Elapsed t during the whole program in seconds:", t2_stop-t2_start)