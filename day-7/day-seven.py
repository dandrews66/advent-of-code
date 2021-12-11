import numpy as np

with open('input.txt') as f:
    data = [int(x) for x in list(f.read().splitlines())[0].split(',')]

    min, max = np.min(data), np.max(data)

    fuel_spent = np.min([sum([np.abs(x - i) for x in data]) for i in range(min, max)])

    print(round(fuel_spent))
    

