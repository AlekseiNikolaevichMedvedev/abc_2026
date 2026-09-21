#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).

seasons = ['зима','весна','лето','осень']

while True:
    user_input = input("Введите номер месяца (число от 1 до 12):").strip()
    if user_input.isdigit():
        month = int(user_input)
        if 1<=month<=12:
            print(f"Время года: {seasons[(month % 12)//3]}")
            break
        else:
            print(f"Ошибка диапозона.")
    else:
        print("Ошибка! Введите число корректно.")