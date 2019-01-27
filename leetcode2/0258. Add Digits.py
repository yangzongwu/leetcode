class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        rep=0
        while num!=0:
            rep+=num%10
            num=num//10
        return self.addDigits(rep)
