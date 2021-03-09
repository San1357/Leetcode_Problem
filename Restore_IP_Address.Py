'''Problem: Restore IP Address '''

#CODE :

class Solution:
    # @param s, a string
    # @return a boolean to indicate whether s is a valid IP address section.
    def restoreIpAddressesHelper(self,s):
        assert 0 < len(s) <= 3
        if len(s) == 1:                         return True
        elif len(s) == 2 and s[0] != "0":       return True
        else:
            if s[0] == "1":                     return True
            elif s[0] == "2":
                if s[1] in "01234":             return True
                elif s[1] == "5":
                    if s[2] in "012345":        return True
        return False
   
    def restoreIpAddresses(self, s):
        
        if not 4 <= len(s) <= 12:       return []
        result = []
        for i in range(1, len(s)-2):
           
            if i > 3:                   break
            for j in range(i+1, len(s)-1):
                
                if j - i > 3:           break
                for k in range(j+1, len(s)):
                    
                    if k - j > 3:       break
                    
                    if len(s) - k > 3:  continue
                    
                    if not self.restoreIpAddressesHelper(s[:i]):    continue
                    if not self.restoreIpAddressesHelper(s[i:j]):   continue
                    if not self.restoreIpAddressesHelper(s[j:k]):   continue
                    if not self.restoreIpAddressesHelper(s[k:]):    continue
                    
                    result.append(s[:i] + "." + s[i:j] + "." + s[j:k] +
                                  "." + s[k:])
        return result
