import math



class Polygon:
    def get_area(self):
        raise NotImplementedError("You  must implement get_are().")
    
    def get_sides(self):
        raise NotImplementedError("You must implement get_sides().")

    def get_perimeter(self):
        perimeter = 0
        sides = self.get_sides()
        for side in sides:
            perimeter += side

        return perimeter

class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_sides(self):
        return [self.side1, self.side2, self.side3]

    def get_area(self):
        return get_triangle_area(self.side1, self.side2, self.side3)

class Rectangle(Polygon):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_sides(self):
        return [self.width, self.height, self.width, self.height]

    def get_area(self):
        return get_rectangle_area(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    


# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height


triangle = Triangle(1, 5, 6)
rect = Rectangle(2, 3)
print([2, 2, 3, 3], sorted(rect.get_sides()))
square = Square(3)
print([3, 3, 3, 3], sorted(square.get_sides()))
print([1, 5, 6], sorted(triangle.get_sides()))