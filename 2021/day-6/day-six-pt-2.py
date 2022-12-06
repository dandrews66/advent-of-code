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
        num_zeroes = digits[0]
        digits.rotate(-1) #Shift each digit of the array down an index. ie number of 5's now becomes the number of 4s. The 0 index rotates around and becomes the 8 index
        digits[6] += num_zeroes #Each zero gets set to 6
        
        day = day + 1

    print(sum(digits))