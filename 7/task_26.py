# #todo Задача 1. Чтение матрицы, load_matrix(filename)
# # Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)

# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36


# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.

# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def load_matrix(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            raw_lines = [line.strip().split() for line in f if line.strip()]
        matrix = [[int(num) for num in line] for line in raw_lines]
        if not matrix:
            return False
        is_valid = all([len(row) == len(matrix[0]) for row in matrix])
        return matrix if is_valid else False
    except (FileNotFoundError, ValueError):
        return False

if __name__ == "__main__":
    FILENAME = "matrix.txt"

    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write("11 12 13 14 15 16\n")
        file.write("21 22 23 24 25 26\n")
        file.write("31 32 33 34 35 36\n")


    result = load_matrix(FILENAME)
    print(f"Матрица из файла: {result}")