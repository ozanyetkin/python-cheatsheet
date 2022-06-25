import pandas as pd

df = pd.read_table("11_advent_of_code/day_5.txt", header=None, delimiter=" -> ")

def marker(point1, point2):
    marked = set()
    x1, y1 = int(point1.split(",")[0]), int(point1.split(",")[1])
    x2, y2 = int(point2.split(",")[0]), int(point2.split(",")[1])

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)):
            marked.add((x1, y))
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)):
            marked.add((x, y1))
    return marked

marked = set()
count = 0
for i in range(len(df)):
    line = marker(df[0].iloc[i], df[1].iloc[i])
    for l in line:
        if l not in marked:
            marked.add(l)
        else:
            count += 1

print(count)