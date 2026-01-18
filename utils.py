from data.fields import field_data

def calculate_egg_cost(n):
    base = 1000
    cost = base

    i = 0
    while i < n-1:
        cost = 1.5 * cost + base/(i + 1)
        i += 1
    
    if cost > 10000000: return 10000000
    return int(round(cost + 0.1, 0))

def calculate_best_field(player, colour):
    bee_count = len(player.bees)

    if colour == "any":
        if bee_count < 5:
            return "clover"
        elif bee_count < 10:
            return "bamboo"
        elif bee_count < 15:
            return "pineapple"
        elif bee_count < 25:
            return "cactus"
        elif bee_count < 35:
            return "mountain_top"
        else:
            return "pepper"
    
    if colour == "red":
        if bee_count < 5:
            return "mushroom"
        elif bee_count < 15:
            return "strawberry"
        elif bee_count < 35:
            return "rose"
        else:
            return "pepper"
    elif colour == "blue":
        if bee_count < 5:
            return "blue_flower"
        elif bee_count < 15:
            return "bamboo"
        else:
            return "pine_tree"
    else:
        if bee_count < 5:
            return "dandelion"
        else:
            return "spider"