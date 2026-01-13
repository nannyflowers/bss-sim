from data.fields import field_data, size_multiplier
from data.tools import tool_data

class CollectPollen:
    def __init__(self, amount, colour="any", field="any"):
        self.amount = amount
        self.colour = colour
        self.field = field

    def calc_bee_effective_rate(self, bee, expected_pollen_per_flower, colour_multiplier):
        base_rate = bee.pollen / bee.p_interval
        return base_rate * expected_pollen_per_flower * colour_multiplier

    def process(self, player):
        
        if self.field == "any":
            expected_pollen_per_flower = 1
        else:
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

        tool_colour_multiplier = sum(
            prob * tool.multipliers[colour]
            for colour, prob in field_data[self.field].colour.items()
        )

        total_tool_rate = base_tool_rate * expected_pollen_per_flower * tool_colour_multiplier

        total_rate = total_tool_rate + total_bee_rate
        return self.amount / total_rate