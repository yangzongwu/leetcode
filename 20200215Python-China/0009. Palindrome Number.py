class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        if x%10==0:
            return False
        y=0
        tmp=x
        while tmp>0:
            y=y*10+tmp%10
            tmp=(tmp-tmp%10)//10
        return x==y
