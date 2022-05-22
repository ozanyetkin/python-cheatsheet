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

def check_pos(konum, maze):
    if konum == (0, 0) or konum == (0, len(maze[0]) - 1) or konum == (len(maze) - 1, 0) or konum == (len(maze) - 1, len(maze[-1]) - 1):
        return "kose"
    elif konum[0] == 0 or konum[0] == len(maze) - 1 or konum[1] == 0 or konum[1] == len(maze[0]) - 1:
        return "kenar"
    else:
        return "orta"

def maze_tra(maze):
    satir = [1] * len(maze[0])
    new_maze = [satir] + maze + [satir]
    for i in range(len(new_maze)):
        new_maze[i] = [1] + new_maze[i] + [1]
    return new_maze

def next_step():
    pass

# print(check_pos((7,7), maze1))
# print(check_pos((0,7), maze1))
# print(check_pos((2,0), maze1))
# print(check_pos((3,4), maze1))

# Test cases for solvable and not solvable mazes
# print(is_solvable(maze1, (0, 0), (7, 7)))
# should print True

# print(is_solvable(maze2, (0, 0), (7, 7)))
# should print False

# print(is_solvable(maze3, (0, 0), (8, 8)))
# should print True
