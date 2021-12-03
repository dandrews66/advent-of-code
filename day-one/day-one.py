
prev_line = None 
counter = 0
with open('input.txt') as f:
    cur_line = f.readline()
    
    while cur_line:
        line_num = int(cur_line)

        if(prev_line != None):
            if(line_num > prev_line):
                counter += 1

        prev_line = line_num
        cur_line = f.readline()
        
print(counter)
    
    
