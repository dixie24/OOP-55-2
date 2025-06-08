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

