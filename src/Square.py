from src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side):
        if not (type(side) == int or type(side) == float):
            raise ValueError
        self.side = side

    @property
    def perimeter(self):
        return 4*self.side

    @property
    def area(self):
        return self.side ** 2

