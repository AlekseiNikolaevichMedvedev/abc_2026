class Product:
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


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    @property
    def total_price(self) -> float:
        return sum(product.price for product in self.products)



order = Order()
book = Product("Book", 10)
pen = Product("Pen", 2)
order.add_product(book)
order.add_product(pen)
print(order.total_price)
