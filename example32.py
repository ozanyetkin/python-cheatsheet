class Polygon:
    def __init__(self, edges):
        self.edges = edges
        self.name = self.get_name()
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()
    
    def get_name(self):
        edge_count = len(self.edges)
        return f"{edge_count}gen"

    def get_area(self):
        return "Area can't be known"

    def get_perimeter(self):
        perimeter = 0
        for edge in self.edges:
            perimeter += edge
        return perimeter


class Triangle(Polygon):
    def __init__(self, edge1, edge2, edge3):
        self.edges = [edge1, edge2, edge3]
        super().__init__(self.edges)
    
    def get_area(self):
        s = self.perimeter / 2
        area = (s * (s - self.edges[0]) * (s - self.edges[1]) * (s - self.edges[2])) ** (1 / 2)
        return area
    

class IsoscelesTriangle(Triangle):
    def __init__(self, edge1, edge2):
        edge3 = edge1
        super().__init__(edge1, edge2, edge3)
        self.name = "ikizkenar " + self.name


class EquilateralTriangle(Triangle):
    def __init__(self, edge1):
        edge2 = edge1
        edge3 = edge1
        super().__init__(edge1, edge2, edge3)
        self.name = "esitkenar " + self.name


# Test case including Polygon, Triangle, Parallelogram, IsoscelesTriangle, EquilateralTriangle, Rectangle, and Square
shapelist = [
    Polygon([1.0, 4.5, 3.1, 3.3]),
    Triangle(3.4, 5.3, 4.2),
    IsoscelesTriangle(4.1, 1),
    EquilateralTriangle(4.2),
    # Rectangle(5, 4),
    # Square(3.25),
]

for shape in shapelist:
    print(
        "{0} Area: {1}  Perimeter: {2:.3f}".format(
            shape.name, shape.area, shape.perimeter
        )
    )