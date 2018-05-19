__author__ = 'vetalalien'

import random

class Warrior:
    def __init__(self, name):
        self.__health__ = 100.0
        self.name = name
        pass
    def get_damage(self, damageValue):
        self.__health__ -= damageValue
    def isAlive(self):
        return self.__health__ > 0
    def set_damage(self, warrior, damageValue):
        warrior.get_damage(damageValue)

war1 = Warrior(input("Введите имя первого воина:"))
war2 = Warrior(input("Введите имя второго воина:"))

deathWarrior = None
while deathWarrior == None:
    warriors = [war1, war2]
    index = random.randrange(2)
    strikingWarrior = warriors[index]
    warriors.pop(index)
    damagedWarrior = warriors.pop(0)
    damageValue = random.randrange(21)
    print(strikingWarrior.name, "бьёт", damagedWarrior.name)
    strikingWarrior.set_damage(damagedWarrior, damageValue)
    print("Игрок", damagedWarrior.name, "получает урон в количестве", damageValue)
    if not damagedWarrior.isAlive():
        deathWarrior = damagedWarrior
print("\n", end = "")
print(deathWarrior.name, "был убит,", "победил", strikingWarrior.name)