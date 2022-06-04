from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = self.get_area()

    def get_area(self):
        self.area = pi * (self.radius ** 2)
        return self.area
    
    def set_area(self, area):
        self.area = area
        self.radius = self.get_radius()
    
    def get_radius(self):
        self.radius = (self.area / pi) ** (1 / 2)
        return self.radius

    def set_radius(self, radius):
        self.radius = radius
        self.area = self.get_area()

c1 = Circle(5)

print(c1.radius)
print(c1.area)

c1.set_area(100)

print(c1.radius)
print(c1.area)

c1.set_radius(6)

print(c1.radius)
print(c1.area)
