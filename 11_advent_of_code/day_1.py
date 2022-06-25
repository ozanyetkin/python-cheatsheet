sweep = []
with open("11_advent_of_code/day_1.txt") as f:
    while True:
        line = f.readline()
        try:
            sweep.append(int(line))
        except:
            pass
        if not line:
            break

count = 0
for i in range(len(sweep)):
    try:
        if sweep[i] < sweep[i+3]:
            count += 1
    except:
        pass

print(count)