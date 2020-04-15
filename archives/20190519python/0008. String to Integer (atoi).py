class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        left=0
        while left<len(str) and str[left]==' ':
            left+=1
        if left==len(str):
            return 0
        if str[left] not in "+-1234567890":
            return 0
        right=left+1
        while right<len(str) and str[right] in "1234567890":
            right+=1
        
        if right==left+1 and str[left] in "+-":
            return 0
        rep=int(str[left:right])
        if rep<-2**31:
            return -2**31
        elif rep>2**31-1:
            return 2**31-1
        else:
            return rep
            
