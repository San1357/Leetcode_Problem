'''Problem :First Missing Positive '''

#CODE:

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # Place number i in the place A[i-1]
        index = 0
        while index < len(A):
            # Already in the place
            if index + 1 == A[index]:       index += 1
            # Nowhere to swap
            elif A[index] <= 0:             index += 1
            # Nowhere to swap
            elif A[index] > len(A):         index += 1
            # No effect to swap
            elif A[index] == A[A[index]-1]: index += 1
            else:
                swapI, swapJ = index, A[index]-1
                A[swapI], A[swapJ] = A[swapJ], A[swapI]
        # Try to find the first i, such that i + 1 != A[i]
        for index in xrange(len(A)):
            if index + 1 != A[index]:   return index + 1
        # If all positive integers appears, the first missing
        # one would be the next integer
        return len(A) + 1
