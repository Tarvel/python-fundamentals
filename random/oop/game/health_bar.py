import os

os.system("")


class HealthBar():
    symbol_remaining = 
    def __init__(entity, length: int = 20, is_coloured: bool = True, colour: str = ""):
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health
        self.is_coloured = is_coloured
        self.colour = colour