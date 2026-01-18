from data.fields import field_data, size_multiplier
from data.tools import tool_data
from events.convert_pollen import ConvertPollen
from utils import calculate_best_field
import math

class CollectPollen:
    def __init__(self, amount=None, colour=None, field=None):
        self.amount = amount
        self.colour = colour
        self.field = field

        if amount == None:  self.amount = "full"
        if colour == None:  self.colour = "any"
        if field == None: self.field = "any"

    def calc_bee_effective_rate(self, bee, expected_pollen_per_flower, colour_multiplier):
        base_rate = bee.pollen / bee.p_interval
        return base_rate * expected_pollen_per_flower * colour_multiplier

    def process(self, player):
        
        if self.amount == "full" or self.amount > player.capacity:
            self.amount = player.capacity - player.pollen
        
        if self.field == "any":
            self.field = calculate_best_field(player, self.colour)
        
        expected_pollen_per_flower = sum(
            prob * size_multiplier[size]
            for size, prob in field_data[self.field].quantity.items()
        )
        
        if self.colour == "any":
            colour_multiplier = 1
        else:
            colour_multiplier = field_data[self.field].colour[self.colour]

        total_bee_rate = sum(
            self.calc_bee_effective_rate(bee, expected_pollen_per_flower, colour_multiplier)
            for bee in player.bees
        )

        tool = player.tool
        base_tool_rate = tool.pps
        sample_field = self.field
        
        if self.field == "any":
            sample_field = "sunflower"

        tool_colour_multiplier = sum(
            prob * tool.multipliers[colour]
            for colour, prob in field_data[sample_field].colour.items()
        )

        total_tool_rate = base_tool_rate * expected_pollen_per_flower * tool_colour_multiplier
        total_rate = total_tool_rate + total_bee_rate
        total_pollen_time = self.amount / total_rate

        player.pollen = self.amount

        return total_pollen_time