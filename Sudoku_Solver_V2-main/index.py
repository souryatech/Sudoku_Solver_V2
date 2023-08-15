board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]



board2 = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]



class Sudoku_Solver():
    #Finds first zero for first move to play
    #Checker if valid
    #AI function takes cell and for loop for every number for cell
    #for every number for cell, cell becomes the number in the real board
    #If the cell does not pass the checker, set cell as 0 and return None
    #If it does, set recursion for next cell
    def __init__(self,board):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)
    
    def print(self):
        print('---------------------')
        for x in self.board:
            spaces = ''
            for y in x:
                spaces += str(y) + ' '
            print('| ' + spaces + '|')
        print('---------------------')


            


    def first_zero(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return (i,j)
    
    def checker(self,number,cell):
        row,col = cell
        for x in self.board[row]:
            if x == number:
                return False
        for y in range(len(self.board)):
            if self.board[y][col] == number:
                return False
        #Coordinates for grid
        sectr = row // 3
        sectc = col // 3
        for i in range(3):
            for j in range(3):
                if self.board[sectr * 3 + i][sectc * 3 + j] == number:
                    return False
        return True
        
    def solve(self):
        if self.first_zero() == None:
            self.print()
        else:
            zero = self.first_zero()
            i, j = zero
            
            for num in range(1,10):
                if self.checker(num,zero):
                    self.board[i][j] = num
                    if self.solve() is not None:
                        return self.solve()
                    else:
                        self.board[i][j] = 0
            return None
            
            
            

Sudoku = Sudoku_Solver(board2)
Sudoku.print()
Sudoku.solve()
