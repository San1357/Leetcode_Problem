'''Problem : Unique Binary Search Trees '''

#CODE :


class Solution(object):


    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        solutions = [-1]*(n)
        return self.numUniqueBST(n, solutions)

    def numUniqueBST(self, n, solutions):

        if n < 0:
            return 0

        if n == 0 or n == 1:
            return 1

        possibilities = 0

        for i in range(0, n):
            if solutions[i] == -1:
                solutions[i] = self.numUniqueBST(i, solutions)
            if solutions[n-1-i] == -1:
                solutions[n-1-i] = self.numUniqueBST(n-1-i, solutions)
            possibilities += solutions[i]*solutions[n-1-i]
        return possibilities
