#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.
from decimal import Decimal, InvalidOperation, Overflow, DivisionByZero

class Calc:
    def __init__(self, x, y):
        self.is_valid = False
        try:
            self.x = Decimal(x)
            self.y = Decimal(y)
            self.is_valid = True
        except InvalidOperation:
            print("Ошибка: Неверный формат чисел!")

    def add(self):
        try:
            return self.x + self.y
        except Overflow:
            return "Ошибка: Переполнение при сложении!"

    def sub(self):
        try:
            return self.x - self.y
        except Overflow:
            return "Ошибка: Переполнение при вычитании!"

    def mul(self):
        try:
            return self.x * self.y
        except Overflow:
            return "Ошибка: Переполнение при умножении!"

    def div(self):
        try:
            return self.x / self.y
        except DivisionByZero:
            return "Ошибка: Деление на ноль!"
        except Overflow:
            return "Ошибка: Переполнение при делении!"

    def floordiv(self):
        try:
            return self.x // self.y
        except DivisionByZero:
            return "Ошибка: Деление на ноль!"

    def mod(self):
        try:
            return self.x % self.y
        except DivisionByZero:
            return "Ошибка: Деление на ноль!"

    def pow(self):
        try:
            return self.x ** self.y
        except Overflow:
            return "Ошибка: Результат возведения в степень слишком велик!"
        except InvalidOperation:
            return "Ошибка: Недопустимая операция возведения в степень!"


def get_valid_number(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return Decimal(user_input)
        except InvalidOperation:
            print("Ошибка ввода! Введите число")

if __name__=="__main__":
    x = get_valid_number("Введите первое число:")
    y = get_valid_number("Введите второе число:")

    calc = Calc(x,y)

    print("\n----Пример вычислений----")

    for attr_name in dir(calc):
        if not attr_name.startswith('__') and attr_name not in ('x','y'):
            method = getattr(calc, attr_name)
            if callable(method):
                description = method.__doc__ or attr_name
                result = method()
                print(f"{description}: {result}")