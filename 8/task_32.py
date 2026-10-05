# # Инкапсуляция и property
# # todo: Класс "Пользователь" (Валидация email)
# # Создайте класс User. У него должны быть свойства email и password.
# # При установке email проверяйте, что строка содержит символ @ (простая валидация).
# # При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# # Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# # пароля сохраненному хешу.

# # Пример использования
# user = User("test@example.com", "secret")
# print(user.email)  # test@example.com
# # print(user.password) # AttributeError
# print(user.check_password("secret"))  # True
# print(user.check_password("wrong"))   # False