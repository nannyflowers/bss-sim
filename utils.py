def calculate_egg_cost(n):
    base = 1000
    cost = base

    i = 0
    while i < n-1:
        cost = 1.5 * cost + base/(i + 1)
        i += 1
    
    if cost > 10000000: return 10000000
    return int(round(cost + 0.1, 0))