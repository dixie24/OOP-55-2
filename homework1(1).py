class Animal:

    def __init__(self, name, breed, kind, category, weight_in_kg):
        # Атрибуты класса
        self.name_of_animal = name
        self.breed_of_animal = breed
        self.kind_of_animal = kind
        self.category_of_category = category
        self.weight_of_animal = weight_in_kg

    # class method методы класса
    def name_of_the_animal(self):
            return f"{self.name_of_animal}"

    def breed(self):
        return f"{self.breed_of_animal} breed of animal"

    def kind(self):
        return f"{self.kind_of_animal} kind of"

    def categ(self):
        return f"{self.category_of_category} category"

    def kgs(self):
        return f"{self.weight_of_animal} kilograms animal"


tiger = Animal("tiger", "siberian", "mammals(млекопитающие)", "wild(дикие)", 300)
dog = Animal("dog","pitbull", "mammals(млекопитающие)", "working dog(cлужебные)", 25)


print(tiger.name_of_the_animal())
print(tiger.breed())
print(tiger.kind())
print(tiger.categ())
print(tiger.kgs())
