class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        rep=0
        tmp=x
        while tmp>0:
            cur=tmp%10
            tmp=(tmp-cur)/10
            rep=rep*10+cur
        return rep==x
