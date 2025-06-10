# Наследование
# Полиморфизм

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} action")

class WarriorHero(Hero):
    def __init__(self, st):
        self.st = st

    def action(self):
        print("method warrior")

hero_1 = WarriorHero("wally", 21,200,2)
print(hero_1.action())
