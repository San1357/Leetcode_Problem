
'''Problem: find-first-and-last-position-of-element-in-sorted-array '''



#CODE:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start, end = 0, len(nums)-1
        left, right = -1, -1
        while start + 1 < end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid
            elif target < nums[mid]:
                end = mid
            elif target == nums[mid]:
				#if mid == target, then go left and right to finalize the range.
                left, right = mid, mid
                while left >0:
                    if nums[left-1]==target:
                        left -=1
                    else:
                        break
                while right < len(nums)-1:
                    if nums[right+1]==target:
                        right +=1
                    else:
                        break
                return [left, right]
		#If exit binary search, then the target must be in between left or right, or the target not in the array.
        if nums[start]==target and nums[end]==target:
            left,right = start,end
                        
        elif nums[end]==target and nums[start]!=target:
            left,right = end, end
            
        elif nums[start]==target and nums[end]!=target:
            left,right = start, start                
        return [left, right]
