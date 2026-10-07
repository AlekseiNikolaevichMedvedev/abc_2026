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


product = Product("Book", 10)
print(product.price)
product.price = -5
print(product.price)