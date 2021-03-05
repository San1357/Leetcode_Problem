'''Problem: SEARCH A TWO D MATRIX '''

#CODE :

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        ''' Flatten the matrix into 1-dimension list. Then this
            question turns to be binary search question.
        '''
        rowLen = len(matrix)
        colLen = len(matrix[0])
        begin, end = 0, rowLen * colLen - 1
        while begin <= end:
            mid = (begin + end) // 2
            # Convert to 1D binary search question
            midCell = matrix[mid//colLen][mid%colLen]
            if midCell > target:    end = mid - 1
            elif midCell < target:  begin = mid + 1
            else:                   return True
        return False
