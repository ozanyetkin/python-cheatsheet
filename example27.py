import random

aminoacids = {
    1: "A", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "K", 10: "L", 11: "M",
    12: "N", 13: "P", 14: "Q", 15: "R", 16: "S", 17: "T", 18: "V", 19: "W", 20: "Y"
}

molecular_weights = {
    "I": 131.1736, "L": 131.1736, "K": 146.1882, "M": 149.2124, "F": 165.19, "T": 119.1197, "W": 204.2262,
    "V": 117.1469, "R": 174.2017, "H": 155.1552, "A": 89.0935, "N": 132.1184, "D": 133.1032, "C": 121.159,
    "E": 147.1299, "Q": 146.1451, "G": 75.0669, "P": 115.131, "S": 105.093, "Y": 181.1894
}

# Test case molecular weight of WEINAY is 884.9309999999998
# calculate_mw("WEINAY")
# calculate_mw(generate_ps(26))

def generate_ps(uzu):
    gene = ""
    for i in range(uzu):
        gene += aminoacids[random.randint(1, 20)]
    return gene

def calculate_mw(gene):
    weight = 0
    for g in gene:
        weight += molecular_weights[g]
    return weight

print(generate_ps(12))
print(calculate_mw("WEINAY"))
print(calculate_mw(generate_ps(26)))
