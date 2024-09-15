money_box = 0
class Enemy:
    def __init__(self, name, health, money, slab_damage):
        self.name = name
        self.health = health
        self.money = money
        self.slab_damage = slab_damage
        
    def slab_take_damage(self, amount):
        global money_box #лол почему нужно вызывать переменную тут а не в if, не я понимаю но хз стрём какойто
        self.health -= amount
        if self.health<=0:
            money_box = money_box + self.money
            print(f"{self.name} Мёртв.\nC него выпало {self.money} монет!")
        else: 
            print(f"{self.name} получил {amount} урона. Здоровье: {self.health}")
  
   
    def is_alive(self):
        return self.health > 0 
Hero = Enemy("Герой", 20, 5, 1)
enemy1 = Enemy("Гоблин", 100,20, 5)
enemy2 = Enemy("Орк", 150,30,4)

enemy1.slab_take_damage(Hero.slab_damage)
enemy2.slab_take_damage(150)

if enemy1.is_alive():
    print(f"{enemy1.name} все еще жив!")
else:
    print(f"{enemy1.name} мертв.")

print(money_box)