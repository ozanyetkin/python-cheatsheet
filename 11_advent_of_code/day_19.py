from collections import Counter, defaultdict
import numpy as np
import matplotlib.pyplot as plt

scan_dict = {}

beacon_list = []
scanner_num = 0

with open("11_advent_of_code/day_19.txt") as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("---"):
        scanner_num = int(line[12:14])
        beacon_list = []
    elif line != "\n":
        x, y, z = line.replace("\n", "").split(",")
        beacon = np.array([int(x), int(y), int(z)])
        beacon_list.append(beacon)
    else:
        scan_dict[scanner_num] = beacon_list


def distance(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    dz = point2[2] - point1[2]
    return dx**2 + dy**2 + dz**2


dis_dict = {}
for scanner in scan_dict.keys():
    put_me = {}
    for choosen in scan_dict[scanner]:
        dis_list = []
        for other in scan_dict[scanner]:
            dis_list.append(distance(choosen, other))
        # print(sorted(dis_list))
        put_me[tuple(choosen)] = Counter(dis_list)
    dis_dict[scanner] = put_me

"""
def scanner_matcher(scanner1,scanner2):
    common=0
    for point1 in dis_dict[scanner1]:
        for point2 in dis_dict[scanner2]:
            keys=dis_dict[scanner1][point1]|dis_dict[scanner2][point2].keys()
            all_numbers=dis_dict[scanner1][point1]|dis_dict[scanner2][point2]
            for key in keys:
                if key not in (dis_dict[scanner1][point1]&dis_dict[scanner2][point2]).keys():
                    del all_numbers[key]
            if sum(all_numbers.values())>=12:
                common+=1
    return True if common>=12 else False
    """


def scanner_matcher(scanner1, scanner2):
    common = 0
    matchings1 = []
    matchings2 = []
    keys1 = set(dis_dict[scanner1].keys())
    keys2 = set(dis_dict[scanner2].keys())
    for point1 in keys1:
        for point2 in keys2.copy():
            countin = 0
            for key in dis_dict[scanner1][point1] & dis_dict[scanner2][point2]:
                countin += (
                    dis_dict[scanner1][point1][key] + dis_dict[scanner2][point2][key]
                )
            if countin >= 12:
                common += 1
                matchings1.append(point1)
                matchings2.append(point2)
                keys2.remove(point2)
        if common >= 12:
            return True, [matchings1, matchings2]
    return False, None


def orientation_same(vector1, vector2):
    ori1 = np.sign(np.cross(np.array([vector1[0], 0, 0]), np.array([0, vector1[1], 0])))
    ori2 = np.sign(np.cross(np.array([vector2[0], 0, 0]), np.array([0, vector2[1], 0])))
    return True if (ori1 == ori2).all() else False


def map_generator(scanner1, scanner2):
    flag1 = False
    flag2 = False
    keys1 = set(dis_dict[scanner1].keys())
    keys2 = set(dis_dict[scanner2].keys())
    for point1 in keys1:
        for point2 in keys2.copy():
            countin = 0
            for key in dis_dict[scanner1][point1] & dis_dict[scanner2][point2]:
                countin += (
                    dis_dict[scanner1][point1][key] + dis_dict[scanner2][point2][key]
                )
            if countin >= 12:
                keys2.remove(point2)
                if flag1:
                    tuple1s, tuple2s = point1, point2
                    flag2 = True
                else:
                    tuple1b, tuple2b = point1, point2
                flag1 = True
            if flag1 and flag2:
                vector1 = np.array(tuple1s) - np.array(tuple1b)
                vector2 = np.array(tuple2s) - np.array(tuple2b)

    oriented = False
    if not orientation_same(vector1, vector2):
        oriented = True
        vector2[2] = vector2[2] * (-1)
    coord_map = []
    iterator = set([x for x in enumerate(vector2)])
    for coord1 in vector1:
        for i, coord2 in iterator.copy():
            if coord2 == coord1:
                coord_map.append(i + 1)
                iterator.remove((i, coord2))
                break
            elif coord2 == coord1 * (-1):
                coord_map.append(-(i + 1))
                iterator.remove((i, coord2))
                break
    return coord_map, oriented


def composer_old(map2, map1):
    f_map = []
    for pointer in map1:
        f_map.append(
            abs(map2[abs(pointer) - 1]) * np.sign(pointer * map2[abs(pointer) - 1])
        )
    return f_map


def apply(map, point):
    range_point = [0, 0, 0]
    for i, number in enumerate(list(point)):
        range_point[abs(map[i]) - 1] = np.sign(map[i]) * number
    return range_point


def composer(*maps):
    f_map = composer_old(maps[0], maps[1])
    for map in maps[2:]:
        f_map = composer_old(f_map, map)
    return f_map


def reverse_map(map):
    r_map = [0, 0, 0]
    for i, prev in enumerate(map):
        r_map[abs(prev) - 1] = np.sign(prev) * (i + 1)
    return r_map


def decoder(scanner1, scanner2, carry_over=[]):
    go_forward, oriented = map_generator(scanner1, scanner2)
    go_back = reverse_map(go_forward)
    set_list = []
    _, matchings = scanner_matcher(scanner1, scanner2)
    matchings1 = matchings[0]
    matchings2 = matchings[1]

    translated_beacons = [
        np.array(apply(go_back, [point[0], point[1], list(point)[2] * (-1)]))
        if oriented
        else np.array(apply(go_back, point))
        for point in matchings2
    ]

    for not_translated in matchings1:
        translation_advo = set()
        for translated in translated_beacons:
            translation_advo.add(tuple(translated - not_translated))
        set_list.append(translation_advo)

    translation = set_list[0]
    for rest in set_list[1:]:
        translation = translation & rest
    translation_vector = np.array(translation.pop())
    orient_rotate = [
        np.array(apply(go_back, [point[0], point[1], list(point)[2] * (-1)]))
        if oriented
        else np.array(apply(go_back, point))
        for point in scan_dict[scanner2] + carry_over
    ]
    translate = [x - translation_vector for x in orient_rotate]
    return translation_vector, go_back, oriented, translate


translation_vecs = {}


def find_layers(path=[[0]], seen={0}):
    if seen == set(range(len(scan_dict.keys()))):
        return path[::-1]
    next_layer = set()

    for next in path[-1]:
        next_layer |= scanner_rel[next]
    next_layer = next_layer.difference(seen)
    path.append(list(next_layer))
    seen = next_layer | seen
    
    return find_layers(path, seen)


carry_overs = defaultdict(list)


def def_value():
    bu = {"Scanner numbers": [], "Scanner locations": []}
    return bu


carry_overs_scanners = defaultdict(def_value)


def solve_all(path, i=0):
    if i == len(path) - 1:
        final = carry_overs[0]
        [
            final.append(x)
            for x in scan_dict[0]
            if not np.any([np.all(np.equal(x, y)) for y in carry_overs[0]])
        ]
        result = set([tuple(x) for x in final])
        return result
    else:
        advocates = set(path[i + 1])
        for node in path[i]:
            where_to = (scanner_rel[node] & advocates).pop()
            trans_vec, go_back, oriented, translated = decoder(
                where_to, node, carry_overs[node]
            )
            translation_vecs[(where_to, node)] = trans_vec
            heyallam = []
            [
                heyallam.append(x)
                for x in translated
                if not np.any([np.all(np.equal(x, y)) for y in heyallam])
            ]
            carry_overs[where_to] = carry_overs[where_to] + translated
            new_locations = []
            for scan_node in carry_overs_scanners[node]["Scanner locations"]:
                new_locations.append(
                    np.array(
                        apply(
                            go_back,
                            [scan_node[0], scan_node[1], list(scan_node)[2] * (-1)],
                        )
                    )
                    - trans_vec
                    if oriented
                    else np.array(apply(go_back, scan_node)) - trans_vec
                )
            new_locations.append((-1) * trans_vec)
            carry_overs_scanners[where_to]["Scanner numbers"] = (
                carry_overs_scanners[where_to]["Scanner numbers"]
                + carry_overs_scanners[node]["Scanner numbers"]
                + [node]
            )
            carry_overs_scanners[where_to]["Scanner locations"] = (
                carry_overs_scanners[where_to]["Scanner locations"] + new_locations
            )
        return solve_all(path, i + 1)


scanner_rel = defaultdict(set)
for scanner in range(len(scan_dict.keys())):
    for candit in range(scanner + 1, len(scan_dict.keys())):
        if scanner_matcher(scanner, candit)[0]:
            scanner_rel[scanner].add(candit)
            scanner_rel[candit].add(scanner)
# Part1
all_beacons = solve_all(find_layers())
print(len(all_beacons))


scanner_loc = sorted(
    [(0, np.array([0, 0, 0]))]
    + list(
        zip(
            carry_overs_scanners[0]["Scanner numbers"],
            carry_overs_scanners[0]["Scanner locations"],
        )
    )
)


manhattan_distances = []
for scanner1 in range(len(scanner_loc)):
    for scanner2 in range(scanner1 + 1, len(scanner_loc)):
        manhattan_distances.append(
            (
                (scanner1, scanner2),
                np.sum(
                    np.absolute(scanner_loc[scanner1][1] - scanner_loc[scanner2][1])
                ),
            )
        )
manhattan_distances.sort(reverse=True, key=lambda x: x[1])
print(manhattan_distances[0])

ax = plt.axes(projection='3d')

for loc in scanner_loc:
    scanner_x, scanner_y, scanner_z = tuple(loc[1])
    ax.scatter3D(scanner_x, scanner_y, scanner_z, c="red")

for beacon in all_beacons:
    beacon_x, beacon_y, beacon_z = beacon
    ax.scatter3D(beacon_x, beacon_y, beacon_z, c="blue")

plt.savefig("scanners_and_beacons.png")