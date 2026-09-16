#todo: Дана сторона квадрата a. Найти его площадь S = a²
# Примечание: сторону квадрата получаем через функцию input().
from decimal import Decimal, InvalidOperation, Overflow
while True:
    try:
        user_input = input("Enter the side of the square:")
        x = Decimal(user_input)
        if x<=0:
            print("The side of the square cannot be less or equal than zero! Try again")
            continue
        s = x**2
        break
    except ValueError:
        print("Input is not a number. Try again.")
    except InvalidOperation:
        print("Enter valid number and try again")
    except Overflow:
        print("The number is too large and caused overflow. Enter smaller number.")
print(f"The area of the square is {s:f}.")
