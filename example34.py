import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Image:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.size = (height, width)
        self.color = np.full((height, width, 3), (255, 255, 255))

    def change_size(self, height, width):
        bin_h = self.height / height
        bin_w = self.width / width
        resized = np.empty((height, width, 3), dtype=int)
        count_i = 0
        for i in np.arange(0, self.height, bin_h):
            count_j = 0
            for j in np.arange(0, self.width, bin_w):
                red = self.color[math.ceil(i):math.ceil(i + bin_h), math.ceil(j):math.ceil(j + bin_w), 0]
                green = self.color[math.ceil(i):math.ceil(i + bin_h), math.ceil(j):math.ceil(j + bin_w), 1]
                blue = self.color[math.ceil(i):math.ceil(i + bin_h), math.ceil(j):math.ceil(j + bin_w), 2]
                resized[count_i, count_j] = np.array([int(np.average(red)), int(np.average(green)), int(np.average(blue))])
                count_j += 1
            count_i += 1
        self.height = height
        self.width = width
        self.size = (height, width)
        self.color = resized

    def randomize(self):
        self.color = np.random.randint(255, size=(self.height, self.width, 3))

    def read_image(self, file_name):
        df = pd.read_table(f"{file_name}.txt", delimiter=",")
        height = df["H"].iloc[-1] + 1
        width = df["W"].iloc[-1] + 1
        canvas = np.empty((height, width, 3), dtype=int)
        vector = np.array(df[["R", "G", "B"]])
        for i in range(len(df)):
            canvas[df["H"].iloc[i], df["W"].iloc[i]] = vector[i]
        self.height = height
        self.width = width
        self.size = (height, width)
        self.color = canvas

    def save(self, name="output"):
        plt.imshow(self.color)
        plt.savefig(name)

img = Image(24, 38)
print(img)
print(img.size)

img.randomize()
img.save("output_1")
img.change_size(15, 24)
img.save("output_2")
img.read_image("example_image")
img.save("output_3")
img.change_size(64, 116)
img.save("output_4")