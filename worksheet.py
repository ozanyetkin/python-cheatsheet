import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('example_img.png')
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
print(img)
imgplot = plt.imshow(img)
plt.show()