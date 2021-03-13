''' Problem :  Distinct Subsequences '''

#CODE : 

class Solution:
   
    def numDistinct(self, S, T):
        cache = [0] * (len(T)+1)
        cache[0] = 1
        for indexS in range(len(S)):
            pre = cache[0]
            for indexT in range(len(T)):
                current = cache[indexT+1]
                if S[indexS] == T[indexT]:
                    cache[indexT+1] += pre
                pre = current
        return cache[-1]
