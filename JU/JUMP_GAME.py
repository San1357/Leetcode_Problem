'''Problem : JUMP GAME '''

#CODE:


class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        m = 0
        i = 0
        res = 0
        if (len(A)<=1):
            return 0
        while i<len(A):
            m = max(m,A[i]+i)
            if m>0:
                res=res+1
            if m>=len(A)-1:
                return res
            tmp=0
            for j in range(i+1,m+1):
                if (j+A[j]>tmp):
                    tmp = j+A[j]
                    i = j
        return res
