class Book:

    def __init__(self, title='', author='', pages=1):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return self.author + ' ' + self.title + ' ' + str(self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('This book has been deleted')


buk = Book("Vaibhav Pandey", "For a change", 123)
print(str(buk))
del(buk)
