#PROBLEM: Longest Palindromic Substring



#CODE:

class Solution:
    
    def longestPalindrome(self, s):
	# Handles Leetcode's edge cases
        if s == "" or s == len(s) * s[0]:
            return s

        p = s[0]
        l = 1

        for i in range(len(s)):
            for j in range(len(s), 0, -1):
                w = s[i:j]

               # Is 'w' longer than our current longest palindrome 'p'?
                if w == w[::-1] and len(w) > l:
                        p = w
                        l = len(w)
        return p
        
	
	
#CODENO.2: work well with no err like Time exceed err
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = ''
        n = [len(s) - 1]

        for diff in range(1, len(s)):
            n.append(n[0] + diff)
            n.append(n[0] - diff)

        for i in n:
            if (min(i + 1, 2 * len(s) - 1 - i) <= len(longest_str)):
                break

            if i % 2 == 0:
                left, right = (i // 2) - 1, (i // 2) + 1
            else:
                left, right = i // 2, (i // 2) + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > len(longest_str):
                longest_str = s[left + 1: right]

        return longest_str
	
