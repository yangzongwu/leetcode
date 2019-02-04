class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=num1[::-1]
        num2=num2[::-1]
        rep=0
        for k1 in range(len(num1)):
            for k2 in range(len(num2)):
                rep+=int(num1[k1])*int(num2[k2])*(10**k1)*(10**k2)
        return str(rep)
