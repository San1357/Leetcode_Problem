'''
Problem: Generate Parantheses''' 

# CODE :

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        values = []
        self.generate(values, '', 0, n, 0)
        return values
    def generate(self, values, s, idx, n, opn):
        if idx >= n*2:
            # print(s)
            values.append(s)
            return
        # print(opn)
        if opn < n:
            self.generate(values, s+'(', idx+1, n, opn+1)
            if opn * 2 > idx:
                self.generate(values, s+')', idx+1, n, opn)
        elif opn == n:
            self.generate(values, s+')', idx+1, n, opn)
