'''Problem : Triangle '''

#CODE :


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            row = triangle[i]
            prev_row = triangle[i-1]
            for j, x in enumerate(row):
                left_sum = x + (prev_row[j-1] if (j-1) > -1 else float('inf'))
                right_sum = x + (prev_row[j] if j < len(prev_row) else float('inf'))
                row[j] = min(left_sum, right_sum)
        
        
        return min(triangle[-1])
