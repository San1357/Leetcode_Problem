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
      
   

#CODE :


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        self.match = {}
        if len(s1) + len(s2) != len(s3):
            return False
        return self.isInterleaveRecu(s1, s2, s3, 0, 0, 0)

    def isInterleaveRecu(self, s1, s2, s3, a, b, c):
        if repr([a, b]) in self.match.keys():
            return self.match[repr([a, b])]

        if c == len(s3):
            return True

        result = False
        if a < len(s1) and s1[a] == s3[c]:
            result = result or self.isInterleaveRecu(s1, s2, s3, a + 1, b, c + 1)
        if b < len(s2) and s2[b] == s3[c]:
            result = result or self.isInterleaveRecu(s1, s2, s3, a, b + 1, c + 1)

        self.match[repr([a, b])] = result

        return result

if __name__ == "__main__":
    print (Solution().isInterleave("a", "", "a"))
    print (Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print (Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))

      
