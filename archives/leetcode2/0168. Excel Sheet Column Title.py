class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ss="0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n<=26:
            return ss[n]
        rep=''
        while n>0:
            if n%26==0:
                rep='Z'+rep
                n=n//26-1
            else: 
                rep=ss[n%26]+rep
                n=n//26
        return rep
