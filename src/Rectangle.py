from Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, h_side, w_side):
        self.h_side = h_side
        self.w_side = w_side

    @property
    def perimeter(self):
        return 2*(self.h_side + self.w_side)

    @property
    def area(self):
        return self.h_side * self.w_side
