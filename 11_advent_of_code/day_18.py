from math import ceil


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

    def explode(self, i=0):
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
        if i < self.length - 2:
            print(self.char_list, i)
            self.explode(i + 1)

    def split(self, i=0):
        if self.char_list[i] >= 10:
            left = self.char_list[i] // 2
            self.char_list[i] = ceil(self.char_list[i] / 2)
            self.char_list.insert(i, left)
            self.depth_list[i] += 1
            self.depth_list.insert(i, self.depth_list[i])
            self.length += 1
            if i < self.length - 2:
                self.split(i + 2)
        if i < self.length - 1:
            print(self.char_list, i)
            self.split(i + 1)

    def reduce(self):
        while max(self.depth_list) >= 5:
            self.explode()
            self.split()

    def __add__(self, other):
        self.char_list += other.char_list
        self.depth_list += other.depth_list
        self.depth_list = [x + 1 for x in self.depth_list]
        self.length += other.length
        self.reduce()
        return self


s1 = Snail("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")

with open ("11_advent_of_code/day_18.txt") as f:
    for line in f:
        s1 = s1 + Snail(line[:-1])
        print(s1.char_list)