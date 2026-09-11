class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animal):
    pass

class Mouse(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")
print(dog.sleep(), cat.eat(), dog.is_alive)