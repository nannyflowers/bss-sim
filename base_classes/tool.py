class Tool:
    def __init__(self, name, pps, multipliers={"white": 1, "red": 1, "blue": 1}):
        self.name = name
        self.multipliers = multipliers
        self.pps = pps