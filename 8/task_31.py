#  Инкапсуляция и property
# # todo: Класс "Температура"
# # Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# # Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# # Внутренне температура должна храниться только в Цельсиях.

# # celsius (get, set) - работа с Цельсиями.
# # fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# # kelvin (get, set) - при установке конвертирует значение в Цельсии.

# # Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")

class Temperature:

    def __init__(self, celsius: float):
        self._celsius = float(celsius)

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self._celsius = (float(value) - 32) * 5 / 9

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float):
        self._celsius = float(value) - 273.15

if __name__ == '__main__':
    t = Temperature(25)

    print(t.celsius)
    print(t.fahrenheit)
    print(t.kelvin)

    t.fahrenheit= 32
    print(t.celsius)