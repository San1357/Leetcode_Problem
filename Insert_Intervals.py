'''Problem: Insert_Intervals '''

#CODE :

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        if not size: return [newInterval]
        def binarySearch(arr, left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid][0] < target: left = mid + 1
                else: right = mid
            return right
			
		# every internal before `left` has a start number smaller than newInterval[0]
        left = binarySearch(intervals, 0, size, newInterval[0]) 
		# every internal after `right` has a start number greater than newInterval[1]
        right = binarySearch(intervals, left, size, newInterval[1] + 0.1) - 1
		# part 2: [minVal, maxVal]
        minVal, maxVal = newInterval[0], newInterval[1]
        leftPart, rightPart = [], []
        for i in range(left - 1, -1, -1):
            if intervals[i][1] >= minVal: # if this interval can be merged as a prefix for part 2
                minVal = min(intervals[i][0], minVal)
            else:
                leftPart.append(intervals[i])
        leftPart.reverse()
        for i in range(max(right, 0), size): # the max(right, 0) avoids when no part 1 exists
            if intervals[i][0] <= maxVal: # if this interval can be merged as a suffix for part 2
                maxVal = max(intervals[i][1], maxVal)
            else:
                rightPart.append(intervals[i])
        return leftPart + [[minVal, maxVal]] + rightPart
