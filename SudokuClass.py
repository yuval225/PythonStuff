import numpy as np
import random
    
class Suduko:
    
    numberList = [1,2,3,4,5,6,7,8,9]
    
    def __init__(self):
        self.board = np.zeros((9,9),dtype=int)
        self.counter = 0 


    def validBoard(self, row,col,insertedNumber):    
        #Check for duplicates in row
        for num in self.board[row]:
            if num == insertedNumber:
                return False
        
        #Check for duplicates in col
        for num in self.board[:,col]:
            if num == insertedNumber:
                return False
        
        #Check for duplicates in cubic
        cubicStartRow = 3 * (row//3)
        cubicStartCol = 3 * (col//3)
        for i in range(0,3):
            for j in range(0,3):
                if self.board[cubicStartRow + i][cubicStartCol+j] == insertedNumber:
                    return False
        return True


    def CreateBoard(self):
        self.board = np.zeros((9,9),dtype=int)
        for i in range(15):
            row = random.randint(0,8)
            col = random.randint(0,8)
            num = random.randint(1,9)
            while not self.validBoard(row,col,num) or self.board[row][col] != 0:
                row = random.randint(0,8)
                col = random.randint(0,8)
                num = random.randint(1,9)
            self.board[row][col] = num
        sudukoCopy = self.board.copy()
        if not self.SolveSuduko():
            self.CreateBoard()
        else:
            self.board = sudukoCopy
    
    def SolveSuduko(self):
        self.counter
        self.board
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for n in range(1,10):
                        if self.validBoard(row,col,n):
                            self.board[row][col] = n
                            if self.SolveSuduko():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def isBoardFull(self):
        return not 0 in self.board

newSuduko = Suduko()
newSuduko.CreateBoard()
print(newSuduko.SolveSuduko())
print(newSuduko.board)
