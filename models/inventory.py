class Inventory:
    def __init__(self):
        self.items = {}
    
    def add(self, item, count=1):
        if item.name in self.items:
            self.items[item.name]["count"] += count
        else:
            self.items[item.name] = {"item": item, "count": count}
    
    def remove(self, item_name, count=1):
        if item_name in self.items:
            self.items[item_name]["count"] -= count
            if self.items[item_name]["count"] <= 0:
                del self.items[item_name]
    
    def get(self, item_name):
        if self.items.get(item_name):
            return self.items[item_name]["item"]
        else:   return False

    def count(self, item_name):
        if self.items.get(item_name):
            return self.items[item_name]["count"]
        else:   return False
    
    def print_inventory(self):
        for name, data in self.items.items():
            print(f"{name}: {data['count']}")
