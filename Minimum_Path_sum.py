'''Problem : Minimum Path '''

#CODE :

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        """
        time = space = O(rows*cols)
        """
        rows, cols, dp = len(grid), len(grid) and len(grid[0]), defaultdict(lambda : sys.maxsize)
        for r,c in product(range(rows), range(cols)):
            dp[(r,c)] = grid[r][c] + ((r or c) and min(dp[(r-1,c)], dp[(r,c-1)]))
        return rows and cols and dp[(rows-1,cols-1)]
