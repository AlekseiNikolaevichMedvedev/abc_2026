# #todo: Напишите лямбду функцию которая возвращает максимальное число
# # из 2 переданных чисел


# # #todo: Для каждого значения из списка mass получите
# # # список проверок(True или False) вхождений значений в диапазон от 1 до 130
# mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]

# #todo: Отсортируйте список с помощью функции filter()
# # и получите итоговый список только нечетных значений
# list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
# print(list(filter( lambda val:  val%2 != 0,  list_ )))


# #todo: Отсортируйте список по расширению ".mp3"
# files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']

# 1. Лямбда: максимум из двух чисел
max_of_two = lambda a, b: a if a > b else b
print(max_of_two(3, 7))


# 2. Проверка вхождения каждого значения в диапазон 1..130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
checks = [1 <= v <= 130 for v in mass]
print(checks)


# 3. Только нечётные значения через filter()
list_ = [10, 11, 14, 25, 33, 36, 100, 101]
print(list(filter(lambda val: val % 2 != 0, list_)))


# 4. Сортировка по расширению ".mp3"
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
sorted_files = sorted(files, key=lambda name: name.endswith('.mp3'), reverse=True)
print(sorted_files)