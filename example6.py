sinir = int(input("sinir giriniz: "))

cift_list = []
tek_list = []
"""
if sinir > 0:
    sinir = sinir
    for i in range(sinir):
        if i % 2:
            tek_list.append(i)
        else:
            cift_list.append(i)
else:
    sinir = -1 * sinir
    for i in range(sinir):
        if i % 2:
            tek_list.append(-i)
        else:
            cift_list.append(-i)

print(tek_list)
print(cift_list)
"""
"""
if sinir >= 0:
    for i in range(0,sinir,2):
        cift_list.append(i)
        tek_list.append(i + 1)
else:
    for i in range(0,sinir, -2):
        cift_list.append(i)
        tek_list.append(i - 1)

print(cift_list)
print(tek_list)
"""
"""
artis = 2
tek_artis = 1

if sinir < 0:
    artis = -2
    tek_artis = -1

for i in range(0,sinir,artis):
    cift_list.append(i)
    tek_list.append(i + tek_artis)

print(cift_list)
print(tek_list)
"""