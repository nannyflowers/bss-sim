class EventManager:
    def __init__(self, player):
        self.player = player

        self.events = []
        self.running = False
        self.total_time = 0
    
    def queue_event(self, event):
        self.events.append(event)
    
    def start(self):
        if self.running == True:    return

        self.running = True
        while self.running:
            self.total_time += self.events[0].process(self.player)
            self.events.pop(0)

            if len(self.events) == 0:   self.running = False
    
    def stop(self):
        self.running = False
    
    def print_total_time(self):
        print(self.total_time)
    
    def harvest(self, player, amount, field="any", colour="any"):
        runs = amount // player.capacity
        leftover = amount % player.capacity

        from events.collect_pollen import CollectPollen
        from events.convert_pollen import ConvertPollen

        for i in range(runs):
            self.queue_event(CollectPollen(colour=colour, field=field))
            self.queue_event(ConvertPollen())
        
        if leftover == 0:   return
        
        self.queue_event(CollectPollen(leftover, colour, field))
        self.queue_event(ConvertPollen())