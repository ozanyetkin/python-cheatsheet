import numpy as np

scan_dict = {}
scanner_num = 0
beacon_list = []

with open("11_advent_of_code/day_19.txt") as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("---"):
        scan_dict[scanner_num] = beacon_list
        scanner_num = int(line[12:14])
        beacon_list = []
    elif line != "\n":
        x, y, z = line.replace("\n", "").split(",")
        beacon = np.array([int(x), int(y), int(z)])
        beacon_list.append(beacon)

def related(beacon1, beacon2):
    beacon1_s = np.absolute(beacon1)
    beacon2_s = np.absolute(beacon2)
    beacon1_s = np.sort(beacon1)
    beacon2_s = np.sort(beacon2)
    scaling = beacon2_s[0] / beacon1_s[0]
    if beacon1_s * scaling != beacon2_s:
        return False
    beacon1 = beacon1 * scaling
    x_loc = np.where(beacon2 == beacon1[0])
    y_loc = np.where(beacon2 == beacon1[1])
    z_loc = np.where(beacon2 == beacon1[2])
    trans_list = []