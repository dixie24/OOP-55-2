class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_info(self):
        return (f"Название товара: {self.__name} \n"
        f"Цена: {self.__price} som \n"
        f"В наличий {self.__stock} штук")


    def info_stock(self):
        return self.__stock


    def buy(self, quantity):

        if quantity < self.__stock:
            self.__stock -= quantity
            return True
        return False


    def the_price(self):
        return self.__price

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        if product.buy(quantity):
            self.products.append((product, quantity))
        else:
            print(f"Нету столько количества, в наличий только {product.info_stock()} штук")

    def checkout(self):
        sum(product.the_price() * quantity for product, quantity in self.products)
        for product, quantity in self.products:
            print(f"{product.get_info()}, Количество: {quantity}, {product.the_price() * quantity}")

phone = Product("Телефон", 22000, 3)
pc = Product("Gaming PC", 120_000, 6)

cart = Cart()
cart.add_product(phone, 2)
cart.checkout()

print("\n")

cart.add_product(pc, 4)
cart.checkout()