''' Problem :Plus One  '''


#CODE :
 
 
 class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_num = ''
        for i in digits:
            str_num += str(i)
        new_num = int(str_num)+1
        
        digits_plus_one = []
        for j in str(new_num):
            digits_plus_one.append(int(j))
        return digits_plus_one
