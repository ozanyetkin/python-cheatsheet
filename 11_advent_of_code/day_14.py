from collections import Counter, defaultdict

with open("11_advent_of_code/day_14.txt") as f:
    lines = f.readlines()

polymers = [l.replace("\n", "").split("->") for l in lines]

base_polymer = polymers[0][0]
poly_trans = {}
for poly in polymers[2:]:
    poly_trans[poly[0][0] + poly[0][1]] = poly[1][1]

"""
def transform(polymer, position=0):
    next_polymer = ""
    if len(polymer) > 2:
        if position != len(polymer) - 2:
            if position == 0:
                next_polymer += polymer[position] + poly_trans[polymer[position] + polymer[position + 1]] + polymer[position + 1] + transform(polymer, position + 1)
            else:
                next_polymer += poly_trans[polymer[position] + polymer[position + 1]] + polymer[position + 1] + transform(polymer, position + 1)
        else:
            return poly_trans[polymer[position] + polymer[position + 1]] + polymer[position + 1]
        return next_polymer
    else:
        return polymer[position] + poly_trans[polymer[position] + polymer[position + 1]] + polymer[position + 1]

def mythosis(step, piece):
    for _ in range(step):
        piece = transform(piece)
    return piece

counter_list = []
for i in range(len(base_polymer) - 1):
    if i != len(base_polymer) - 2:
        stepped_piece = mythosis(10, base_polymer[i] + base_polymer[i + 1])
        stepped_piece = stepped_piece[:len(stepped_piece) - 1]
        counter_list.append(Counter(stepped_piece))
    else:
        stepped_piece = mythosis(10, base_polymer[i] + base_polymer[i + 1])
        counter_list.append(Counter(stepped_piece))
"""

def def_value():
    return 0

sum_dict = defaultdict(def_value)

def generate(base_polymer, step):
    if step > 0:
        for x in range(len(base_polymer) - 1):
            generate(base_polymer[x] + poly_trans[base_polymer[x:x + 2]], step - 1)
            generate(poly_trans[base_polymer[x:x + 2]] + base_polymer[x + 1], step - 1)
    else:
        