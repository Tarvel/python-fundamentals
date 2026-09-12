from food import kibble_bowl
class Pet:
    def __init__(self, name, breed, hunger, energy, happiness, waste_count):
        self.name = name
        self.breed = breed
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.waste_count = waste_count
        self.is_alive = True
        self.food = kibble_bowl
    
    def feed(self, food):
        self.hunger += self.food.hunger_reduction
        self.energy += self.food.energy_boost
        self.happiness += self.food.happiness_boost
        self.waste_count += 2

        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))

        print (f"You have fed {self.name}, your {self.breed}.\n[+] Hunger: {self.hunger}\n[+] Energy: {self.energy}\n[+] Happiness: {self.happiness}")
    
    def clean(self):
        self.waste_count = 0
        self.happiness += 10

        print (f"You have cleaned")



class Dragon(Pet):
    def __init__(self, name : str, waste_count=0, breed= "Dragon", hunger=50, energy=60, happiness=50):
        super().__init__(name=name, waste_count=waste_count, breed=breed, hunger=hunger, energy=energy, happiness=happiness)

    def feed(self, food):
        super().feed(food=food)
        self.refuse_fruit = (self.food.category == "Fruit")
        if self.refuse_fruit:
            self.hunger = self.hunger
            self.energy =self.energy
            self.happiness = self.happiness

    
    def breathe_fire(self):
        self.energy -= 20
        self.hunger += 15
        self.waste_count = 0

        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))