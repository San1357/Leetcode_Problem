'''Problem : VALID PALINDROME '''
#CODE :


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) < 2:          return True
        head, tail = 0, len(s)-1
        while head < tail:
            if not s[head].isalnum():
                head += 1
            elif not s[tail].isalnum():
                tail -= 1
            else:
                if s[head].lower() == s[tail].lower():
                    head += 1
                    tail -= 1
                else:
                    return False
        return True
