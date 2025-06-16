class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_info(self):
        print(f"Название товара: {self.__name} \n"
        f"Цена: {self.__price} som \n"
        f"В наличий {self.__stock} штук")

    def buy(self, quantity):

        if quantity < self.__stock:
            self.__stock -= quantity
            return True
        return False

laptop = Product("asus", 40000, 2)
smart_watches = Product("Samsung", 20000, 4)


# print(laptop.get_info())
# print(laptop.buy(1))
# laptop.get_info()

print("\n")

smart_watches.get_info()
smart_watches.buy(2)
print("\n")
smart_watches.get_info()