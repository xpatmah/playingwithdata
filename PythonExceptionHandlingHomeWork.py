for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except TypeError:
        print("ValueError")

x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print('Zero Division Error')
finally:
    print('All Done')


def ask(num):
    return num * num


while True:
    try:
        print(ask(int(input("Enter The number\n"))))
    except ValueError:
        print("Wrong input please try again")
        continue
    else:
        break
    finally:
        print('All Done')
