'''Problem:  search-insert-position '''


#CODE :

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        ''' A variant of the binary search algorithm
            If target is in A, return the position of its first
                occurrence.
            Otherwise, rethurn the position of the first element,
                which is larger than target.
        '''
        begin = 0
        end = len(A) - 1
        insertPos = 0
        while begin <= end:
            mid = (begin + end) // 2
            if A[mid] == target:
                # Target found
                return mid
            elif A[mid] > target:
                end = mid - 1
                insertPos = mid
            else:
                begin = mid + 1
                insertPos = mid + 1
        return insertPos
