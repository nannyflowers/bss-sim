class Bee:
    def __init__(self, name, energy, speed, attack, pollen, p_interval, convert_amount, c_interval):
        self.name = name
        self.energy = energy
        self.speed = speed
        self.attack = attack
        self.pollen = pollen
        self.p_interval = p_interval
        self.convert_amount = convert_amount
        self.c_interval = c_interval
    
    def copy(self):
        return Bee(self.name, self.energy, self.speed, self.attack, self.pollen, self.p_interval, self.convert_amount, self.c_interval)