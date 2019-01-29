class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        rep1=0
        for num in num1:
            rep1=rep1*10+int(num)
        rep2=0
        for num in num2:
            rep2=rep2*10+int(num)
        return str(rep1+rep2)
        
