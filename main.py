from models.player import Player
from events.collect_pollen import CollectPollen
from events.convert_pollen import ConvertPollen
from models.event_manager import EventManager

import time as t

player = Player()
event_manager = EventManager(player)

player.buy_basic_egg()
player.hatch_egg("Basic Egg")

event_manager.harvest(player, 3500000)

event_manager.start()
event_manager.print_total_time()