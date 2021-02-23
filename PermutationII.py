'''Problem:
PERMUTATIONII '''



#CODE:


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 1:
            return [nums]
        output_list, output_list_copy, temp_output = [], [], []
        for num in nums:
            if not output_list:
                output_list = [[num]]
                continue
            for t in output_list:
                assigned, already_seen = False, None
                for j in range(len(t)+1):
                    if already_seen == num and assigned:
                        continue
                    t1 = t[0:j] + [num] + t[j:]
                    if j < len(t) and t[j] == num:
                        assigned, already_seen = True, num
                    temp_output.append(t1)
                output_list_copy += temp_output
                temp_output = []
            output_list = output_list_copy
            output_list_copy = []
        return output_list
