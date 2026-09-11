from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name="Hero", health=100)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

hero.equip(weapon=iron_sword)

hero.drop_weapon()
hero.drop_weapon()

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()
