from Figure import Figure


class Triangle(Figure):
    name = "triangle"

    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        if not (self.is_triangle()):
            raise ValueError

    def is_triangle(self):
        maximum_side = max(self.first_side, self.second_side, self.third_side)
        triangle_array = [self.first_side, self.second_side, self.third_side]
        triangle_array.remove(maximum_side)
        return maximum_side < triangle_array[0] + triangle_array[1]

    @property
    def perimeter(self):
        return (self.first_side + self.second_side + self.third_side) / 2

    @property
    def area(self):
        return (self.perimeter * (self.perimeter - self.first_side) * (self.perimeter - self.second_side) *
                (self.perimeter - self.third_side)) ** 0.5

