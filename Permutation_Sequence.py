'''Problem : Permutation Sequence '''

#CODE :

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        numberPermutations = []
        count = 1
        numberPermutations.append(count)
        for i in range(1, n):
            count *= i
            numberPermutations.append(count)
        numbers = []
        for i in range(1, n+1):
            numbers.append(i)
        solution=[]
        count = k-1
        for i in range(0,n):
            position = count//numberPermutations[n-i-1]
            count -= position * numberPermutations[n-i-1]
            element = numbers.pop(position)
            solution.append(str(element))
        return "".join(solution)
