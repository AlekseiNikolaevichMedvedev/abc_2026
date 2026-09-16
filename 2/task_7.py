#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
def read_coordinates(point: str) -> float:
    while True:
        try:
            return float(input(f"Enter the coordinates of the point {point}: "))
        except ValueError:
            print(f"Value error. Try again.\n")

A = read_coordinates("A")
B = read_coordinates("B")
C = read_coordinates("C")

AC = abs(C-A)
BC = abs(B-C)

print(f"The length of AC is {AC}\n")
print(f"The length of BC is {BC}\n")
print(f"The sum of AC and BC is {AC+BC}\n")