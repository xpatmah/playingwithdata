# import sys
#
# print(sys.executable)


class Dog:

    def __init__(self, name='default_name', bread='default'):
        self.bread = bread
        self.name = name

    def get_bread(self):
        return self.bread

    def get_name(self):
        return self.name


dog = Dog('Rocky', 'BullDog')
print(dog.bread)




