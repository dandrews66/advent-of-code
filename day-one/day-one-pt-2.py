from collections import deque

class WindowQueue():

    def __init__(self, size):
        self.q = deque([], maxlen=size)
        self.size = size
    
    def add(self, num):
        self.q.append(num)

    def sum(self):
        return sum(self.q)

    def full(self):
        return len(self.q) >= self.size

with open('input.txt') as f:
    counter = 0
    prev_sum = None

    q = WindowQueue(3)

    line = f.readline()
    
    while line:
        if(line != ''):
            q.add(int(line))

            if(q.full()):
                cur_sum = q.sum()

                if(prev_sum != None):
                    if(cur_sum > prev_sum):
                        print('{} greater than {}'.format(cur_sum, prev_sum))
                        counter += 1
                
                prev_sum = cur_sum 

        line = f.readline()

print(counter)
    
    
