# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
#
# Преобразуйте переменную flag в Boolean
# flag = 1
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
#
# Преобразуйте значение 0 и 1 в Boolean
#
# Преобразуйте False в строку


def print_answer(var_in=None, var_out=None):
    print(f"""Значение входной переменной и тип: {var_in}, {type(var_in)}.
Значение преобразованной переменной и тип: {var_out}, {type(var_out)}.""")

var_in = "23"
var_out = int("23")
print_answer(var_in=var_in, var_out=var_out)

var_in = "23abc"
import re
def get_int_from_str(text):
    match = re.search(r'\d+',text)
    number = None
    if match:
        number = int(match.group())
    return number

# Либо решение руками
# var_out = int(str[:2])
var_out = get_int_from_str(var_in)
print_answer(var_in=var_in, var_out=var_out)

var_in = "123abc"
var_out = bool(var_in)
print_answer(var_in=var_in, var_out=var_out)

var_in = 1
var_out = bool(var_in)
print_answer(var_in=var_in, var_out=var_out)

var_in = "Privet"
var_out = bool(var_in)
print_answer(var_in=var_in, var_out=var_out)

var_in = ""
var_out = bool(var_in)
print_answer(var_in=var_in, var_out=var_out)

var_in = 1
var_out = bool(var_in)
print_answer(var_in=var_in, var_out=var_out)

var_in = 0
var_out = bool(var_in)
print_answer(var_in=var_in, var_out=var_out)

var_in = False
var_out = str(var_in)
print_answer(var_in=var_in, var_out=var_out)