'''Problem : Gray Code '''

#CODE :

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            for n in reversed(result):
                result.append(1 << i | n)
        return result
