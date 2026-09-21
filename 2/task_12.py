# todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм,
#  4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M в этих единицах (вещественное число).
#  Вывести массу данного тела в килограммах
from decimal import Decimal, InvalidOperation

UNIT_NAMES = {
    1: "килограмм",
    2: "миллиграмм",
    3: "грамм",
    4: "тонна",
    5: "центнер"
}

MASS_CONVERSION= {
    1: Decimal(1.0),
    2: Decimal(1e-6),
    3: Decimal(1e-3),
    4: Decimal(1e3),
    5: Decimal(1e2)
}

while True:
    try:
        print("Доступные единицы измерения:")
        for num, name in UNIT_NAMES.items():
            print(f"  {num} — {name}")

        unit_number = int(input("Введите номер единицы массы: "))
        if unit_number in MASS_CONVERSION:
            break
        print(f"Ошибка: выберите номер от 1 до {len(UNIT_NAMES)}. Попробуйте снова.\n")
    except ValueError:
        print("Ошибка: введите целое число.\n")

unit_name = UNIT_NAMES[unit_number]
while True:
    try:
        mass = Decimal(input(f"Введите массу тела в единицах '{unit_name}': "))
        if mass >= 0:
            break
        print("Ошибка: масса не может быть отрицательной. Попробуйте снова.\n")
    except InvalidOperation:
        print("Ошибка: некорректный ввод")

result = mass*MASS_CONVERSION[unit_number]

print("\n--- Результат конвертации---")
print(f"Исходная масса: {mass.normalize()} {unit_name}")
print(f"Масса в килограммах: {result.normalize()} кг")



