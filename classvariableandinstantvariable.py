class Apple:
    name = 'Apple'

    def __init__(self, name):
        self.name = name
        self.value = len(name)

    def get_value(self):
        return self.value

    def get_name(self):
        value = self.get_value()
        return self.name+" "+str(value)

    @classmethod
    def sta_method(cls, name):
        return cls(name)

    @staticmethod
    def st_mathod():
        return Apple.sta_method('sdfsf')


apple = Apple("Instance")
print(apple.get_name())
print(Apple.name)
print(Apple.sta_method("ekrhweir"))
print(apple.st_mathod())
