''' Interleaving String '''
#CODE :


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > len(s2):
            return self.isInterleave(s2, s1, s3)
        match = [False for i in range(len(s1) + 1)]
        match[0] = True
        for i in range(1, len(s1) + 1):
            match[i] = match[i -1] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            match[0] = match[0] and s2[j - 1] == s3[j - 1]
            for i in range(1, len(s1) + 1):
                match[i] = (match[i - 1] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i] and s2[j - 1] == s3[i + j - 1])
        return match[-1]
      
      
      
      # or SOLUTION 2
      
      
