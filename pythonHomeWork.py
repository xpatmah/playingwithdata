class Line:

    def __init__(self, coordinates_x, coordinates_y):
        self.coordinates_x = coordinates_x
        self.coordinates_y = coordinates_y

    def distance(self):
        x1, y1 = self.coordinates_x
        x2, y2 = self.coordinates_y
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slop(self):
        x1, y1 = self.coordinates_x
        x2, y2 = self.coordinates_y
        return (y2 - y1) / (x2 - x1)


lines = Line((2, 3), (3, 4))
print(lines.distance())
print(lines.slop())
