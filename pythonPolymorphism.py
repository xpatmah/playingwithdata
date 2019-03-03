class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Animal is created")

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating '+self.name)


class Dog(Animal):

    def __init__(self):
        # Not Mandatory to call
        Animal.__init__(self, name='Dog', age=10)
        print('Dog is created')

    def who_am_i(self):
        print('I am a dog')


class Cat(Animal):

    def __init__(self):
        # Not Mandatory to call
        Animal.__init__(self, name='cat', age=12)
        print('Dog is created')

    def who_am_i(self):
        print('I am a dog')


dog = Dog()
dog.eat()
dog.who_am_i()