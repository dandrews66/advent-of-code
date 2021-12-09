from collections import deque

with open('input.txt') as f:
    data = list(f.read().splitlines())[0].split(',')
    data = list(map(int, data))
    
    digits = deque([0,0,0,0,0,0,0,0,0]) #counting number of digits (0,1,2,3,4,5,6,7,8)
    
    #Init the digit list
    for x in data:
        digits[x] += 1
    
    day = 0
    max_days = 256
    
    while day < max_days:
        num_to_spawn = digits[0]
        
        digits.rotate(-1)
        digits[6] += num_to_spawn #Each zero gets set to 6
        
        day = day + 1

    print(sum(digits))