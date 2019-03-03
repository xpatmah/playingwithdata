def add(one, two):
    return one+two


while True:
    try:
        one = int(input("Enter the number \n"))
    except ValueError:
        print('not a number')
        continue
    else:
        print("No Error")
        break
    finally:
        print("After the exception")


