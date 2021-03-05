'''Problem: Combinations '''

#CODE : 

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(n,k,start):
            # base case: need only one element
            if k == 1:
                return [[i] for i in range(start,n+1)]
            result = []
            for i in range(start,n-k+2):
                L = helper(n,k-1,i+1)
                for j in L:
                    result.append([i]+j)
            return result
        
        return helper(n,k,1)
