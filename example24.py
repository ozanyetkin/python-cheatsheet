import numpy as np
# Initialize a maze that is solvable
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

# Initialize another maze that is not solvable
maze2 = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0],
]

# Just in case, create a bigger maze and test the function
maze3 = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0],
]
"""
def check_pos(konum, maze):
    if konum == (0, 0) or konum == (0, len(maze[0]) - 1) or konum == (len(maze) - 1, 0) or konum == (len(maze) - 1, len(maze[-1]) - 1):
        return "kose"
    elif konum[0] == 0 or konum[0] == len(maze) - 1 or konum[1] == 0 or konum[1] == len(maze[0]) - 1:
        return "kenar"
    else:
        return "orta"
"""
def maze_tra(maze):
    satir = [1] * len(maze[0])
    new_maze = [satir] + maze + [satir]
    for i in range(len(new_maze)):
        new_maze[i] = [1] + new_maze[i] + [1]
    return new_maze

def next_step(konum, maze):
    komsu_list = [
        (konum[0] + 1, konum[1]),
        (konum[0], konum[1] + 1),
        (konum[0], konum[1] - 1),
        (konum[0] - 1, konum[1])
    ]
    aday = []
    for i in komsu_list:
        if maze[i[0]][i[1]] == 0:
            aday.append(i)
    return aday

def modif(koord, maze):
    k1 = koord[0]
    k2 = koord[1]
    if koord[0] == 0:
        k1 += 1
    if koord[0] == len(maze) - 1:
        k1 -= 1
    if koord[1] == 0:
        k2 += 1
    if koord[1] == len(maze[0]) - 1:
        k2 -= 1
    return (k1, k2)

def run(konum, son, maze, path, crossover):
    path.append(konum)
    print(konum)
    print(crossover)
    print(np.array(maze))
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
        sonraki = next_step(konum, maze)[0]
        kalanlar = next_step(konum, maze)[1:]
        if kalanlar != []:
            crossover += kalanlar
        return run(sonraki, son, maze, path, crossover)

def is_solvable(maze, bas, son):
    bas = (bas[0] + 1, bas[1] + 1)
    son = (son[0] + 1, son[1] + 1)
    maze = maze_tra(maze)
    return run(bas, son, maze, [], [])

# print(check_pos((7,7), maze1))
# print(check_pos((0,7), maze1))
# print(check_pos((2,0), maze1))
# print(check_pos((3,4), maze1))

# Test cases for solvable and not solvable mazes
print(is_solvable(maze3, (0, 0), (8, 8)))
print(np.array(maze_tra(maze3)))
# should print True

# print(is_solvable(maze2, (0, 0), (7, 7)))
# should print False

# print(is_solvable(maze3, (0, 0), (8, 8)))
# should print True
