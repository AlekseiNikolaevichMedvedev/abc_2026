import  random

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


gm = Game()
gm2 = Game()
gm.start()
gm2.start()