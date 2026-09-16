#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.
from decimal import Decimal, InvalidOperation, Overflow, DivisionByZero

class Calc:
    def __init__(self, x, y):
        try:
            self.x = Decimal(x)
            self.y = Decimal(y)
        except InvalidOperation:
            print("Wrong format!")

    def add(self):
        return 