import pandas as pd

df = pd.read_table("11_advent_of_code/day_3.txt", dtype=str, header=None)

gamma = ""
for i in range(12):
    count = 0
    for j in range(len(df)):
        count += int(df[0].iloc[j][i])
    if count >= 500:
        gamma += "1"
    else:
        gamma += "0"

epsilon = ""
for bit in gamma:
    if bit == "0":
        epsilon += "1"
    else:
        epsilon += "0"

print(gamma)
print(epsilon)

def deci(bin):
    decimal = 0
    bin = bin[::-1]
    for i in range(len(bin)):
        decimal += int(bin[i]) * (2 ** i)
    return decimal

print(deci(gamma) * deci(epsilon))

def most_common(pos, aday):
    count_1 = 0
    count_0 = 0
    for ad in aday:
        if df[0].iloc[ad][pos] == "1":
            count_1 += 1
        else:
            count_0 += 1
    if count_1 > count_0:
        return "1"
    elif count_0 > count_1:
        return "0"
    else:
        return "="

def life_sup(bit, pos=0, aday=list(range(1000))):
    if len(aday) == 1:
        return aday
    m = most_common(pos, aday)
    if m == "=":
        finder = bit
    else:
        if bit == "1":
            finder = m
        else:
            finder = '0' if m == '1' else '1'
    aday_n = []
    for i in range(len(aday)):
        if df[0].iloc[aday[i]][pos] == finder:
            aday_n.append(aday[i])
    aday = aday_n
    pos += 1
    return life_sup(bit, pos, aday)

o2 = life_sup("1")[0]
co2 = life_sup("0")[0]

print(deci(df[0].iloc[o2]) * deci(df[0].iloc[co2]))
