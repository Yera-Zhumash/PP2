class Shape:
    def __init__(self):
        self.area_value = 0

    def area(self):
        return self.area_value

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.area_value = length * length