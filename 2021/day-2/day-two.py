
x = 0
depth = 0
aim = 0

with open('input.txt') as f:
    line = f.readline()

    while(line):
        instructions = line.split()
        
        print(instructions)
        if(len(instructions) > 1):
            direction = instructions[0]
            amount = int(instructions[1])

            if(direction == 'forward'):
                x += amount
                depth += (aim * amount)
            elif(direction == 'up'):
                aim -= amount
            elif(direction == 'down'):
                aim += amount
        
        print("horz: {}".format(x))
        print("depth: {}".format(depth))
        print("aim: {}".format(aim))        
        line = f.readline()

print("x: {}".format(x))
print("depth: {}".format(depth))
print("total: {}".format(depth*x))
    
    
