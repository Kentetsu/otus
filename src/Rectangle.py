from src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, h_side, w_side):
        if not (type(h_side) == int or type(h_side) == float and type(w_side) == int or type(w_side) == float):
            raise ValueError
        self.h_side = h_side
        self.w_side = w_side

    @property
    def perimeter(self):
        return 2*(self.h_side + self.w_side)

    @property
    def area(self):
        return self.h_side * self.w_side

