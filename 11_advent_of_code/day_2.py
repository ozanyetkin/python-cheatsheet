import pandas as pd

df = pd.read_table("11_advent_of_code/day_2.txt", delimiter=" ")

depth, hori = 0, 0
for i in range(len(df)):
    if df["direction"].iloc[i] == "forward":
        hori += df["power"].iloc[i]
    elif df["direction"].iloc[i] == "up":
        depth -= df["power"].iloc[i]
    else:
        depth += df["power"].iloc[i]

print(depth * hori)

depth, hori, aim = 0, 0, 0
for i in range(len(df)):
    if df["direction"].iloc[i] == "forward":
        hori += df["power"].iloc[i]
        depth += df["power"].iloc[i] * aim
    elif df["direction"].iloc[i] == "up":
        aim -= df["power"].iloc[i]
    else:
        aim += df["power"].iloc[i]

print(depth * hori)
