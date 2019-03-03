from pythonmodule import calculate_area


class Circle:

    owner = 'Anurag Anmol'
    pi = 3.14

    def __init__(self, radius, name='default'):
        self .name = name
        self.radius = radius

    def get_radius(self):
        print(calculate_area(self.radius))
        print(Circle.pi * self.radius * self.radius)


dog = Circle(radius=23, name='My Circle')
dog.get_radius()
