import math

class Line: 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    # /
    def __truediv__(self, factor): 
        new_point1 = (self.point1 [0] / factor, self.point1[1] / factor)
        new_point2 = (self.point2 [0] / factor, self.point2[1] / factor)
        return Line(new_point1, new_point2)

    # //
    def __floordiv__(self, factor): 
        new_point1 = (self.point1 [0] // factor, self.point1[1] // factor)
        new_point2 = (self.point2 [0] // factor, self.point2[1] // factor)
        return Line(new_point1, new_point2)

    # len()
    def __len__(self): 
        distance_x = (self.point1[0] - self.point2[0]) ** 2
        distance_y = (self.point1[1] - self.point2[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)

    # ==
    def __eq__(self, other): 
        if not isinstance(other, Line):
            return False
        
        return self.point1 == other.point1 and self.point2 == self.point2

    # !=
    def __ne__(self, other): 
        return not self.__eq__(other)

    # >
    def __gt__(self, other): 
        return len(self) > len(other)

    # >=
    def __ge__(self, other): 
        return len(self) >= len(other)

    # <
    def __lt__(self, other): 
        return len(self) < len(other)

    # <=
    def __lt__(self, other): 
        return len(self) <= len(other)

line1 = Line((10, 5), (20, 9))
line2 = Line((10, 3), (20, 9))
print(line1 < line2)
print(line1 > line2)
