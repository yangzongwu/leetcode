class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """ 
        i=1
        while 2**i<=num:
            i+=1
        rep=2**i-1 
        return rep^num
