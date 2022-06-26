from time import perf_counter
from collections import Counter
t1_start = perf_counter()

with open('11_advent_of_code/day_6.txt') as f:
    line = f.readline()

time_to_birth = [int(l) for l in line.split(",")]
times = {}
for i in range(9):
    times[i] = 0

for t in time_to_birth:
    times[t] += 1

for day in range(256):
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
