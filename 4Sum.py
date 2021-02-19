'''
Problem: 4sum

#CODE:

class Solution(object):
    ### my own code, run time is O(N*N)
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #nums.sort()
        length = len(nums)
        d = dict()
        for i in range(length):
            for j in range(i+1, length):
                val = nums[i] + nums[j]
                if val in d:
                    d[val].append((i,j))
                else:
                    d[val] = [(i,j)]
        res = set()
        for k in d:
            val = target - k
            if val in d:
                vlist = d[val]
                klist = d[k]
