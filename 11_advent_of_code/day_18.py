from math import ceil
from copy import deepcopy

class Snail:
    def __init__(self, input=str):
        self.char_list = []
        self.depth_list = []
        depth = 0
        for char in input:
            if char.isnumeric():
                self.char_list.append(int(char))
                self.depth_list.append(depth)
            elif char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
        self.length = len(self.char_list)

    def explode(self, i=0, once=False):
        if self.depth_list[i] >= 5:
            if i == 0:
                self.char_list[i + 2] += self.char_list[i + 1]
            elif i == self.length - 2:
                self.char_list[i - 1] += self.char_list[i]
            else:
                self.char_list[i + 2] += self.char_list[i + 1]
                self.char_list[i - 1] += self.char_list[i]
            self.char_list[i + 1] = 0
            self.char_list.pop(i)
            self.depth_list[i + 1] -= 1
            self.depth_list.pop(i)
            self.length -= 1
        if i < self.length - 2 and not once:
            self.explode(i + 1)

    def split(self, i=0):
        if self.char_list[i] >= 10:
            left = self.char_list[i] // 2
            self.char_list[i] = ceil(self.char_list[i] / 2)
            self.char_list.insert(i, left)
            self.depth_list[i] += 1
            self.depth_list.insert(i, self.depth_list[i])
            self.length += 1
            if self.depth_list[i] >= 5:
                self.explode(i, once=True)
                if i == 0:
                    self.split(i)
                else:
                    self.split(i - 1)
            else:
                self.split(i)
        if i < self.length - 1:
            self.split(i + 1)

    def reduce(self):
        self.explode()
        self.split()

    def magnitude(self, i=0):
        char_list = deepcopy(self.char_list)
        depth_list = deepcopy(self.depth_list)
        while max(depth_list) != 0:
            max_depth = max(depth_list); i = 0; searching=True
            while searching:
                if depth_list[i] == max_depth:
                    char_list[i + 1] = char_list[i] * 3 + char_list[i + 1] * 2
                    char_list.pop(i)
                    depth_list[i + 1] -= 1
                    depth_list.pop(i)
                    searching = False
                i += 1
        return char_list[0]

    def __add__(self, other):
        self.char_list += other.char_list
        self.depth_list += other.depth_list
        self.depth_list = [x + 1 for x in self.depth_list]
        self.length += other.length
        self.reduce()
        return self

with open("11_advent_of_code/day_18.txt") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]

result = Snail(lines[0])
for i in range(1, len(lines)):
    result = result + Snail(lines[i])

print(result.magnitude())

combinations = [(x, y) for x in lines for y in lines]

max_magnitude = 0
for combination in combinations:
    magnitude = (Snail(combination[0]) + Snail(combination[1])).magnitude()
    if magnitude > max_magnitude:
        max_magnitude = magnitude

print(max_magnitude)
