class Food:
    def __init__(self, name : str, category : str, hunger_reduction : int, energy_boost : int, happiness_boost : int, is_toxic = False, is_spicy = False):
        self.category = category
        self.hunger_reduction = hunger_reduction
        self.energy_boost = energy_boost
        self.happiness_boost = happiness_boost
        self.is_toxic = is_toxic
        self.is_spicy = is_spicy
    

kibble_bowl = Food(
    name="Kibble Bowl",
    category="Standard",
    hunger_reduction=20,
    energy_boost=0,
    happiness_boost=5,
)

prime_steak = Food(
    name="Prime Steak",
    category="Meat",
    hunger_reduction=45,
    energy_boost=10,
    happiness_boost=25,
)

tuna_fillet = Food(
    name="Tuna Fillet",
    category="Fish",
    hunger_reduction=30,
    energy_boost=5,
    happiness_boost=20,
)

golden_apple = Food(
    name="Golden Apple",
    category="Fruit",
    hunger_reduction=15,
    energy_boost=15,
    happiness_boost=10,
)

fire_pepper = Food(
    name="Fire Pepper",
    category="Elemental",
    hunger_reduction=10,
    energy_boost=35,
    happiness_boost=0,
    is_spicy=True,
)

rotten_scraps = Food(
    name="Rotten Scraps",
    category="Waste",
    hunger_reduction=10,
    energy_boost=-15,
    happiness_boost=-30,
    is_toxic=True,
)