# # Инкапсуляция и property
# # todo: Класс "Товар" (Защита от отрицательной цены)
# # Создайте класс Product. У него есть свойства name (простая строка) и price.
# # При установке цены проверяйте, что она не отрицательная.
# # Если пытаются установить отрицательную цену, устанавливайте 0.


# # Пример использования
# product = Product("Book", 10)
# print(product.price)  # 10
# product.price = -5
# print(product.price)  # 0

# Создайте класс Product(name, price) со свойствами name и price для чтения и записи. 
# При отрицательной цене устанавливайте 0, в том числе при создании товара.
# Добавьте пример: создайте Product('Book', 10), выведите цену, присвойте цене -5 и выведите её снова.

class Product():
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            self._price = 0.0
        else:
            self._price = float(value)

if __name__ == '__main__':
    product = Product("Book", 10)
    print(product.price)
    product.price = -5
    print(product.price)