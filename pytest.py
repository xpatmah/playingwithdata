#from pythonmodule import calculate_area
#from mainpackage import mymainscript
from mainpackage.mainsubpackage import mysubscript


class Circle:

    owner = 'Anurag Anmol'
    pi = 3.14

    def __init__(self, radius, name='default'):
        self .name = name
        self.radius = radius

    def get_radius(self):
        # print(mymainscript.calculate_area(self.radius))
        print(mysubscript.calculate_area(self.radius))
        print(Circle.pi * self.radius * self.radius)


dog = Circle(radius=23, name='My Circle')
dog.get_radius()
