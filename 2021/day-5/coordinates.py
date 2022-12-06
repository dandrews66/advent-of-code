class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def equals(self, point):
        return self.x == point.x and self.y == point.y

class Line():

    def __init__(self, a, b):
        self.pointA = a
        self.pointB = b

        self.x1 = self.pointA.x
        self.y1 = self.pointA.y
        self.x2 = self.pointB.x
        self.y2 = self.pointB.y

        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1

    def get_slope(self):
        return 0 if self.dx == 0 else self.dy/self.dx

    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

    
        
