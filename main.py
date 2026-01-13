from models.player import Player
from events.collect_pollen import CollectPollen

player = Player()
player.buy_basic_egg()
player.inventory.print_inventory()
player.hatch_egg("Basic Egg")
player.print_hive()

collect_pollen = CollectPollen(200, field="sunflower")
print(collect_pollen.process(player))