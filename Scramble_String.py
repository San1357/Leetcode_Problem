'''Problem :Scramble String '''

#CODE : 

class Solution:
    def __init__(self):
        self.map = {} # key: (s1, s2), value: bool

    def isScramble(self, s1, s2):
        if (s1, s2) in self.map:
            return self.map[(s1, s2)]

        if len(s1) != len(s2):
            self.map[(s1, s2)] = False
            return False

        if s1 == s2:
            self.map[(s1, s2)] = True
            return True

        
        if sorted(s1) != sorted(s2):
            self.map[(s1, s2)] = False
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True

            if self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                return True

        
        self.map[(s1, s2)] = False
        return False
