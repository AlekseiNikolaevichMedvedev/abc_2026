# #todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# # Для этого считайте список всех строк при помощи метода readlines().

# #Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

if __name__ == '__main__':
    filename = './inverted_sort.txt'

    with open(file=filename, mode='w', encoding='utf-8') as file:
        file.write('Beautiful is better than ugly.\n')
        file.write('Explicit is better than implicit.\n')
        file.write('Simple is better than complex.\n')
        file.write('Complex is better than complicated.\n')

    with open(file=filename, mode='r+', encoding='utf-8') as file:
        lines = file.readlines()
        reversed_lines = reversed(lines)
        file.seek(0, 2)
        file.writelines(reversed_lines)

