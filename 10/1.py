class LearningMaterial:
    def __init__(self, title, author, duration_minutes):
        self.title = title
        self.author = author
        self.duration_minutes = duration_minutes

    def display_info(self):
        return print(f"{self.title} | {self.author} | {self.duration_minutes}")

    def get_difficulty(self) -> str:
        return "Средняя"


class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_minutes, video_quality, subtitles_available):
        super().__init__(title, author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available


class Article(LearningMaterial):
    def __init__(self, title, author, duration_minutes, word_count, reading_level):
        super().__init__(title, author, duration_minutes)
        self.word_count = word_count
        self.reading_level = reading_level

    def get_difficulty(self) -> str:
        if self.word_count < 1000:
            return "Лёгкая"
        elif self.word_count <= 3000:
            return super().get_difficulty()
        else:
            return "Сложная"


class Quiz(LearningMaterial):
    def __init__(self, title, author, duration_minutes, questions_count, passing_score):
        super().__init__(title, author, duration_minutes)
        self.questions_count = questions_count
        self.passing_score = passing_score

    def get_difficulty(self) -> str:
        if self.passing_score > 80:
            return "Высокая"
        else:
            return super().get_difficulty()

if __name__ == '__main__':
    video   = VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True)
    article = Article("Глубокое обучение", "Анна Петрова", 10, 1200, "advanced")
    quiz    = Quiz("Проверка знаний", "Платформа", 20, 10, 75)

    for material in (video, article, quiz):
        print(f"{material.title}: {material.get_difficulty()}")