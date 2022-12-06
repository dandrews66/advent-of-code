import numpy as np

with open('input.txt') as f:
    data = [int(x) for x in list(f.read().splitlines())[0].split(',')]
    
    min, max = np.min(data), np.max(data)

    # Lol
    fuel_spent = np.min([sum([( ((x ** 2) + x )/ 2 ) for x in [np.abs(x - i) for x in data]]) for i in range(min, max)])

    print(round(fuel_spent))
    

