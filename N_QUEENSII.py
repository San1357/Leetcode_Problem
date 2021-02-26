'''Problem: N_QUEENSII '''

#CODE :

class Solution:
    # check if the queen can be placed on board[i][j]
    def check(self, i, j):
        for x, y in self.pieces:
            if i == x or y==j or abs(x-i) == abs(y-j):
                return False
        return True
    
    # dfs check for all poosible path and backtrack   
    def backtrack(self, i, j, count):
        # if all queens are placed -> valid solution
        if count == 0:
            #print(self.board)
            sol = [''.join(row) for row in self.board]
            self.result.append(list(sol))
            
        for x in range(i+1, self.n):
            for y in range(self.n):
                if self.check(x, y):
                    self.pieces.append((x, y))
                    self.board[x][y] = 'Q'
                    self.backtrack( x, y, count-1)
                    self.board[x][y] = '.'
                    self.pieces.pop()
                    
    def totalNQueens(self, n: int) -> int:
        # initialize board with '.'
        self.n = n
        self.board = [['.']*(n) for i in range(n)]
        self.pieces = []
        self.result = []
        # try for all columns in the first row as first piece
        for i in range(self.n):
            self.pieces.append((0, i))
            self.board[0][i] = 'Q'
            self.backtrack(0,i, self.n-1)
            self.board[0][i] = '.'
            self.pieces.pop()
                    
        # print(len(self.result))
        return len(self.result)
