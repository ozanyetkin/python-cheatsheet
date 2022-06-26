import pandas as pd
import turtle
from collections import Counter

df = pd.read_table("11_advent_of_code/day_5.txt", header=None, delimiter=" -> ")

def marker(point1, point2):
    marked = []
    x1, y1 = int(point1.split(",")[0]), int(point1.split(",")[1])
    x2, y2 = int(point2.split(",")[0]), int(point2.split(",")[1])

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            marked.append((x1, y))

    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            marked.append((x, y1))

    if abs(y1 - y2) == abs(x1 - x2):
        x_crement = int((x2 - x1) / abs(x2 - x1))
        y_crement = int((y2 - y1) / abs(y2 - y1))
        for i in range(abs(x2 - x1) + 1):
            marked.append((x1 + x_crement * i, y1 + y_crement * i))

    return marked

lines = set()
intersections = set()
for i in range(len(df)):
    line = marker(df[0].iloc[i], df[1].iloc[i])
    for point in line:
        if point not in lines:
            lines.add(point)
        else:
            intersections.add(point)

print(len(intersections))
"""
c = Counter(lines)
counter = 0
for key, value in c.items():
    if value > 1:
        counter += 1
"""
"""
s = turtle.Screen()
t = turtle.Turtle()

s.title('Canvas')
s.setup(width = 0.5, height = 0.5, startx=0, starty=0)

s.setworldcoordinates(-200,-200,1200,1200)
for i in range(len(df)):
    lines = marker(df[0].iloc[i], df[1].iloc[i])
    for l in lines:
        t.goto(l[0], l[1])
        t.dot()
"""