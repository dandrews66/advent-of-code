import numpy as np

class BingoSetup():

    def __init__(self, file):
        with open(file) as f:
            self.chosen_numbers = list(map(int, f.readline().split(',')))
            self.boards = []

            cards = list(f.read()[1:].split('\n\n'))
            for card in cards:
                self.boards.append(BingoBoard([list(map(int, j.split())) for j in card.split('\n')]))
            
            
            
            # remaining_lines = f.readlines()[1:]
            # print(remaining_lines)

    def get_boards(self):
        return self.boards

    def get_chosen_numbers(self):
        return self.chosen_numbers



class BingoBoard():
    def __init__(self, matrix):
        self.matrix = matrix
        
    def mark(self, number):
        for i in range(0, len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == number:
                    self.matrix[i][j] = None

    def print(self):
        print(np.matrix(self.matrix))
    
    def get_sum(self):
        sum = 0
        for row in self.matrix:
            for element in row:
                if element != None:
                    sum += element
                
        return sum
    
    def isWinner(self):
        ## Check horizontals
        for row in self.matrix:
            count = 0
            for element in row:
                if element != None:
                    break; 
                else:
                    count += 1
            
            if count == len(self.matrix):
                return True
            
                    
        ## Check verticals
        for i in range(0, len(self.matrix[0])):
            count = 0
            for row in self.matrix:
                element = row[i]
                if element != None:
                    break; 
                else:
                    count += 1
            
            if count == len(self.matrix):
                return True        
                
        
        return False
