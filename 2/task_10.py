# todo: 10.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 10.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.


# 10.1 Проверка, является ли число A четным
while True:
    try:
        A = int(input("input A: "))
        if not isinstance(A, int):
            print('Type error. Enter int.')
        is_even = A % 2 == 0
        print(is_even)
        break
    except ValueError:
        print('Value error. Enter a number.')

# 10.2 Проверка, является ли число A нечетным
# Число нечетное, если остаток от деления на 2 не равен 0
while True:
    try:
        A = int(input("input A: "))
        if not isinstance(A, int):
            print('Type error. Enter int.')
        is_even = A % 2 != 0
        print(is_even)
        break
    except ValueError:
        print('Value error. Enter a number.')