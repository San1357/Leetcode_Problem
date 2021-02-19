'''Problem: Valid Parantheses 



#CODE:


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        #use a stack -- refer to an answer
        pairs = {")": "(",
                 "}": "{",
                 "]": "["}

        for c in s:
            if(c in ["(", "{", "["]):
                stack.append(c)
            elif(len(stack) == 0 or pairs[c] != stack.pop()):
                return False

        return stack == []
