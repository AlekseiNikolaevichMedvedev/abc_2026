class WheelOfFortune:
    def __init__(self, word: str, lives: int = 5, guessed_letters=None):
        if not word:
            raise ValueError("Загаданное слово не может быть пустым")
        self.word = word.lower()
        self.lives = lives
        # Используем переданное множество или создаем новое
        self.guessed_letters = set(guessed_letters) if guessed_letters else set()

    @property
    def current_state(self) -> str:
        """Возвращает текущее состояние слова (например, я к * * * * * )"""
        return "".join([letter if letter in self.guessed_letters else "*" for letter in self.word])

    def guess_letter(self, letter: str) -> bool:
        """Обрабатывает отгадывание одной буквы"""
        if len(letter) != 1:
            raise ValueError("Нужно ввести ровно одну букву")
        
        letter = letter.lower()
        if letter in self.guessed_letters:
            return False  # Буква уже называлась, попытка не тратится

        self.guessed_letters.add(letter)

        if letter in self.word:
            return True
        else:
            self.lives -= 1
            return False

    @property
    def is_won(self) -> bool:
        """Проверяет, отгадано ли всё слово целиком"""
        return all(letter in self.guessed_letters for letter in self.word)

    @property
    def is_game_over(self) -> bool:
        """Проверяет, закончилась ли игра (победа или кончились жизни)"""
        return self.is_won or self.lives <= 0

    def to_dict(self):
        """Преобразует состояние игры в словарь для сохранения в сессию Flask"""
        return {
            'word': self.word,
            'lives': self.lives,
            'guessed_letters': list(self.guessed_letters)
        }

    @classmethod
    def from_dict(cls, data):
        """Восстанавливает объект игры из словаря сессии"""
        if not data:
            return cls(word="якубович", lives=5)
        return cls(
            word=data.get('word', 'якубович'),
            lives=data.get('lives', 5),
            guessed_letters=data.get('guessed_letters', [])
        )
