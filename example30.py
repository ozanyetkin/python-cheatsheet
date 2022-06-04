maze1 = [
    [0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

def next_step(konum, maze):
    komsu_list = [
        (konum[0] + 1, konum[1]),
        (konum[0], konum[1] + 1),
        (konum[0], konum[1] - 1),
        (konum[0] - 1, konum[1])
    ]
    aday = []
    for i in komsu_list:
        try:
            if maze[i[0]][i[1]] == 0:
                aday.append(i)
        except IndexError:
            pass
    return aday

def run(konum, son, maze, path=[], crossover=[], count=0):
    path.append(konum)
    # print(konum)
    # print(crossover)
    # print(np.array(maze))
    maze[konum[0]][konum[1]] = 1
    if konum == son:
        return True, path
    elif next_step(konum, maze) == []:
        if crossover == []:
            return False, path
        else:
            sonraki = crossover[0]
            crossover = crossover[1:]
            return run(sonraki, son, maze, path, crossover)
    else:
        count += 1
        sonraki = next_step(konum, maze)[0]
        kalanlar = next_step(konum, maze)[1:]
        if kalanlar != []:
            crossover += kalanlar
        return run(sonraki, son, maze, path, crossover)

print(run((0, 0), (7, 7), maze1))