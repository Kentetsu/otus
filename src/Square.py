from Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side):
        self.side = side

    @property
    def perimeter(self):
        return 4*self.side

    @property
    def area(self):
        return self.side ** 2
