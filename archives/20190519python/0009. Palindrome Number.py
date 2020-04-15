class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        rep=0
        cur=x
        while cur>0:
            rep=rep*10+cur%10
            cur//=10
        return rep==x
