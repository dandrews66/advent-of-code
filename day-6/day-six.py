def is_zero(number):
    if number == 0:
          return True  
    return False

with open('input.txt') as f:
    data = list(f.read().splitlines())[0].split(',')
    data = list(map(int, data))

    day = 0
    max_days = 80
    
    while day < max_days:
        print(day)
        num_spawned = len(list(filter(is_zero, data)))
        new_laternfish = [8 for x in range(0, num_spawned)]

        data = [x - 1 for x in data] #subtract days
        data = [x if x != -1 else 6 for x in data] #Replace 0 with 6
        data.extend(new_laternfish) #Add new laternfish

        day = day + 1

    print(len(data))