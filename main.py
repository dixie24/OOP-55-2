from xml.etree.ElementTree import QName


class Animal:

    def __init__(self, name, breed, kind, category, weight_in_kg):

        self.name_of_animal = name
        self.breed_of_animal = breed
        self.kind_of_animal = kind
        self.category_of_category = category
        self.weight_of_animal = weight_in_kg


    def name_of_the_animal(self):
            return f"{self.name_of_animal}"


tiger = Animal("tiger", "siberian", "mammals(млекопитающие)", "wild(дикие)", 300)
dog = Animal("dog","pitbull", "mammals(млекопитающие)", "working dogs(cлужебные)", 25)


# print(tiger.name_of_the_animal())
# print(tiger.breed_of_animal)
# print(tiger.kind_of_animal)
# print(tiger.category_of_category)
# print(tiger.weight_of_animal)


print(dog.name_of_the_animal())
print(dog.breed_of_animal)
print(dog.kind_of_animal)
print(dog.category_of_category)
print(dog.weight_of_animal)

# class Hero:
#
#     # конструктор класса
#     def __init__(self, name="john", lvl=1, hp=10):
#         # Атрибуты класса
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     # class method методы класса
#     def base_action(self):
#         if self.lvl == 100:
#             return f"{self.name} super Hero"
#         return f"{self.name} base Hero"
#
#     def added(self):
#         pass
#
#
#
# # Объект класса|Экземпляр класса
# kirito = Hero(name="Kirito", hp=123)
# asuna = Hero("asuna", 100, 1000)
# array = [1,2,3]
# tuples = (1,2,3)
# integer = 123
# sting = "123"
#
# print(kirito.lvl)