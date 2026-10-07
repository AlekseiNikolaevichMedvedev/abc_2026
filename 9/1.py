import csv
import os
import random
from datetime import datetime

# Импорт словаря согласно условию задачи
from db import DICT_DEFENITION_WORD


class Yakubovich:

    def __init__(self):
        self.player_name = input("Введите ваше имя: ").strip()
        self.word = ""
        self.mask = ""
        self.session_id = ""

    def _generate_key(self):
        return f"session-{int(datetime.now().timestamp())}"

    def print_menu(self):
        print("\n--- Меню игры ---")
        print("1 — Новая партия")
        print("2 — Загрузка сохраненной партии")
        print("3 — Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            self.word = random.choice(list(DICT_DEFENITION_WORD.keys()))
            self.mask = "#" * len(self.word)
            self.session_id = self._generate_key()
            print(f"Загадано слово из {len(self.word)} букв!")
            print(f"Подсказка: {DICT_DEFENITION_WORD[self.word]}")
            self.start_game()
        elif choice == "2":
            self.load_game()
        elif choice == "3":
            self.end_game()
        else:
            print("Некорректный ввод. Возврат в меню.")
            self.print_menu()

    def start_game(self):
        while "#" in self.mask:
            print(f"Текущая маска: {list(self.mask)}")
            user_input = input(
                "Введите букву (или '2' для сохранения): "
            ).strip()

            if user_input == "2":
                self.save_game()
                print("Игра продолжается...")
                continue

            if not user_input:
                print("Вы ничего не ввели.")
                continue

            letter = user_input[0].lower()

            if letter in self.word:
                new_mask = ""
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        new_mask += letter
                    else:
                        new_mask += self.mask[i]
                self.mask = new_mask
                print("Есть такая буква!")
            else:
                print("Такой буквы нет.")

        print(f"Поздравляем! Вы отгадали слово: {list(self.mask)}")
        self.end_game()

    def save_game(self):
        """Сохранение партии в save_game.csv в формате дата|сессия|имя|слово|маска."""
        file_exists = os.path.exists("save_game.csv")

        with open(
            "save_game.csv", mode="a", encoding="utf-8", newline=""
        ) as file:
            writer = csv.writer(file, delimiter="|")
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow(
                [
                    current_date,
                    self.session_id,
                    self.player_name,
                    self.word,
                    self.mask,
                ]
            )
        print("Игра успешно сохранена!")

    def load_game(self):
        if not os.path.exists("save_game.csv"):
            print("Файл сохранений пуст или не существует.")
            self.print_menu()
            return

        player_saves = []
        with open(
            "save_game.csv", mode="r", encoding="utf-8", newline=""
        ) as file:
            reader = csv.reader(file, delimiter="|")
            for row in reader:
                if row:
                    player_saves.append(row)
        current_player_saves = []
        for index, save in enumerate(player_saves):
            if save[2] == self.player_name:
                current_player_saves.append((index, save))

        if not current_player_saves:
            print(f"Сохранений для игрока {self.player_name} не найдено.")
            self.print_menu()
            return

        print(f"\nСохранения игрока {self.player_name}:")
        for display_idx, (file_idx, save) in enumerate(current_player_saves):
            print(
                f"{display_idx} — Дата: {save[0]} | Сессия: {save[1]} | Маска: {save[4]}"
            )

        try:
            choice_idx = int(
                input("Введите номер сохранения для загрузки: ").strip()
            )
            if 0 <= choice_idx < len(current_player_saves):
                _, selected_save = current_player_saves[choice_idx]
                self.session_id = selected_save[1]
                self.word = selected_save[3]
                self.mask = selected_save[4].replace(
                    "\n", ""
                )
                print(f"Партия восстановлена! Подсказка: {DICT_DEFENITION_WORD.get(self.word, 'Нет подсказки')}")
                self.start_game()
            else:
                print("Неверный номер. Возврат в меню.")
                self.print_menu()
        except ValueError:
            print("Ошибка ввода. Ожидалось число. Возврат в меню.")
            self.print_menu()

    def end_game(self):
        """Завершение игры."""
        print("Спасибо за игру в Поле чудес! До свидания!")
        exit()


if __name__ == "__main__":
    game = Yakubovich()
    game.print_menu()