from math import ceil


class Snail:
    def __init__(self, input):
        self.depth_list = []
        self.char_list = []
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
        self.reduce()

    def explode(self, i=0):
        if self.depth_list[i] == 4:
            if i == 0:
                self.char_list[i + 2] += self.char_list[i + 1]
            elif i == self.length - 2:
                self.char_list[i - 1] += self.char_list[i]
            else:
                self.char_list[i + 2] += self.char_list[i + 1]
                self.char_list[i - 1] += self.char_list[i]

            self.char_list[i + 1] = 0
            self.char_list.pop(i)
            self.depth_list[i + 1] = 3
            self.depth_list.pop(i)
            self.length -= 1
            print(self.char_list)
            self.explode(i=0)
        elif i < self.length - 2:
            self.explode(i + 1)

    def split(self, i=0):
        if self.char_list[i] >= 10:
            left = self.char_list[i] // 2
            self.char_list[i] = ceil(self.char_list[i] / 2)
            self.char_list.insert(i, left)
            self.depth_list[i] += 1
            self.depth_list.insert(i, self.depth_list[i])
            self.length += 1
            print(self.char_list)
            self.explode()
            self.split()
        elif i < self.length - 1:
            self.split(i + 1)

    def reduce(self):
        self.explode()
        self.split()

s = Snail("[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]")
print(s.char_list)