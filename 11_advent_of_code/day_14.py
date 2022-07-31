from collections import Counter, defaultdict
from copy import deepcopy

with open("11_advent_of_code/day_14.txt") as f:
    lines = f.readlines()

polymers = [l.replace("\n", "").split("->") for l in lines]

base_polymer = polymers[0][0]
n_step_dict = {}
for poly in polymers[2:]:
    n_step_dict[poly[0][0] + poly[0][1]] = {1: {poly[0][0] + poly[1][1]: 1, poly[1][1] + poly[0][1]: 1}}

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
"""
def generate(base_polymer, step):
    if step > 0:
        for x in range(len(base_polymer) - 1):
            generate(base_polymer[x] + poly_trans[base_polymer[x:x+2]], step - 1)
            generate(poly_trans[base_polymer[x:x+2]] + base_polymer[x+1], step - 1)
    else:
        sum_dict[base_polymer[0]] += 1

generate(base_polymer, 10)
sum_dict[base_polymer[-1]] += 1

print(max(sum_dict.values()) - min(sum_dict.values()))
"""
"""
def generate(base_polymer, step):
    if step > 0:
        for x in range(len(base_polymer) - 1):
            generate(base_polymer[x] + poly_trans[base_polymer[x:x+2]], step - 1)
            generate(poly_trans[base_polymer[x:x+2]] + base_polymer[x+1], step - 1)
    else:
        sum_dict[base_polymer] += 1

one_step_dict = poly_trans.copy()

for key in one_step_dict.keys():
    generate(key, 1)
    one_step_dict[key] = deepcopy(sum_dict)
    sum_dict.clear()
"""
# print(one_step_dict)
"""
def finders_keepers_even(base_polymer, step):
    if len(base_polymer) > 2:
        for x in range(len(base_polymer) - 1):
            finders_keepers_even(base_polymer[x:x+2], step)
    else:
        if step != 1:
            if (base_polymer, step) in n_step_dict.keys():
                return n_step_dict[(base_polymer, step)]
            else:
                finders_keepers_even(base_polymer, step // 2)
        else:
            base_step = {}
            # for key in one_step_dict[base_polymer].keys():
            #     for subkey in one_step_dict[key].keys():
            #         base_step[subkey] = one_step_dict[base_polymer][key] * one_step_dict[key][subkey]
            n_step_dict[(base_polymer, 2)] = base_step
            finders_keepers_even(base_polymer, step * 2)
"""
def climber(double_poly, target):
    max_key = max(n_step_dict[double_poly].keys())
    if target == max_key or target == 1 or target in n_step_dict[double_poly].keys():
        return n_step_dict[double_poly][target]
    elif target > max_key * 2:
        base_dict = defaultdict(def_value)
        for key in n_step_dict[double_poly][max_key].keys():
            for subkey in climber(key, max_key).keys():
                base_dict[subkey] += n_step_dict[double_poly][max_key][key] * climber(key, max_key)[subkey]
        n_step_dict[double_poly].update({max_key * 2: base_dict})
        return climber(double_poly, target)
    else:
        base_dict = defaultdict(def_value)
        for key in n_step_dict[double_poly][max_key].keys():
            for subkey in climber(key, target - max_key).keys():
                base_dict[subkey] += n_step_dict[double_poly][max_key][key] * climber(key, target - max_key)[subkey]
        n_step_dict[double_poly].update({target: base_dict})
        return climber(double_poly, target)

# climber("CH", 5)
# print(n_step_dict)

my_list = []
for key in n_step_dict.keys():
    for subkey in n_step_dict[key][1].keys():
        my_list.append(subkey)

stupid_priority = Counter(my_list).most_common()
priority_a = []
priority_b = []

for key, _ in stupid_priority:
    if key in n_step_dict[key][1].keys():
        priority_a.append(key)
    else:
        priority_b.append(key)

priority_keys = priority_a + priority_b + list(set(n_step_dict.keys()).difference(set(my_list)))

def stepper(step):
    for key in priority_keys:
        climber(key, step)

for x in range(1, 4):
    stepper(2 ** x)

for x in range(2, 6):
    stepper(x * 8)

dict_list = []
for x in range(len(base_polymer) - 1):
    dict_list.append(climber(base_polymer[x:x+2], 40))

char_dict = defaultdict(def_value)
for key in priority_keys:
    for dict in dict_list:
        if key in dict.keys():
            char_dict[key[0]] += dict[key]
            char_dict[key[1]] += dict[key]

char_dict[base_polymer[0]] += 1
char_dict[base_polymer[-1]] += 1

print((max(char_dict.values()) - min(char_dict.values())) // 2)
