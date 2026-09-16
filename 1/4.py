# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130

# Задачу решить без функций max и прочих.

def dum_max(vals):
    m=[]
    if vals:
        first, *rest = vals
        m = first
        if rest:
            for x in rest:
                if x>m:
                    m=x
    else:
        m=[]
    return m

def report(vals_in):
    print(f"Входные данные: {vals_in}")
    print(f"Ответ: {dum_max(vals=vals_in)}")

report([])
report([10,15,2])
report([77,9,130])
