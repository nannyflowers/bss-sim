from base_classes.item import Item
from data.bees import bee_templates
import random as r

class Egg(Item):
    def __init__(self, name, odds):
        super().__init__(name)
        self.odds = odds
    
    def hatch(self, player):
        if len(self.odds) != 5:  print("Invalid odds");  return

        player.inventory.remove(self.name, 1)

        seed = r.random()
        total_chance = 0

        for i in range(len(self.odds)):
            chance = self.odds[i]
            total_chance += chance / 100

            if seed >= total_chance:    continue

            else:
                match i:
                    case 0:
                        player.add_bee(bee_templates["Basic Bee"].copy())
                return
    
    def copy(self):
        return Egg(self.name, self.odds.copy())