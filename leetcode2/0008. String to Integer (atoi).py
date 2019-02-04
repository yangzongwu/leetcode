class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        left=0
        while left<len(str) and str[left]==' ':
            left+=1
        if left==len(str) or str[left] not in '+-1234567890':
            return 0
        if str[left] in '+-':
            if left==len(str)-1 or str[left+1] not in '1234567890':
                return 0
        right=left+1
        while right<len(str) and str[right] in '1234567890':
            right+=1
        rep=int(str[left:right])
        if rep>2**31-1:
            return 2**31-1
        if rep<-2**31:
            return -2**31
        return rep
        
