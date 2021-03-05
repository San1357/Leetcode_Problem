'''Problem : Subset '''

#CODE : 

class Solution(object):
    def subsets(self, nums):
        def helper(i, combination):
            answer.add(tuple(combination))
            if i>=len(nums): return
            helper(i+1, combination+[nums[i]])
            helper(i+1, combination)

        answer = set()
        helper(0, [])
        return [list(combination) for combination in answer]
