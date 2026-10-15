class NotificationSender:
    def send(self, message: str, user) -> None:
        raise NotImplementedError


class EmailSender(NotificationSender):
    def send(self, message: str, user) -> None:
        print(f"Email для {user.name} | Образовательная платформа | {message}")


class SMSSender(NotificationSender):
    def send(self, message: str, user) -> None:
        print(f"SMS для {user.name} | {message[:50]}")


class PushSender(NotificationSender):
    def send(self, message: str, user) -> None:
        print(f"Push для {user.name} | 🎓 {message}")


class User:
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications


def notify_user(user: User, message: str) -> None:
    for sender in user.preferred_notifications:
        sender.send(message, user)


if __name__ == '__main__':
    maria = User("Мария", [EmailSender(), PushSender()])
    notify_user(maria, "Блок аналитики начинается с 27 октября!")