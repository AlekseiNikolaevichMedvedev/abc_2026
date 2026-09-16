# todo: Определить в коде переменные:
# 1. Целочисленного типа
# 2. Вещественного типа
# 3. Логического типа
# 4. Строкового типа
# 5. Пустого типа
# Вывести их типы.

var_list = {
    'integer': 123,
    'float': 3.14,
    'boolean': False,
    'string': "fvasdjfvbasdjkfbasdkufbsadf",
    'None': None
}

type_list = { x: type(var_list[x]) for x in var_list.keys() }

for x in var_list.keys():
    y = var_list[x]
    print(f"Переменная {var_list[x]} имеет тип {type_list[x]}")