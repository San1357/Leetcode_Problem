'''Problem : SPIRAL MATRIX '''

#CODE :

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.counter = 1
        self.top, self.bottom, self.left, self.right = 0, n-1, 0, n-1
        self.res = [[0]*n for _ in range(n)]
        while self.counter <= n*n:
            self.tr()
            self.td()
            self.tl()
            self.tu()
        return self.res
        
    def tr(self):
        temp = self.left
        while temp <= self.right:
            self.res[self.top][temp] = self.counter
            self.counter += 1
            temp += 1
        self.top += 1
    
    def td(self):
        temp = self.top
        while temp  <= self.bottom:
            self.res[temp][self.right] = self.counter
            self.counter += 1
            temp += 1
        self.right -= 1
            
    def tl(self):
        temp = self.right
        while temp >= self.left:
            self.res[self.bottom][temp] = self.counter
            self.counter += 1
            temp -= 1
        self.bottom -= 1
    
    def tu(self):
        temp = self.bottom
        while temp >= self.top:
            self.res[temp][self.left] = self.counter
            self.counter += 1
            temp -= 1
        self.left += 1
