def add(num1, num2) -> float:
    return num1 + num2


def sub(num1, num2) -> float:
    return num1 - num2


def multiply(num1, num2) -> float:
    return num1 * num2


def divide(num1, num2) -> float:
    if num2 == 0:
        print("can't divide by zero ")
        return 0.0
    return num1 / num2


print("enter -1 to exit ")
while 1:
    a = int(input('enter the first number : '))
    b = int(input('enter the second number : '))
    if a == -1:
        break
    operation = int(input("enter operation \t\n1.add \t\n2.sub \t\n3.multiply \t\n4.division\t\nenter: "))
    match operation:
        case 1:
            print("addition is ", add(a, b))
        case 2:
            print("Substraction is ", sub(a, b))
        case 3:
            print("Multiplicaton is ", multiply(a, b))
        case 4:
            if divide(a, b) != 0.0:
                print("Division is ", divide(a, b))
