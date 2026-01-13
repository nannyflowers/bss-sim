from utils import calculate_egg_cost
from models.inventory import Inventory
from data.eggs import egg_templates
from models.items import Egg
from data.tools import tool_data

class Player:
    def __init__(self):
        self.honey = 0
        self.pollen = 0
        self.capacity = 200
        self.eggs_bought = 1

        self.tool = tool_data["scooper"]
        self.bees = []
        self.inventory = Inventory()
    
    def add_honey(self, amount):
        self.honey += amount
    
    def add_bee(self, bee):
        self.bees.append(bee)
    
    def hatch_egg(self, egg_name):
        egg = self.inventory.get(egg_name)
        if egg and isinstance(egg, Egg):
            egg.hatch(self)
        else:
            print(f"Player doesn't own egg: {egg_name}")
        self.inventory.remove(egg)
    
    def buy_basic_egg(self):
        self.add_honey(0 - calculate_egg_cost(self.eggs_bought))
        self.eggs_bought += 1

        egg = egg_templates["Basic Egg"].copy()
        self.inventory.add(egg)
    
    def print_hive(self):
        for i in range(len(self.bees)):
            bee = self.bees[i]
            print(f"{i + 1}: {bee.name}")