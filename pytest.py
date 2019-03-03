class Circle:

    owner = 'Anurag Anmol'
    pi = 3.14

    def __init__(self, radius, name='default'):
        self .name = name
        self.radius = radius

    def get_radius(self):
        print(Circle.pi * self.radius * self.radius)


dog = Circle('My Circle')
print(dog.get_radius())
