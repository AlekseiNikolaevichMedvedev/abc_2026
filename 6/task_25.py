#todo: Допишите для игры "Поле чудес" функции сохранения и загрузки игры через сериализацию.
# Данные сериализации записываются и сохраняются в файле.
import random
import pickle
import os

import random
import pickle
import os

class Game:
    def __init__(self):
        self._dict = {'False': 'Логическое значение', 'None': 'Пустой'}
        self.keys = list(self._dict.keys())
        self.ind = random.randint(0, len(self.keys) - 1)
        self.secret = self.keys[self.ind]
        self.mask = [' * '] * len(self.secret)

    def show_describe(self):
        """ Выводит описание слова  """
        print(self._dict[self.secret])

    def show_secret(self):
        """ Выводит слово """
        for val in self.mask:
           print(val, end="")

    def get_letter(self):
        letter = input("\n Введите букву:")
        return letter

    def check_letter(self, letter):
        for ind, val in enumerate(self.secret):
            if val.upper() == letter.upper():
                self.mask[ind] = f" {letter} "

    def start(self):
        while ( " * " in self.mask):
            self.show_describe()
            self.show_secret()
            letter = self.get_letter()
            self.check_letter(letter)


FILENAME = "game_save.dat"

def save_game(game_obj):
    with open(FILENAME, 'wb') as f:
        pickle.dump(game_obj, f)
    print("\n Игра успешно сохранена!")

def load_game():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'rb') as f:
            print("\n Игра загружена с места сохранения!")
            return pickle.load(f)
    print("\n Файл сохранения не найден. Начата новая игра.")
    return Game()


def play_game(game_obj):
    current_game = game_obj
    while " * " in current_game.mask:
        current_game.show_describe()
        current_game.show_secret()
        letter = current_game.get_letter()
        if letter.strip() == '\\save':
            save_game(current_game)
            continue    
        current_game.check_letter(letter)
    print(f"\nВы победили! Cлово: {current_game.secret}")


if __name__ == "__main__":
    choice = input("1 - Новая игра\n2 - Загрузить сохранение\nВыберите действие: ")
    if choice == "2":
        gm = load_game()
    else:
        gm = Game()
    play_game(gm)



    