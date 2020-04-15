class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.insert(0,0)
        flag=1
        for k in range(len(digits)-1,-1,-1):
            if digits[k]+flag==10:
                flag=1
                digits[k]=0
            else:
                digits[k]+=flag
                break
        if digits[0]==1:
            return digits
        else:
            return digits[1:]
