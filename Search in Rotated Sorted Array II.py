'''Problem: Search in Rotated Sorted Array II '''

#CODE :

class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l  < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
        
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid 
                else: 
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid 
            else:
                l += 1 # move until you can decide which side mid locates
        return nums[l] == target
