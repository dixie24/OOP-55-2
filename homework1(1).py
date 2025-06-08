class Person:

    def __init__(self, name, age, city):
        # Атрибуты класса
        self.name = name
        self.age = age
        self.city = city


    def introduce(self):
            return f"Привет, меня зовут {self.name}, мне {self.age} лет и я живу в городе {self.city}."

    def is_adult(self):
            if self.age >=18:
                return True
            else:
                return False


emir = Person("Эмир", 10, "Бишкек")
gulnaz = Person("Гульназ", 20, "Берлин")


print(emir.introduce())
print(emir.is_adult())
print(gulnaz.introduce())
print(gulnaz.is_adult())