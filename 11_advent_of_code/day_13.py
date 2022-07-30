import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_table("11_advent_of_code/day_13.txt", header=None)

size_x = 0
size_y = 0
point_list = []
fold_list = []
for data in df[0]:
    try:
        x, y = data.split(",")
        point_list.append((int(x), int(y)))
        size_x = max(int(x), size_x)
        size_y = max(int(y), size_y)
    except ValueError:
        axis, fold = data.replace("fold along ", "").split("=")
        fold_list.append((axis, int(fold)))

paper = np.zeros((size_y + 1, size_x + 1), dtype=int)

for point in point_list:
    x, y = point
    paper[y][x] = 1

for instruction in fold_list:
    fold_axis, fold_num = instruction
    flipped_paper = np.flip(paper, 1 if fold_axis == "x" else 0)
    final_paper = paper + flipped_paper
    final_paper = final_paper[:fold_num, :] if fold_axis == "y" else final_paper[:, :fold_num]
    paper = final_paper

print(paper)
print(np.count_nonzero(paper))
paper = paper > 0

fig, ax = plt.subplots()
im = ax.imshow(paper)
plt.savefig("paper.png")


def main():
    with open("11_advent_of_code/day_13.txt") as f:
        data = [i for i in f.read().splitlines()]

    # seperate coordinates and fold data into seperate lists
    for i, val in enumerate(data):
        if val == '':
            coordinates = data[:i]
            folds = data[i+1:]
    
    coordinates = [[int(j) for j in i.split(',')] for i in coordinates]

    # for each fold, translate coordinates using formula: num - ((num - fold_num) * 2)
    for fold in folds:
        axis = fold[11]
        fold_num = int(fold[13:])

        if axis == 'y':
            for coordinate in coordinates:
                y = coordinate[1]
                if ((y - fold_num) * 2) >= 0:
                    coordinate[1] = y - ((y - fold_num) * 2)

        if axis == 'x':
            for coordinate in coordinates:
                x = coordinate[0]
                if ((x - fold_num) * 2) >= 0:
                    coordinate[0] = x - ((x - fold_num) * 2)
        
    # get max range for x and y coords
    max_x, max_y = 0, 0
    for coordinate in coordinates:
        if coordinate[0] > max_x:
            max_x = coordinate[0]
        if coordinate[1] > max_y:
            max_y = coordinate[1]

    # make an empty graph
    graph = [[' ' for x in range(max_x + 1)] for y in range(max_y + 1)]

    # append coordinates to the graph with '#'
    for coordinate in coordinates:
        x, y = coordinate[0], coordinate[1]
        if graph[y][x] == ' ':
            graph[y][x] = '#'

    # print the graph
    for line in graph:
        print(line)


if __name__ == '__main__':
    main()