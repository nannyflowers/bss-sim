import math

class ConvertPollen:
    def __init__(self, amount="all"):
        self.amount = amount
    
    def process(self, player):

        if len(player.bees) == 0:   print("Player has no bees, therefore can't convert."); return 99999999999999999999

        convert_rate = sum(
            bee.convert_amount / bee.c_interval
            for bee in player.bees
        )
        
        if self.amount == "all":    self.amount = player.pollen

        convert_time =  self.amount / convert_rate
        return convert_time