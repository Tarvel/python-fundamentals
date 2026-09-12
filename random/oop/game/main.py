from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name="Hero", health=100)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

hero.equip(weapon=iron_sword)


while True:
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
    