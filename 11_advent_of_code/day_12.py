with open('11_advent_of_code/day_12.txt') as f:
    lines = f.readlines()

path_pieces = [l.replace("\n", "").split("-") for l in lines]

