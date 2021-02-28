'''Problem : Unique Paths II '''

#CODE :

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        # COmpute the dimensions
        rowLen = len(obstacleGrid)
        colLen = len(obstacleGrid[0])
        # Compute the number of possible path in the first column
        possiblePathCount = [0] * rowLen
        possiblePathCount[0] = 1
        # Compute the number of possible path in the remaining column
        for colIndex in range(colLen):
            if obstacleGrid[0][colIndex] == 1:
                # This cell is obstacle. Impossible to reach here.
                possiblePathCount[0] = 0
            for rowIndex in range(1, rowLen):
                if obstacleGrid[rowIndex][colIndex] == 1:
                    # This cell is obstacle. Impossible to reach here.
                    possiblePathCount[rowIndex] = 0
                else:
                    # We may reach here by moving from either left or upper cell.
                    possiblePathCount[rowIndex] += possiblePathCount[rowIndex-1]
        return possiblePathCount[-1]
