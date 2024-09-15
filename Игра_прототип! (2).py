from time import sleep
from random import randint
# 1 библиотека добавляет фукцию для создания пауз, вторая для генерации чисел в указаном пределе

class Person:
    def __init__(self, name,Hp_Person, slab_damage, siln_damage, money):
        self.name = str(name)
        self.Hp_Person = int(Hp_Person)          
        self.slab_damage = int(slab_damage)          
        self.siln_damage = int(siln_damage)          
        self.money = int(money)          
#создание класса объекта с именем хилом сильной\слабой атакой и количеством денег

    def slab_take_damage(self , amount):
        self.Hp_Person -= amount
        if self.Hp_Person<=0:
            Hero.money += self.money
            print(f"{self.name} Мёртв.\nC него выпало {self.money} монет!")
        else: 
            print(f"{self.name} получил {amount} урона. Здоровье: {self.Hp_Person}")

    def siln_take_damage(self , amount):
        self.Hp_Person -= amount
        if self.Hp_Person<=0:
            Hero.money += self.money
            print(f"{self.name} Мёртв.\nC него выпало {self.money} монет!")
        else: 
            print(f"{self.name} получил {amount} урона. Здоровье: {self.Hp_Person}")

Hero = Person("Герой", 20, 1, 5, 3)


print( Hero.__dict__ )
    