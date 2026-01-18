from base_classes.field import Field

size_multiplier = {
    "single": 1.0,
    "double": 2.0,
    "triple": 3.0
}

field_data = {
    "sunflower": Field("Sunflower", {"single": 0.9, "double": 0.1, "triple": 0}, {"white": 0.7, "red": 0.15, "blue": 0.15}),
    "dandelion": Field("Dandelion", {"single": 0.85, "double": 0.15, "triple": 0}, {"white": 0.85, "red": 0.05, "blue": 0.10}),
    "mushroom": Field("Mushroom", {"single": 0.90, "double": 0.10, "triple": 0}, {"white": 0.30, "red": 0.70, "blue": 0.0}),
    "blue_flower": Field("Blue Flower", {"single": 0.90, "double": 0.10, "triple": 0.0}, {"white": 0.30, "red": 0.0, "blue": 0.70}),
    "clover": Field("Clover", {"single": 0.50, "double": 0.50, "triple": 0.0}, {"white": 0.34, "red": 0.33, "blue": 0.33}),
    "strawberry": Field("Strawberry", {"single": 0.20, "double": 0.75, "triple": 0.05}, {"white": 0.25, "red": 0.75, "blue": 0.0}),
    "spider": Field("Spider", {"single": 0.10, "double": 0.80, "triple": 0.10}, {"white": 1.0, "red": 0.0, "blue": 0.0}),
    "bamboo": Field("Spider", {"single": 0.20, "double": 0.75, "triple": 0.05}, {"white": 0.25, "red": 0.0, "blue": 0.75}),
    "pineapple": Field("Pineapple", {"single": 0.20, "double": 0.50, "triple": 0.30}, {"white": 0.90, "red": 0.05, "blue": 0.05}),
    "stump": Field("Stump", {"single": 0.0, "double": 0.0, "triple": 1.0}, {"white": 0.1777, "red": 0.0667, "blue": 0.7556}),
    "cactus": Field("Cactus", {"single": 0.0, "double": 0.50, "triple": 0.50}, {"white": 0.0698, "red": 0.4651, "blue": 0.4651}),
    "pumpkin": Field("Pumpkin", {"singe": 0.0, "double": 0.30, "triple": 0.70}, {"white": 0.60, "red": 0.20, "blue": 0.20}),
    "pine_tree": Field("Pine Tree", {"single": 0.05, "double":0.45, "triple": 0.50}, {"white": 0.15, "red": 0.0, "blue": 0.85}),
    "rose": Field("Rose", {"single": 0.05, "double": 0.45, "triple": 0.5}, {"white": 0.15, "red": 0.85, "blue": 0.0}),
    "mountain_top": Field("Mountain Top", {"single": 0.0, "double": 0.0, "triple": 1.0}, {"white": 0.0, "double": 0.50, "triple": 0.50}),
    "pepper": Field("Pepper", {"single": 0.0, "double": 0.0, "triple": 1.0}, {"white": 0.15, "red": 0.85, "blue": 0.0}),
    "coconut": Field("Coconut", {"single": 0.0, "double": 0.0, "triple": 1.0}, {"white": 0.8763, "red": 0.0825, "blue": 0.0412})
}