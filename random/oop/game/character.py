from weapon import fists
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists

    
    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print (f"{self.name} dealt an attack {self.weapon.damage} damage to {target.name} with {self.weapon.name}")



class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon

    def equip(self, weapon: str):
        self.weapon = weapon
        self.health_bar = HealthBar(self, colour="green")
        print(f"{self.name} equipped {self.weapon.name}")
     
    def drop_weapon(self):
        old_weapon = self.weapon
        self.weapon = self.default_weapon
        if old_weapon == self.weapon:
            print(f"can't drop {self.default_weapon.name}, {self.name} is currently using {self.default_weapon.name}")
        else:
            print(f"{self.name} dropped {old_weapon.name} now using {self.default_weapon.name}")


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: str) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, colour="red")