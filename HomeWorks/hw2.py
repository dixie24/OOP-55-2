class Heroes:
    def __init__(self, name, hp, power_points, heal):
        self.name = name
        self.hp = hp
        self.power_points = power_points
        self.heal = heal
    def action(self,):
        print(f"{self.name} hero")

    def health(self):
        print(f"{self.hp} уровень здоровья")

    def attack(self):
        self.power_points -= 50
        print(f"{self.name} атаковала! Осталось {self.power_points} очков силы из 100")

    def healing(self, to):
        to.hp += self.heal
        print(self.name, "исцеляет", to.name)

    def status(self):
        print(f"Наименование персонажа {self.name}, \n"
              f"Здоровье: {self.hp}, \n"
              f"Очков сил: {self.power_points},\n"
              f"Исцеление(хилка): {self.heal}")

class Archer(Heroes):

    def __init__(self, name, hp, power_points, heal, arrows, precision):
        super().__init__(name, hp, power_points, heal)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 30:
            self.arrows -= 1
            hit = self.precision > 10

            if hit:
                print("hit successfully")
            else:
                print("missed")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} пополнил(а) запас стрел")



    def status(self):
        print(f"Наименование персонажа {self.name}, \n"
              f"Здоровье: {self.hp}, \n"
              f"Очков сил: {self.power_points},\n"
              f"Исцеление(хилка): {self.heal}, \n" 
              f"{self.arrows} количество стрел, {self.precision} Точность попадания")

hero_1 = Heroes("Mercy healer", 140, 260, 30)
hero_2 = Heroes("Nier", 120, 80, 0)



hero_1.attack()
hero_1.status()
print("\n")
hero_2.attack()
hero_2.status()

print("\n")
hero_1.healing(hero_2)
hero_2.health()
hero_2.status()

print("\n")
archer_1 = Archer("Mia", 80, 70, 0, 60, 5)


archer_1.attack()
print("\n")
archer_1.status()