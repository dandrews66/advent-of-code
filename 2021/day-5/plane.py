from coordinates import Point
import numpy as np

class Plane():

    def __init__(self, max_size):
        self.plane = [[0 for i in range(max_size)] for j in range(max_size)]
    
    def add_line(self, line):
        
        #Cap the increment distance at +1/-1
        dx = line.get_dx()
        if dx != 0:
            dx = 1 if dx > 0 else -1
        
        dy = line.get_dy()
        if dy != 0:
            dy = 1 if dy > 0 else -1
        
        point = line.pointA
        finish = line.pointB

        while not point.equals(finish):
            self.plane[point.y][point.x] += 1
            x = point.x + dx
            y = point.y + dy
            
            point = Point(x, y)

        self.plane[finish.y][finish.x] += 1

    def print(self):
        print(np.matrix(self.plane))

    def get_num_overlaps(self):
        count=0
        for row in self.plane:
            for element in row:
                if element > 1:
                    count += 1
        return count

