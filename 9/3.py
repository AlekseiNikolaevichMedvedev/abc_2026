class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self._password_hash = hash(password)
      
    @property
    def email(self) -> str:
        return self._email
      
    @email.setter
    def email(self, new_email: str):
        if "@" not in new_email:
            raise ValueError("Некорректный формат email: отсутствует символ '@'")
        self._email = new_email
      
    @property
    def password(self):
        raise AttributeError("Чтение пароля напрямую запрещено")
      
    @password.setter
    def password(self, new_password: str):
        self._password_hash = hash(new_password)
      
    def check_password(self, password: str) -> bool:
        return hash(password) == self._password_hash


user = User("test@example.com", "secret")

print(user.email)
print(user.check_password("secret"))
print(user.check_password("wrong"))
