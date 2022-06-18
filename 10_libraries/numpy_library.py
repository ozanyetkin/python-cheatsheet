import numpy as np

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

maze = np.array(maze1)

print(maze)
print(maze.size)
print(maze.shape)
